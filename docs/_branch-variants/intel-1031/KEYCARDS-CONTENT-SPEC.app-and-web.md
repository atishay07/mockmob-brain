# Key cards: content spec (31 Oct 2026, owner D200-D206)

This spec is binding for every agent that authors, checks or imports Key cards. The owner's rule (D202) is
that NCERT's exact language is kept, with the reference, because "that language is what fetches them marks".

## 1. Sources
- **Current NCERT Class 12 chapter PDFs only (Reprint 2026-27).** They live in
  `C:\Users\atish\Desktop\mockmob copy\ncert-books\pdf\` and are named by NCERT code (e.g. `lebs101.pdf` = Business
  Studies Part 1 Ch 1).
- **Read the PDF itself for exact wording.** The Read tool with `pages` shows what is printed.
- **`pdftotext <file> -` (no `-layout`) gives reading-order text.** Use it to search and check, but fix extraction
  artefacts from the printed page. For example "t he" is "the", and a lost dash makes "commonmanagement".
- **Page reference = the printed book page number** in the page corner, not the PDF page index.
- **Chapters outside the CUET 2026 syllabus get no cards** (`syllabus-verified.md` lists them).
- **Topics an NCERT chapter covers that CUET 2026 does not list get no cards either.** This matters most for
  Economics and Biology, where the CUET unit lists name sub-topics.

## 2. Card kinds and labels (shown to students exactly as written in the Label column)

| kind | Label | Front (prompt) | Back (answer) | Typical subjects |
|---|---|---|---|---|
| `definition` | Definition | "Define *X*" or "What is *X*?" (add the author if NCERT names one) | NCERT's exact defining sentence(s) | All |
| `term` | Term | NCERT's exact sentence with the key term replaced by a blank `____` | The term, then the full sentence | All |
| `key_line` | Key line | An important NCERT statement with 1-3 key words blanked | The full line with the blanked words marked | Political Science, Biology, Economics |
| `list` | List | "Name the *N* features/functions/importance of *X*" | NCERT's own numbered or headed list, item titles exact, each with NCERT's first explanatory sentence where short | Business Studies, Biology, Political Science |
| `difference` | Difference | "*X* vs *Y*: the difference on *basis*" | NCERT's own comparison-table row(s), exact | Business Studies, Economics, Biology, Accountancy |
| `steps` | Steps | "Steps in *X*, in order" | NCERT's ordered steps, exact titles | Business Studies (planning, staffing), Biology (processes), Accountancy |
| `types` | Types | "Types of *X*" | NCERT's classification, exact names | All |
| `formula` | Formula | "Formula: *X*" | The formula exactly as NCERT prints it, plus what each symbol means (NCERT wording) | Accountancy ratios, Economics, Biology (equations rarely) |
| `fact` | Fact | A who/when/where/how-many question | The fact, with the NCERT sentence that states it | Political Science, Economics (Indian Economic Development), Biology |
| `example` | Example | NCERT's example or case, with the concept hidden | The concept it illustrates, with NCERT's line | Business Studies, Economics |
| `entry` | Entry | "Journal entry / treatment: *situation*" | The entry or treatment exactly as NCERT shows it | Accountancy |
| `quote` | Quote | "Who said / in which document: '…'" | Source and context, NCERT wording | Political Science |

**English (no NCERT book for CUET English) gets an English deck.** It has its own kinds: `word` (meaning),
`idiom`, `one_word` (one-word substitution), `usage` (correct word or form) and `rule` (grammar rule with a wrong/right
pair). Its sources are WordNet (already licensed in `data/study/sources/`) and authored text. Every English card carries
`source.kind = "authored"` or `"wordnet"`, never NCERT.

## 3. Card record (one JSON object per card)

```json
{
  "id": "kc.business_studies.nature-and-significance-of-management.def-management-koontz",
  "v": 1,
  "subject": "business_studies",
  "chapterKey": "business_studies.nature-and-significance-of-management",
  "chapter": "Nature and Significance of Management",
  "unit": "Nature and Significance of Management",
  "kind": "definition",
  "front": "Define management (Harold Koontz and Heinz Weihrich).",
  "back": "Management is the process of designing and maintaining an environment in which individuals, working together in groups, efficiently accomplish selected aims.",
  "quote": "Management is the process of designing and maintaining an environment in which individuals, working together in groups, efficiently accomplish selected aims.",
  "blanks": [],
  "source": { "kind": "ncert", "book": "Business Studies Part 1", "code": "lebs101", "chapterNo": 1, "page": 3, "section": "Definitions of Management" },
  "importance": "must",
  "asked": 0,
  "tags": ["management"],
  "order": 10
}
```

**Rules:**
- **`quote` is the exact NCERT text the card rests on.** It is mandatory for every NCERT-sourced card.
  - `back` must equal `quote`, or be a substring of it, or (for `list`, `steps` and `types`) be composed only of exact
    NCERT fragments joined by line breaks.
  - For `term` and `key_line`, `front` is `quote` with the blanked words replaced by `____`, and `blanks` lists those
    words in order.
- **Paraphrase is allowed in exactly one place:** the optional `note` field (at most about 160 characters), shown
  below the card as "In short" for explanation (D202).
- **`importance`:**
  - `"must"` covers definitions, boxed and highlighted text, items NCERT lists under a heading, summary points, and
    anything a past CUET paper asked.
  - `"good"` covers the rest.
  - Aim for about 60% `must`.
- **`asked` is the count of real past CUET questions that test this exact point.** Use 0 unless a past-paper match is
  certain. Never guess.
- **`order` follows the book**, so a deck reads in NCERT order.
- **Size:** `front` at most about 140 characters. `back` at most about 420 characters, except `list`, `steps` and
  `types`, which may run to about 700.
- **One idea per card.** Long NCERT paragraphs become several `key_line` cards, not one wall.
- **Blanks** must be the words that carry marks: a term, a number or a name, never "the" or "is". A blank must
  have exactly one right answer given the line.
- **The id is stable:** `kc.<subject>.<chapter-slug>.<kind-short>-<slug>`. Never reuse an id for different content.
  Changing content means `v+1`.

## 4. How many cards
- Each pilot chapter gets about 25-45 cards, more for long chapters.
- Cover every NCERT definition, every headed list, every comparison table and every formula in the CUET-listed part
  of the chapter.
- A chapter with fewer than 15 cards fails the coverage check unless the chapter is genuinely short; say so in
  `coverage_note`.

## 5. Checks (automatic; a failure means quarantine, never forced publication)
1. **Quote:** the normalised `quote` must appear in the normalised `pdftotext` text of the cited PDF. Normalise by
   lowercasing, dropping every character that is not a letter or digit, and joining hyphenated line breaks. The cited
   `page` must contain it, or the page before or after it (for lines that cross a page).
2. **Shape:** the id pattern, required fields and size limits from section 3; `back` and `front` derived from `quote`
   as section 3 says.
3. **Blanks:** each blank word occurs in `quote`, is not a stopword, and is not repeated elsewhere in the `front`.
4. **Duplicates:** no two cards in a subject have the same normalised `quote` and `kind`, and no two have the same
   `front`.
5. **Syllabus:** `chapterKey` resolves to a chapter that is in CUET 2026 (from the verified syllabus map).
6. **Independent review:** a second agent sees only the PDF pages and the card. It answers four questions: Is it exact?
   Is it important for CUET? Is the front unambiguous? Is the importance right? Any "no" means quarantine, with a
   reason.

## 6. Output files
- `data/keycards/decks/<subject>.json`: `{ "subject", "version", "source": "NCERT Reprint 2026-27", "cards": [...] }`,
  published cards only.
- `data/keycards/quarantine/<subject>.json`: failed cards, each with its `reasons`.
- `data/keycards/coverage/<subject>.json`: per chapter, the number of cards by kind and by importance, plus any
  `coverage_note`.
