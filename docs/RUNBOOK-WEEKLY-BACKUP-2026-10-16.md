# Runbook: weekly database backup (16 Oct 2026)

Tool: `scripts/backup/weekly-db-dump.ps1`. It dumps the production Supabase Postgres (schema and data) to a dated compressed file on this PC, keeps the newest 8, and logs a redacted result line. It only reads from the database.

Status: written and tested for argument handling and redaction with a fake URL (dry run). Not yet run against the real database, because `SUPABASE_DB_URL` is not set yet and no dump tool is installed on this PC (checked 16 Oct: no `pg_dump`; `npx` exists but needs Docker).

## 1. Owner steps (one time)

1. Get the connection string. Supabase dashboard, Connect, **Session pooler** (port 5432). Use the pooler, not the direct host: the direct host is IPv6 only on Free and fails on many home networks. The string looks like `postgresql://postgres.<ref>:<password>@aws-0-<region>.pooler.supabase.com:5432/postgres`. Percent-encode special characters in the password (the script decodes them).
2. Set it as a Windows **user** environment variable (Settings, System, About, Advanced system settings, Environment variables, New, under User variables): name `SUPABASE_DB_URL`, value the string. Never paste it in chat or a file.
3. Optional: `MOCKMOB_BACKUP_DIR` for another folder. Default is `Documents\MockMob backups`.
4. Install a dump tool, one of:
   - **PostgreSQL client tools** (recommended; no Docker): https://www.postgresql.org/download/windows/, tick only "Command Line Tools", version 17 or newer (Supabase runs Postgres 17; an older `pg_dump` refuses a newer server). Add `C:\Program Files\PostgreSQL\17\bin` to the user PATH.
   - Or **Docker Desktop**; the script then falls back to `npx supabase db dump`, which runs `pg_dump` in a container.
5. Open a new terminal and check: `powershell -File scripts\backup\weekly-db-dump.ps1 -DryRun`. It prints the host, the tool it chose and the output path, with the password hidden.
6. First real run: `powershell -File scripts\backup\weekly-db-dump.ps1`. Expect "OK ... N tables". Open the folder and confirm the file exists.

Exit codes: 0 ok, 2 bad or missing URL, 3 no tool, 4 dump failed, 5 file empty or tiny, 6 no tables found.

## 2. Weekly schedule (main session)

Pick one. Both run on this PC, so the PC must be on.

- **Windows scheduled task** (survives Claude restarts; preferred):
  `schtasks /Create /SC WEEKLY /D SUN /ST 03:30 /TN "MockMob weekly backup" /TR "powershell -NoProfile -ExecutionPolicy Bypass -File \"C:\Users\atish\Desktop\mockmob copy\mockmob-next\scripts\backup\weekly-db-dump.ps1\"" /RL LIMITED`
  Add "run as soon as possible after a missed start" in Task Scheduler, Settings, so a sleeping PC catches up. User environment variables are visible to a task running as the same user.
- **Claude scheduled-tasks tool** (`mcp__scheduled-tasks__create_scheduled_task`): a weekly task whose prompt runs the same command and reports the last line of `backup.log`. Only works while the Claude app is open.

The scheduling itself is a persistent configuration change, so the main session does it only after the owner says yes and the first manual run has passed.

## 3. Restore into staging (never into production)

Make a **separate** Supabase project (staging) or a local Postgres. Do not restore over production.

For a `.dump` file (pg_dump path):
```
pg_restore --no-owner --no-acl --clean --if-exists -d "<staging connection string>" "mockmob-YYYY-MM-DD_HHMM.dump"
```
Expect harmless errors for Supabase-managed objects (extensions, `auth` and `storage` internals that the new project already has). Restore `public` only with `--schema=public` if the full restore is noisy.

For a `.sql.gz` file (Supabase CLI path):
```
gzip -dc mockmob-YYYY-MM-DD_HHMM.sql.gz | psql "<staging connection string>"
```
Then check row counts of the main tables (`profiles`, `questions`, attempts) against the log line and production, and run the app against staging env vars before trusting the backup.

Do one restore drill soon after the first backup. An untested backup is a guess.

## 4. What Supabase Free does not cover

- No automatic daily backups and no point-in-time recovery on Free; those start on Pro (daily backups, 7 days) and the PITR add-on. This weekly file is the only copy.
- A project paused for inactivity can be lost after the pause window; a backup outside Supabase is the protection.
- Storage objects (files in buckets) are **not** in a database dump, only their metadata rows. Back those up separately if they matter.
- Auth users are in the `auth` schema and are dumped, but restoring them into another project needs the same JWT secret for existing sessions; password hashes carry over.
- Edge functions, secrets, project settings and Vercel settings are not in the dump. Keep their sources in git.
- Weekly means up to 7 days of lost data in the worst case. If that is too much, run it more often (the retention is by count; raise `-Keep`).
- The files hold student data. Keep the folder on this PC only, do not sync it to a shared drive, and treat it as sensitive.
