# Key cards conflict sweep brief (31 Oct 2026)

**Why this sweep:** a student revises Key cards as facts to hold, so a deck must never teach two things that cannot both
be true. NCERT itself sometimes disagrees with itself.

**The known case:**
- Accountancy Part II p. 81 says discount on issue of debentures "can be written off ... during the life time of
  debentures".
- p. 106 says it "is written-off in the year when debentures are issued".
- Two published cards stated the two sides. One is now held back.

**Your job:** find every such conflict among the PUBLISHED cards of one subject.

## Inputs (read only)
- **Cards:** `C:\Users\atish\Desktop\mockmob copy\wt-1031-keycards-web\data\keycards\decks\<subject>.json` (`cards[]`
  with id, chapterKey, kind, front, back, quote, source.page, importance).
- **NCERT text:** the PDFs in `C:\Users\atish\Desktop\mockmob copy\ncert-books\pdf\` (pdftotext, or
  `python "C:\Users\atish\Desktop\mockmob copy\wt-1031-keycards-web\scripts\keycards\pdfium_pages.py" <pdf>`). Use it
  to confirm context.

## What counts as a conflict
Two or more cards where a student who learns both would hold contradictory answers to one question:
- a different rule for the same treatment (when, where or how something is recorded or shown)
- a different number, date, count or list for the same thing
- a different definition of the same term that cannot both hold
- a "never" or "only" on one card that another card breaks

**Not conflicts:**
- Two true statements about different cases. Example: a financial vs a non-financial enterprise, when each card says
  which case it covers.
- A list and one of its items.
- Different wording of the same fact. That is a duplicate, not a conflict; list it separately under `duplicates` when
  a student would see the same fact twice.

**A card that is true in context but misleading out of context:** "only sweat equity shares can be issued at a
discount", when the book elsewhere allows a discount on reissue of forfeited shares, is a conflict if the card does not
carry its context.

## Method
1. Group the cards by chapter and by shared key terms. Use a script in your own scratch folder to find candidate pairs
   with overlapping subject words, then read each candidate pair yourself.
2. Also compare across chapters for the same term, since some topics appear in two chapters.
3. For each real conflict, read both cited pages in NCERT.
4. Decide which card to hold back:
   - Keep the card that states the book's specific, later or more detailed treatment, or the one that matches the law
     or standard the book cites.
   - Hold back the other.
   - If you cannot tell which side the exam would take, hold back both.

## Output
`C:\Users\atish\Desktop\mockmob copy\ncert-books\sweep\conflicts-<subject>.json`:

```json
{ "conflicts": [ { "hold": ["<cardId>", ...], "keep": ["<cardId>", ...], "why": "short, with both pages" } ],
  "duplicates": [ ["<cardId>", "<cardId>"] ], "pairsRead": n }
```

- Do not edit drafts, reviews or decks.
- Scratch goes only in your own `kc-conflict-<subject>` folder inside your temp folder.

## Return
Three lines:
1. Pairs read, conflicts found, cards to hold.
2. The two clearest conflicts.
3. Duplicates found.
