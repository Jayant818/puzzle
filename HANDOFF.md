# HANDOFF — MrBeast $10,000 hidden-video puzzle (updated 2026-09-08)

## Latest Result: Read Before The Historical Notes

**Red solved: FANTASTIC. Blue solved through FOURTH UPLOAD; six-letter terminal
still unverified.** Full evidence, extraction table, source corrections, and
remaining gaps are in `SOLUTION_PROGRESS.md`. Reproduce with
`python3 tools/solve_desk.py`.

**Author errata, September 6:** DoctorXOR confirms that the grass jigsaw piece
has an extra blue I and the red desk paper is missing a 2. The corrected
readings are VII (giving P in Tyto capensis) and (8,3,5,2,4,4). These are
production mistakes, not unresolved extraction clues:
https://www.reddit.com/user/DoctorXOR/comments/1w89jup/comment/p840oup/
In the same post, he says Team Beast alone checks submissions and announces
a winner; he does not know their status. Silence is not a rejection signal.

**Newest corroboration:** `FANTASTIC HEDWIG` exactly matches CiviledXI's public
SHA-256 commitment at
https://www.reddit.com/r/MrBeast/comments/1w7qx8b/6_and_9_letter_words_solved_for/
Run `python3 tools/check_community_hash.py`. This is a community-claim match,
not official contest confirmation; the 251634-to-HEDWIG derivation is still
missing. The user reports already submitting this exact phrase.

**Original-video correction:** the completed submission animation at about
17:26.5-17:26.9 contains **15 asterisks, not 16**. Fresh 10-fps extraction and
counts in five consecutive frames confirm this. See `VIDEO_AUDIT.md` and run
`python3 tools/count_submission_mask.py`. This gives limited support to trying
`FANTASTICHEDWIG` without a space; it does not prove the answer or server rules.

- The jigsaw pictures are owl species; index their scientific names. They give
  BIRDS OF AMERICA and XOR SUPERB OWLS (with the author-confirmed VII correction).
- The pink list indexes historical scientific names, ordered into A-Z slots by
  old English plate titles. Q and X are absent; **QX=TH** supplies their letters.
  The exact output is **MRBEASTSANDWHERETOFINDTHEM**. Replacing crossed-out MR
  gives the nine-letter answer **FANTASTIC**.
- **Correction to the earlier XOR conclusion:** the placeholder IS a case mask.
  `SuperB-owLs14` XOR `%H6U=)Z7</#bq` is `v=F0OkwXKcPSE`, the URL suffix for
  MrBeast's *Hi Me In 10 Years*. The earlier prose-only readability test was wrong.
- The blue sticky decodes by alternating left/right ends to LAST WORD THEN NINTH.
  Those words in the linked video's official captions are **FOURTH UPLOAD**.
- **251634 remains unused. HEDWIG is a checksum-corroborated community candidate**,
  not an independently decoded blue terminal. No assistant submissions were made.
- The fourth main-channel video's third spawn label is **Peahen, not Pelican**.
  See the corrected list and 250-frame OCR results in `SOLUTION_PROGRESS.md`.
- Latest retry: six linked channels' fourth-upload title/caption extractions
  and keyed rail-fence alternatives did not resolve 251634. See progress
  section 7 and `tools/test_blue_alternatives.py`; do not repeat as untried leads.
- September 6 author-history pass found a verified 2019 DoctorXor puzzle with
  grouping/indexing/final-clue mechanics. Also added sampled visual coverage
  of his fourth-oldest video and four main-channel Shorts alternatives; none
  resolved the blue terminal. See `FINDINGS.md` sections 27-28 and progress
  section 9. Do not claim he confirmed this puzzle reuses a particular old one.
- September 6 focused 251634 audit: saved the six literal Minecraft spawn
  labels and 148 bounded label/single-source tests, with no dictionary-word
  result. Direct key order cannot select HEDWIG from those names; destination
  order could only do so with an additional unexplained index sequence.
  See `FINDINGS.md` section 29 and `tools/audit_blue_251634.py`.
- **September 7: consolidated review dossier built.** `LLM_REVIEW_PACKET.md` (plus `.docx`,
  `.pdf` with embedded clue images, `dossier_images/` and `LLM_REVIEW_EVIDENCE.zip`) is a
  standalone packet for an outside reviewer: every clue transcription, both extraction tables,
  the reproducible derivations, the fourth-upload candidates with honest per-video coverage,
  the full test register, a corrections table, and prioritised reviewer questions. Re-check it
  with `python3 tools/verify_dossier.py` (0 failures on 2026-09-07). That pass found no answer
  but did correct four documentation errors and confirm that **251634 is the only clue on
  either chain with no role**; see `FINDINGS.md` section 30.
- September 8 DoctorXOR channel refresh: same 21 public video IDs/order and one
  Short. The walkthrough description has additional links relative to our cache:
  Colin's working spreadsheet and an August 5 podcast interview. The inspected
  spreadsheet tabs corroborate the old hunt's fourth answer TOWARDS; the podcast
  audio remains unreviewed. No new 251634 derivation. See `FINDINGS.md` section 31;
  the September 7 review packet has not been regenerated with this addendum.
- Everything below is historical and may contain conclusions superseded above.

Read this first. It is the single entry point for anyone (human or AI agent) picking this up. Detailed logs: `FINDINGS.md` (chronological, everything tried), `candidates.md` (guess shortlist), `council.md` (persona council verdict). Reproducible material lives in `work/`, scripts in `tools/`.

## 0. TL;DR
- Target: the first correct answer at https://puzzle-video-sweepstakes.mrbeast.app/ wins $10,000. Contest runs 2026-09-02 12:00 ET to 2027-09-02 or first correct entry. Multiple guesses allowed, no penalty, no feedback.
- Video: "How 1 Person Solved A $1,000,000 Puzzle!" on @MrBeast2, id `82CX6WULNA0`, 17:47, published 2026-09-02. Puzzle author: Colin Sanders (DoctorXOR), winner of the $1M hunt.
- Confirmed entry point: pinned comment → tinyurl.com/xorprofile → CyberChef recipe **XOR, UTF-8 key `%H6U=)Z7</#bq`**, input placeholder `AaaaaA-aaAa##` (13 chars). Interpretation: find a 13-character string in the video, XOR it, read the answer.
- Status: **unsolved.** Every mechanical sweep of the video for a literal 13-character token came back empty (1080p and 4K). The only unexplained authored objects are physical props on Jimmy's detective-office desk (handwritten enumeration notes, six sticky notes, fourteen Roman-numeral picture cards). First structural confirmation (2026-09-04): the scrambled blue monitor sticky is an exact anagram of LAST WORD THEN NINTH, whose (4,4,4,5) shape matches the `(4445)` node on the desk note, so the enumeration reading of the notes is right. The (3,6,4) 13-letter phrase that instruction acts on has not been found. Nothing has yet passed the XOR readability gate.

## 1. Hard facts (verified)
| Fact | Evidence |
|---|---|
| Recipe URL | `https://gchq.github.io/CyberChef/#recipe=XOR({'option':'UTF8','string':'%H6U=)Z7</#bq'},'Standard',false)&input=QWFhYWFBLWFhQWEjIw` (tinyurl 301 redirect, `work/` curl log in FINDINGS §1) |
| Key bytes | `25 48 36 55 3D 29 5A 37 3C 2F 23 62 71` |
| Placeholder is a literal case mask | Corrected 2026-09-05: `SuperB-owLs14` produces a valid YouTube URL suffix; see `SOLUTION_PROGRESS.md` |
| Linked CyberChef zip | Stock GitHub Actions build at commit 73a55e35 (2026-09-01); diffed against official v11.4.0, only version strings differ. Not tampered |
| puzzle.pdf | 84-page official answer key to the $1M hunt (SB1-12, PG1-13, GC1-11, OP1-14, MP1-40, MM1-4). Style reference only. Contains none of the new desk props |
| Sweepstakes site | Next.js static. POST /api/entries {guess,email,agree} → entryId → emailed 6-digit code → POST /api/entries/verify → "You're in the running… submit another guess anytime". Server-side only, no correctness feedback, 500-char guess |
| QR at 17:32 | Exactly the sweepstakes URL |
| Thumbnail | Designed "ACCESS DENIED" board with 17 fake login dates, USER ID 127-666-F733, blurry QR; A/B tested against two plain stills, so unreliable as a carrier |
| "674 on the right" (viewer comment) | Three stencilled wall boxes numbered 6, 7, 4 on the right brick wall of the set |
| Colin's second video same day | "The Ramblings of a Million Dollar Winner (Riddle #0: The Hat Trick)" `aFo8P073eSY` — three story riddles, unrelated to the $10k puzzle per its transcript |

## 2. Everything tried, with result (do not redo)
Video/audio (1080p re-encode `vidssave…mp4` and original 4K VP9 `work/orig_4k.webm`):
- Container/metadata, trailing bytes, ID3 → clean.
- Full spectrograms (log, linear, L−R), whole-track pure-tone (DTMF/Morse) scan → nothing. Outro 17:37-17:47 is synth SFX plus a song with vocals ("oh baby" per auto-captions), unidentified.
- Single-frame insert detection at 64×36 and 160×90 (4×4 regions) → only stylistic flickers and white wipes (0:59, 1:07, 1:23, 2:41, 3:24, 5:07, 5:41, 6:20, 11:44, 12:07, 12:12, 16:10.0, 17:12.0, 17:17.9).
- Solid-colour frame scan (base-3 colour cards) → nothing.
- OCR: every second at 1080p (7066 tokens) and every 4 s at 4K tiled (267 frames × 12 tiles), plus 1 fps 4K of intro laptop screens and 3 fps 4K of the ending TV screen → no `XXXXXX-XXXX99`-shaped token, no "674" text.
- Captions: uploaded EN (speaker-coloured) — hyphens, zero-width spaces, colours all structural; FR/ES/DE/JA normal translations; EN uploaded vs auto diff shows no inserted words.
- Digit "rain" shot 17:09 (only appears inside the ending TV montage) → glyph set `=473 2569`, glyphs re-roll randomly each frame (78%→36%→15% agreement over 1,2,5 frames, no shift), so no fixed text. Closed.
- TV static at 17:00 averaged → nothing. Bouncing cookie 17:42-17:47 → plain DVD-logo bounce; final frame is a stock cookie PNG with its transparency checkerboard showing.
- Rapid "INSTRUCTIONS" montage 5:16-5:24 → all PG1-13 cards from the PDF, no extra card.
- Ending-scene props at 4K: box tape blank; TV bezel "zenith / COLOR TV-VCR COMBINATION", no model number; rotary phone has no number card; tablet shows "4:51 PM Sun Mar 8".
- Colin's channel banner/avatar/about → nothing. Sweepstakes site source/cookies/headers → nothing.
- XOR gate run on every structured string visible in the video (vault code chunks, tablet text, IDs, prop numbers, stickies, brand names, dates, hashtags) → all junk. See `tools/xor_check.py`.
- Community: top 300 + newest 1500 comments scraped; only useful signal was the pinned tinyurl and viewers pointing at the desk paper, the phone and "674".
- Anagram/instruction tests (2026-09-04): blue sticky letters `ADEHHILNNNORSTTTW` = LAST WORD THEN NINTH exactly, but 2034 common-word (4,4,4,5) anagrams exist (134 instruction-like), so it is the leading reading, not a proof. Not a `251634` columnar transposition. Yellow sticky `BOOKSWOLDNAMES` is not a (5,2,7) scramble (48 anagrams, all nonsense). OCR of every frame holds no (3,6,4) all-caps block. "Last word, then ninth" applied to the transcript, title, description and pinned comment gives nothing ("video"/"Bowl", "Puzzle!").
- Outside write-ups received so far (two AI analyses) were checked line by line; their verified points are folded in above, their unverified claims (IP flagging, no cooldown, "bypass the final steps") are not.

## 3. Open leads (the actual candidate material) — details and crops in FINDINGS §9
All found on Jimmy's desk / the boxes behind it; same desk and same orange rotary phone reappear in the ending TV scene. Best frames: 0:18 (`work/frames4k/desk765/d_18.png`), 5:40 (`frames4k/notes/n_340_full.png`), 12:45 (`frames4k/desk765/d_765.png`), 17:00-17:47.
1. **Handwritten number notes** (red ink) `(527)` → `(83544)` → `M̶R̶ (9)`; (blue ink) `(364)` and `(4445)` → `(66)` → `(6)`. Read as crossword-style enumerations: (3,6,4)=13 letters = placeholder length. Trivial numeric readings (A1Z26, sums, products, T9, area codes, hex/octal) rejected.
2. **Six stickies on the black case**: `081 XIV Seahawks?`, `## How many?`, `QX=TH` (cryptogram crib), `251634` (permutation of 1-6), `PLATES`, `YouTube link.. watch?`.
3. **Fourteen emoji-style picture cards** with one red and one blue Roman numeral each, notched so they can chain: elf II/XI · window I/VII · falling chart VIII/IX · ribbon V/VII · door VI/VIII · snow cloud IX/V · laughing-crying face XIV/X · hedgehog+eagle IX/VII · Route 66 IV/II · teal ticket VI/VI · Oman flag VI/V · Africa+pineapple VIII/IV · US flag+barn IV/VII · bull VII/?. Desk sticky "Roman numbers for Roman words?" refers to them. Inventory incomplete (several seen edge-on).
4. **Pink note** by the keyboard (9:04): NOT a cryptogram — it is 24 (number, Roman numeral) pairs, now legible via a community collage: 029 III, 039 VI, 042 V, 061 II, 074 IX, 076 IV, 081 XIV, 083 XI, 101 II, 102 III, 112 IX, 162 V, 184 V, 216 I, 225 VI, 235 VII, 245 VIII, 246 VIII, 253 XIV, 275 III, 329 X, 337 VI, 358 IX, 424-6 XVI. Reads as an index (page/line or player/episode); source unidentified. See FINDINGS §15b.
5. Monitor stickies: blue `LSWRTE / NNHTIN / HDOTA — should I call it bird food?` — its 17 letters are an exact anagram of **LAST WORD THEN NINTH** (4,4,4,5), matching the `(4445)` node on the blue note. Leading reading but not unique (2034 common-word anagrams; 134 instruction-like). Yellow `Books w/ old names… Alphabetize?` is plain text, likely an ordering hint. See FINDINGS §12.
6. Wall boxes 6-7-4 (colours blue, pink, white).
**Jigsaw mechanic, best current model (FINDINGS §16–16c):** the pieces are ordered by their physical tabs and notches (numeral-matching was tested and does not give a unique chain once colours are read correctly). Each card = picture word + RED numeral + BLUE numeral. 14 red numerals ↔ the red note's (5,2,7) 14-letter phrase; 13 visible blue numerals ↔ the blue note's (3,6,4) 13-letter phrase. Extract the indexed letter from each picture's word in jigsaw order to get both phrases; then apply LAST WORD THEN NINTH (blue chain) and the still-unknown (8,3,5,4,4) instruction (red chain). Corrected colour reads are in FINDINGS §16b.

## 4. Council verdict (5 personas, 2026-09-03) — full text in `council.md`
Unanimous Option A (mean 62%): decode the desk props; the recipe is a verifier for a constructed answer, not a search target. Einstein's two-day falsification test: complete the card inventory; if no domino chain exists and neither numeral colour is a permutation of I..N, the cards are decoration and effort moves back to the two unchecked audio gaps (reversed audio, outro song ID). Sharpest caveat (Munger): the placeholder's hyphen and two trailing digits sit uneasily against a 13-letter enumerated phrase.

## 5. Guessing strategy
No feedback and no penalty, so submit plausible answers by hand as they arise (one email code per guess; do not script it — rules forbid tampering). Ranked list in `candidates.md` (Tiers 1-5). On the first wrong guess, inspect the raw JSON of `/api/entries` and `/api/entries/verify` in DevTools: the page only reads `entryId` and `error`; any extra field would be an oracle.

## 6. Files
- `FINDINGS.md` — full chronological log, dead ends, prop inventory with frame references.
- `candidates.md` — guess shortlist and submission mechanics.
- `council.md` — persona council transcript summary.
- `tools/xor_check.py` — gate: XOR any candidate with the key, flags printable/readable. `tools/ocr_all.py`, `tools/ocr_tiles.py` — the OCR sweeps (rapidocr).
- `work/orig_4k.webm` — original 3840×2160 VP9 stream (format 313). `work/frames/` — 1 fps 1080p frames and contact sheets. `work/frames4k/` — 4K frames and prop crops (`desk765/`, `notes/`, `cards/`, `pink/`, `rain/`, `tvm/`). `work/audio/` — spectrograms, mono WAV. `work/yt/` — description, info.json with comments, captions (EN + 4 languages + auto), Colin's two videos' transcripts, thumbnails. `work/site/` — sweepstakes HTML, headers, rules, JS bundles. `work/cyberchef/`, `work/cc_official/` — linked and official CyberChef builds. `work/ocr*.json` — OCR outputs.
- Environment notes: yt-dlp must be ≥ 2026.08 with deno installed or YouTube truncates the 4K stream at 92 MB; rapidocr_onnxruntime and opencv-contrib-python-headless were pip-installed with `--break-system-packages`.

## 6b. Colin's on-record starting hint (Twitch, 2026-09-03 night; FINDINGS §14)
"Have you solved the jigsaw puzzle? In MrBeast's video, the first thing you should do is look for a jigsaw puzzle." He made the puzzle alone, says it is smaller than the Super Bowl hunt, and will not discuss it until Team Beast announces a winner (none announced as of then). So: the fourteen notched cards are the entry point. Community state is in FINDINGS §15 (bird FENCE = rail fence; pink note = number/Roman-numeral index; 674 = Nauru dialling code; claimed jigsaw reading SUBSCRIBE TO MRB, unverified).

## 6c. Community solution structure (2026-09-05, unverified; FINDINGS §17)
Redditors claim: red pad (5,2,7) = BIRDS OF AMERICA, with the pink pairs as Audubon plate numbers + letter indexes, alphabetized, MR struck → a 9-letter word (they say BEASTSAND); blue pad (3,6,4) = XOR SUPERB OWLS → (6,6) FOURTH UPLOAD → LAST WORD THEN NINTH → a 6-letter word. Both phrase lengths match our red/blue numeral counts exactly. None of their words pass the XOR gate, so the CyberChef recipe is a step inside the blue chain ("XOR"), not a final-answer check.

## 6d. Red chain is now computable (FINDINGS §18)
All 435 Havell plate names are in `work/audubon/havell_plates_pitt.json`. The 24 pink pairs map to 24 letters = the red pad's (8,3,5,4,4) instruction. First extraction (Audubon titles, spaces removed, alphabetized by bird) gives `CUEDCRR?MR?ERDABAELWGWAI` — not yet clean because two indexes overflow the Audubon titles (modern names such as Pomarine Jaeger fit), so the remaining work is choosing the right name form and sort key until an English 24-letter sentence appears.

## 7. Working model of the puzzle (best current hypothesis)
Two chains on the desk, each = [scrambled source] + [scrambled instruction] → intermediate → final:
- Blue chain: a (3,6,4) 13-letter phrase [unfound] + instruction LAST WORD THEN NINTH (from the blue sticky) → (6,6) → a 6-letter final.
- Red chain: a (5,2,7) 14-letter phrase [unfound] + a (8,3,5,4,4) 24-letter instruction [unfound] → a 9-letter final; "MR" was written and struck out before the (9).
- The 13-letter (3,6,4) phrase is the prime candidate for the CyberChef input; the finals may be what the sweepstakes form wants (note the ending card "SUBSCRIBE FOR A COOKIE": SUBSCRIBE is 9 letters, COOKIE is 6 — unproven, but it fits both chain lengths).
- Likely sources for the unfound phrases: the fourteen Roman-numeral cards (13-14 letters, "Roman numbers for Roman words?"), the illegible pink note (with `QX=TH` as crib), and the `251634` / "Alphabetize?" notes as ordering steps.

## 6e. Latest tests (FINDINGS §19)
Pink numbers are not MrBeast upload indices; owl-plate ⊕ Super-Bowl arithmetic fails; phrase strings fail the XOR key. MrBeast's fourth-ever upload is "More birds IN MINECRAFT!!" (Jan 2013) — a thematic fit for FOURTH UPLOAD and BIRDS OF AMERICA; title last word MINECRAFT (9 letters). Unresolved.

## 8. Suggested next actions for the next agent
1. Finish the card inventory from the 0:18 and 12:45 4K frames (both numerals, exact picture); test emoji-name and Latin-name indexing by numeral, domino chaining on matching numerals, and the `251634` order. Any 13-letter (3,6,4) result goes straight into `tools/xor_check.py`.
2. If a (3,6,4) phrase appears, also apply LAST WORD THEN NINTH to it and to its XOR output, and submit every readable result.
3. Hunt for a legible source of the pink note (BTS photos, shorts, Colin's Thursday Twitch stream); with `QX=TH` as a crib a substitution solver will finish it fast.
4. Identify the outro song and check reversed audio 17:36-17:47 (cheap, unchecked).
5. Keep submitting from `candidates.md` while working; log every submitted guess with a timestamp in `candidates.md`. Add SUBSCRIBE and COOKIE as guesses if not already sent.
