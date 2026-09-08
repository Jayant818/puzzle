# MrBeast $10,000 Video Puzzle — Independent Review Dossier

- **Compiled:** 2026-09-07
- **Research window:** 2026-09-02 → 2026-09-07
- **Status of the puzzle at time of writing:** partially solved; one step demonstrably missing.
- **Purpose:** hand this to an independent reviewer and ask what has been missed.

---

## 0. Ready-to-use independent-review prompt

> Copy everything below the line into a fresh model session together with this whole document.

---

You are an independent puzzle-hunt reviewer. The document that follows is a research dossier on
an unsolved step of a live cryptic puzzle contest. It was assembled by a prior solver team, and
it deliberately separates four evidence classes: **observed fact**, **reproducible deduction**,
**assumption**, and **speculation / community claim**. Respect those labels; do not silently
promote one class into another.

Your job is **not** to hand back a guess. Your job, in this order:

1. **Falsify.** Find any claim in Sections 4–7 that is wrong, circular, or rests on an
   unstated assumption. Say exactly which claim and why. A confident "these all check out"
   is a valid answer only if you actually re-derived them.
2. **Find the gap.** The unsolved step is stated precisely in Section 1.2. Identify mechanisms
   that would consume the unused clue **251634** and produce a six-letter result, and rank them
   by how much clue support each has — not by how nice the output word looks.
3. **Name what is untested.** Section 9 lists known holes (unread props, un-reviewed video/audio,
   sampling gaps). Add holes the team did not list.
4. **Challenge the frame.** If you think the whole blue-chain model after `FOURTH UPLOAD` is
   mis-framed, say so and give the alternative reading.

Hard constraints:

- **Do not reverse-engineer toward HEDWIG.** A candidate answer exists and is described in
  Section 10. Treating it as the target and searching for a rule that emits it is the single
  most common failure mode here, and it has already produced several false leads. If you propose
  a mechanism, it must be justified by a clue *before* you look at what it outputs.
- Do not claim the puzzle is solved, or that the prize is still available. Neither is known.
- Do not treat sampled frames, OCR runs, captions, contact sheets, or spectrograms as complete
  visual or audio review. The dossier is explicit about where coverage is sparse.
- Do not treat community agreement, upvotes, or a matching hash as verification of correctness.
- Do not suggest contacting the organizers, the author, or other solvers, and do not suggest
  submitting entries on anyone's behalf.

Deliver: (a) a list of confirmed errors or weak links, (b) ranked candidate mechanisms for the
missing step with their clue justification, (c) the highest-value untested check you would run
next and exactly how you would run it.

---

## 1. Executive summary

### 1.1 What the puzzle is

MrBeast's second channel published *How 1 Person Solved A $1,000,000 Puzzle!* on 2026-09-02.
Hidden in the set dressing of that video is a new puzzle written by Colin Sanders (Reddit and
YouTube handle **DoctorXOR**), the winner of the earlier $1,000,000 hunt. The first person to
submit the correct answer at `https://puzzle-video-sweepstakes.mrbeast.app/` wins $10,000.

The puzzle is built as **two parallel chains** drawn as flowcharts on two pads on the desk set:

| Chain | Source phrase | Instruction phrase | Intermediate | Terminal |
|---|---|---|---|---|
| **Red** (red ink pad) | `(527)` = **BIRDS OF AMERICA** | `(8 3 5 [2] 4 4)` = **MRBEASTS AND WHERE TO FIND THEM** | — | ~~MR~~ `(9)` = **FANTASTIC** |
| **Blue** (blue ink pad) | `(364)` = **XOR SUPERB OWLS** | `(4 4 4 5)` = **LAST WORD THEN NINTH** | `(66)` = **FOURTH UPLOAD** | `(6)` = **unsolved** |

### 1.2 The precise unsolved problem

> **Given the verified intermediate `FOURTH UPLOAD`, and the unused blue sticky note `251634`,
> derive a six-letter terminal answer by a rule that is supported by a clue in the video.**

Everything up to and including `FOURTH UPLOAD` is reproducible from local evidence and is
re-derived by a script in this repository. After that point the chain stops. Specifically:

- `251634` is a permutation of the digits 1–6. It is written on a **blue** sticky in **blue** ink,
  so by the puzzle's own colour convention it belongs to the blue chain. It has no demonstrated role.
- The blue chain's own flowchart shows `(66) → (6)`: two six-letter words must become one
  six-letter word. No rule for that reduction has been found.
- `FOURTH UPLOAD` is naturally read as *"go to the fourth upload"*, but which channel's fourth
  upload, and what to extract there, are both unestablished. Twelve candidate videos have been
  checked at varying (mostly sparse) depth. None produced a justified six-letter result.

### 1.3 What is and is not established

| Claim | Status |
|---|---|
| Red terminal = **FANTASTIC** | **Reproducible deduction.** Derived end-to-end from cached Audubon data; exact, no fudging. Re-run `tools/solve_desk.py`. |
| Blue verified through **FOURTH UPLOAD** | **Reproducible deduction.** Same script asserts it from the linked video's official captions. |
| **251634** unexplained | **Observed fact.** 148 bounded indexing tests + this dossier's own extra test produced no dictionary word. |
| **FANTASTIC HEDWIG** is the answer | **Unverified community claim.** It matches a public SHA-256 commitment posted by a solver (Section 10.2), which proves agreement with that poster, not correctness. Its blue half has never been extracted by anyone publicly, including us. |
| Two production errors confirmed by the author | **Observed fact**, primary source in Section 12. |
| Final entry animation shows **15** asterisks | **Observed fact**, re-counted at three thresholds across 5 sampled + 13 native frames. |
| The prize is still unclaimed | **Unknown.** A live entry form proves nothing. No winner announcement was found, but the search was not exhaustive. |
| The user's submitted entry was rejected | **Unknown, and unknowable from silence.** Contest rules explicitly say the Sponsor will not correspond with non-winning entrants (Section 3.4). |

### 1.4 Evidence-grade key used throughout

| Tag | Meaning |
|---|---|
| **[OBS]** | Directly observed in a cached local file (video frame, caption file, HTML, image). Anyone with the file can see it. |
| **[REPRO]** | Deduction reproduced mechanically by a script in `tools/`, with asserts. |
| **[ASSUME]** | A working assumption that the chain depends on but which is not independently proven. |
| **[SPEC]** | Speculation or hypothesis, ours. |
| **[CLAIM]** | Asserted by a third party (community solver, secondary source). Not verified. |
| **[AUTHOR]** | Stated by the puzzle's author on the record. |

---

## 2. Original puzzle context, sources, and dates

### 2.1 The video [OBS]

| Field | Value |
|---|---|
| Title | *How 1 Person Solved A $1,000,000 Puzzle!* |
| URL | `https://www.youtube.com/watch?v=82CX6WULNA0` |
| Channel | MrBeast 2 (`@MrBeast2`) |
| Published | 2026-09-02 |
| Duration | 1067 s (17:47), 31,981 frames |
| Native format | 3840×2160 VP9 (yt-dlp format 313), 30000/1001 fps |
| Stats at capture | 1,619,771 views / 120,059 likes |

Local copies: `work/orig_4k.webm` (1.7 GB original 4K stream) and a 1080p re-encode in the
repository root. Metadata `work/yt/mb_video.info.json`; captions `work/yt/mrbeast.en.vtt`
(uploaded EN) and `work/yt/mb_auto.en.vtt` (auto), plus FR/ES/DE/JA tracks.

### 2.2 The entry point [OBS]

The **pinned comment** by @MrBeast on the video reads:

> Make sure you check out Colin's profile 👀 https://tinyurl.com/xorprofile

That TinyURL 301-redirects to a CyberChef recipe:

```
https://gchq.github.io/CyberChef/#recipe=XOR({'option':'UTF8','string':'%H6U=)Z7</#bq'},'Standard',false)&input=QWFhYWFBLWFhQWEjIw
```

- Operation: **XOR**, key = UTF-8 string `` %H6U=)Z7</#bq `` , scheme Standard, null-preserving off.
- Key bytes: `25 48 36 55 3D 29 5A 37 3C 2F 23 62 71` (13 bytes).
- Input placeholder, base64 `QWFhYWFBLWFhQWEjIw`, decodes to **`AaaaaA-aaAa##`** — 13 characters,
  encoding a shape: capital, 4 lowercase, capital, hyphen, 2 lowercase, capital, lowercase, 2 digits.

The recipe is therefore not a search target for a 13-character string printed somewhere in the
video. It is a *verifier for a string you construct*. This was the single largest early
misdirection in this research (Section 12).

### 2.3 Other linked material [OBS]

| Item | URL / file | Relevance |
|---|---|---|
| $1M hunt answer key | `mrb.gg/p/puzzle` → `puzzle.pdf`, 84 pages, produced 2026-08-13 | Style reference for Colin/Lone Shark idioms. Contains **none** of the new desk props (all 84 pages checked). |
| Colin's channel | `https://www.youtube.com/@doctorxor` | Banner/avatar/about contain nothing puzzle-relevant. |
| Colin's walkthrough | `https://youtu.be/XCOkRKUe3Nc` — *How to Solve a $1,000,000 Puzzle*, 31:07, 2026-09-02 | Solve-through of the old hunt. |
| Colin's second same-day upload | `aFo8P073eSY` — *The Ramblings of a Million Dollar Winner (Riddle #0: The Hat Trick)*, 11:48 | Three unrelated story riddles. |
| Offline CyberChef zip | `CyberChef_73a55e35….zip`, 83 MB | Stock GitHub Actions build at commit `73a55e35` (2026-09-01). Diffed file-by-file against official v11.4.0: identical except version strings. **Not tampered.** |
| Six "SUB TO ALL CHANNELS" links | channel IDs `UCX6OQ3DkcsbYNE6H8uQQuVA`, `UC4-79UOlP48-QNGgCko5p2g`, `UCIPPMRA040LQr5QPyJEbmXA`, `UCUaT_39o1x6qWjz7K2pWcgw`, `UCAiLfjNXkNv24uhpzUgPa6A`, `UCZzvDDvaYti8Dd8bLEiSoyQ` | = MrBeast, MrBeast 2, MrBeast Gaming, Beast Reacts, Beast Philanthropy, Beast Animations. Tested as a "six fourth-uploads" source for 251634; no result (Section 7). |

### 2.4 Contest rules, verbatim extracts [OBS]

Cached at `work/site/rules.html` (fetched 2026-09-02 and 2026-09-05; Vercel-hosted Next.js).

> "The Contest begins at 12:00 p.m. Eastern Time ("ET") on September 2, 2026 and ends at
> 11:59 a.m. ET on September 2, 2027 **or when the winning answer has been successfully
> received by Sponsor as determined by it**, … whichever occurs first."

> "The first correct answer submitted to Sponsor during the Contest Period via the Website, if
> any, as determined by Sponsor in its sole discretion, will win the Grand Prize… **TO WIN YOU
> MUST BE THE FIRST PERSON TO SUBMIT THE ANSWER TO SPONSOR 100% CORRECTLY AS DETERMINED BY
> SPONSOR IN ITS SOLE DISCRETION.** … YOU ARE NOT A WINNER OF THE GRAND PRIZE EVEN IF YOU HAVE
> BEEN NOTIFIED THAT YOU SUBMITTED THE CORRECT ANSWER UNTIL VERIFICATION IS COMPLETE…"

> "Sponsor and their personnel **will not enter into any correspondence, including email, with
> non-winning Entrants** relating to such Entrants' participation in the Contest."

> "One (1) Grand Prize is available consisting of $10,000…"

> "Sponsor reserves the right, in its sole discretion, to disqualify any individual found
> **tampering with the proper administration of the Contest**…"

Two consequences that matter for reasoning about status:

- **Silence after a submission is uninformative.** The rules guarantee no correspondence with
  non-winning entrants, and a *winning* entrant is contacted only through a verification process
  of unstated duration. Neither outcome produces a signal on the entrant's side within any known
  window. [OBS]
- **The matching rule is unpublished.** "100% correct as determined by Sponsor" gives no
  guidance on case, spacing, or punctuation. Any reasoning that depends on the server accepting
  a particular format is [SPEC]. [OBS]

### 2.5 Submission mechanism [OBS]

From the site's JavaScript bundles (`work/site/*.js`):

1. `POST /api/entries {guess, email, agree}` → returns `entryId`; a 6-digit code is emailed.
2. `POST /api/entries/verify {entryId, code}` → "You're in the running. You can submit another
   guess anytime."
3. No client-side answer check, no correctness feedback. Guess field is free text, max 500 chars.
4. Multiple guesses are explicitly invited. The tampering clause means guesses must be entered
   by hand, not scripted.

**The assistant has submitted no entries and contacted no one.** The user reports having
submitted `FANTASTIC HEDWIG` on 2026-09-05 (exact time not recorded) and reports no response.

---

## 3. The set and where the clues sit

All puzzle props are on and around Jimmy's "detective office" desk (video 0:45–15:40), plus the
same desk seen again through a TV screen in the ending scene (17:00–17:47).

**Best frames**, with 4K crops cached under `work/frames4k/`:

| Time | Seconds | What it shows | Cached frame |
|---|---|---|---|
| 0:18 | 18 | Widest view of the boxes carrying the jigsaw pieces | `frames4k/desk765/d_18.png` |
| 5:36–5:40 | 336–340 | Red enumeration pad, box column | `frames4k/notes/n_340_full.png` |
| 9:04 | 544 | Monitor stickies, pink index note, keyboard sticky | `frames4k/f_544.0.png`, `frames4k/d544_mon_stickies.png` |
| 12:45 | 765 | Clearest desk: blue pad, six case stickies, phone | `frames4k/desk765/d_765.png` |
| 17:00–17:47 | 1020–1067 | Ending TV scene: same desk, blue pad partly under a box | `frames4k/f_1020.3.png` … |
| 17:26.5–17:26.9 | 1046.5–1046.9 | Completed mock entry form: 15 asterisks | `work/video_audit/typing/frame_016..020.jpg` |

A high-quality community-assembled collage of nearly every prop is cached at
`work/reddit/img/r02.png` and reproduced as `dossier_images/01_desk_prop_collage.jpg`. Several
readings in this dossier are sharper in that collage than in our own 4K crops, because the
poster had access to a cleaner source. Where that matters it is flagged.

---

## 4. Exact clue transcriptions

Uncertainty is stated per item. "Legible" means unambiguous at the stated source; "inferred"
means the transcription required judgement.

### 4.1 The two enumeration pads

**Red-ink pad** (visible 5:36–5:40 and 12:45; `dossier_images/04_red_pad.jpg`) — flow runs
right to left:

```
(5 2 7)  →  (8 3 5 4 4)  →  M̶R̶ (9)
```

- Legible. "MR" is written and physically struck through before the `(9)`. [OBS]
- The author has confirmed the second node is **missing a 2**: intended `(8 3 5 2 4 4)`. [AUTHOR]

**Blue-ink pad** (12:45; `dossier_images/03_blue_flowchart.jpg`):

```
(3 6 4)     (4 4 4 5)
     \         /
       (6 6)
         |
        (6)
```

- Legible. Both top nodes arrow into `(66)`, which arrows into `(6)`. [OBS]
- In the ending scene the same sheet is partly under a box and reads `(364) → (6 2… → (6)`.
  That "62" is the `(66)` seen at a worse angle; a community commenter mistook it for a
  separate `(62)` node. Resolved. [OBS]
- **There is no strike-through anywhere on the blue pad**, unlike the red pad's struck `MR`.
  A community solver flagged this as significant; we record it as an observation, not a rule. [OBS]

**Reading:** these are crossword-style enumerations (word lengths). Trivial numeric readings
(A1Z26, digit sums, products, phone keypad / T9, US area codes, hex, octal) were tested and
rejected. [REPRO, negative]

### 4.2 The six stickies on the black equipment case

`dossier_images/02_case_stickies.jpg`, from 12:45. They **alternate colour and ink**, and the
colours match the two chains:

| # | Sticky colour | Ink | Text | Chain | Status |
|---|---|---|---|---|---|
| 1 | Yellow | Red | `081 XIV` / `Seahawks?` | Red | **Used.** Plate 81 is *Fish Hawk or Osprey* — a sea hawk — and is one of the 24 pink pairs. The joke is the label. |
| 2 | Blue | Blue | `# #` / `How many?` | Blue | **Used.** Two digit-slots; the answer is 14, the number of jigsaw pieces, which supplies the `14` at the end of the CyberChef input. |
| 3 | Yellow | Red | `QX=TH` | Red | **Used.** Supplies the two alphabet slots (Q and X) that no Audubon plate title begins with. |
| 4 | Blue | Blue | `251634` | Blue | **UNUSED — this is the gap.** |
| 5 | Yellow | Red | `PLATES` | Red | **Used.** Identifies the pink numbers as Audubon plate numbers. |
| 6 | Blue | Blue | `YouTube link..` / `watch?` | Blue | **Used.** Supplies the `https://www.youtube.com/watch?` wrapper for the XOR output. |

This alternation is a strong structural signal and is [OBS] from the image: three yellow/red
stickies serve the red chain, three blue/blue stickies serve the blue chain. Two of the three
blue stickies are consumed. **`251634` is the only blue clue with no role.**

`251634` is written as six uninterrupted digits. There are no colons, decimal points, arrows or
separators. A timestamp reading would require inventing punctuation that is not on the note. [OBS]

### 4.3 Monitor stickies (9:04)

`dossier_images/06_monitor_stickies.jpg`.

**Blue sticky**, three lines of block capitals plus a subtitle:

```
LSWRTE
NNHTIN
HDOTA
Should I call it bird f____?
```

- The 17 letters are legible. [OBS]
- The subtitle's last word is **uncertain at our best 4K crop**: our own crop supports
  "bird food?"; the community collage reads "bird **Fence**?" and the community reading is
  thematically coherent (rail **fence** cipher). Neither reading changes the decode.
  **Flagged uncertainty.** [OBS / partly CLAIM]

**Yellow sticky:** `Books w/ old names…` / `Alphabetize?` — legible. [OBS]

**Keyboard sticky (orange, 9:04):** `Roman numbers for Roman words?` — legible. Refers to the
jigsaw pieces' Roman numerals indexing *Latin* (Roman) scientific names. [OBS]

### 4.4 The pink index note (9:04, left of the keyboard)

`dossier_images/05_pink_note.jpg`. Twenty-four (number, Roman numeral) pairs, hand-printed in
two columns, numbers ascending in each column. **Fully legible in the community collage**; our
own 4K crops are motion-blurred beyond reading, so this transcription's provenance is the
collage, cross-checked against the extraction working exactly. [OBS via collage]

```
029 III      039 VI
042 V        061 II
074 IX       076 IV
081 XIV      083 XI
101 II       102 III
112 IX       162 V
184 V        216 I
225 VI       235 VII
245 VIII     246 VIII
253 XIV      275 III
329 X        337 VI
358 IX       424-6 XVI
```

`424-6` means plate 424, **figure 6** (that plate is a six-figure composite). [REPRO — confirmed
against the plate concordance, Section 5.2.]

The pink note lies on top of a printed sheet carrying a small table, which is illegible in every
frame. [OBS — unresolved, Section 9.]

### 4.5 The fourteen jigsaw pieces

`dossier_images/07_jigsaw_pieces.jpg`, `10_piece_atlas.jpg`. Each piece is a notched/tabbed tile
carrying one picture, one **red** Roman numeral, and one **blue** Roman numeral. Thirteen pieces
carry both; the Tasmania piece carries only a red numeral.

Pictures (as drawn): elf · barred door · bar chart with a down arrow at the smallest bar ·
spectacles · Feastables chocolate bar · snow cloud · face-with-tears-of-joy · Tasmania silhouette ·
calendar showing 25 · Oman flag · Africa + grass · US flag + red barn · pharaoh/eagle · brown square.

A wall poster near the desk shows a black book captioned **"Boo!" / "Five of these"**
(`dossier_images/11_boo_five_of_these.jpg`) — i.e. BOO + BOOK = **boobook**, and five pieces are
boobook owls. [OBS]

### 4.6 Other set text (recorded, not used)

| Item | Text | Note |
|---|---|---|
| Wall electrical boxes, right brick wall | circled **6** (blue), **7** (pink), **4** (white/black), top to bottom | The "674 on the right" a commenter asked Colin about. `+674` is Nauru's dialling code. No role found. [OBS] |
| Second badge set beside them | **2** (teal), **1** (white), **4** (orange) | No role found. [OBS] |
| Wall stickies | `LIMA PERU`, `X'S ON BELT`, `LIGHT BLINKS`, `CODE ON DOOR`, `DASHES` | All map to $1M-hunt puzzles in `puzzle.pdf` (SB2/SB3/SB4/SB12). Recap dressing. [REPRO] |
| Cardboard box handwriting | `July 1st 1988 – June 30 89`; another box `INVOICES 2008-02` | Partly hidden. No role found. [OBS] |
| Jet tail number | `N407TC` | Recap prop. [OBS] |
| Road-sign board | 170, 12, 20, 20, 8, 126, 199, 30, 101, 38, 4, 880 | This is the old hunt's GC9 prop. Two community members could not find it in the video and concluded it was fabricated; it is in the collage and is recap dressing. [OBS] |
| Ending card | `SUBSCRIBE FOR A COOKIE` | SUBSCRIBE = 9, COOKIE = 6 — matches both terminal lengths. Tested as a guess pair; unverified coincidence. [SPEC] |
| Mock entry form (TV montage) | Title `BEAST SWEEPSTAKES`, placeholder `Type your answer here...` | The completed animation shows 15 asterisks. Section 6.5. [OBS] |

---

## 5. The two solved chains, reproducibly

Everything in this section is re-derived by `python3 tools/solve_desk.py`, which asserts each
result and fails loudly if any input changes.

### 5.1 The owl jigsaw: identification and index table [REPRO]

Each picture names an owl species; the Roman numerals index that species' **scientific** name
with spaces removed (the "Roman numbers for Roman words?" sticky). Red numerals spell the red
source phrase; blue numerals spell the blue source phrase.

| # | Picture | Owl | Scientific name | Red numeral | Red letter | Blue numeral | Blue letter |
|---|---|---|---|---|---|---|---|
| 1 | Oman flag | Omani owl | *Strix butleri* | VI | **B** | V | **X** |
| 2 | Calendar, 25 December | Christmas boobook | *Ninox natalis* | II | **I** | IV | **O** |
| 3 | Chocolate bar (Feastables) | Chocolate boobook | *Ninox randi* | VI | **R** | VI | **R** |
| 4 | Snow cloud | Snowy owl | *Bubo scandiacus* | IX | **D** | V | **S** |
| 5 | Brown square | Brown boobook | *Ninox scutulata* | VI | **S** | VIII | **U** |
| 6 | Africa + grass | African grass owl | *Tyto capensis* | IV | **O** | VII\* | **P** |
| 7 | Face with tears of joy | Laughing owl | *Ninox albifacies* | X | **F** | XIV | **E** |
| 8 | Spectacles | Spectacled owl | *Pulsatrix perspicillata* | V | **A** | VII | **R** |
| 9 | Bar chart, arrow at smallest bar | Least boobook | *Ninox sumbaensis* | VIII | **M** | IX | **B** |
| 10 | Tasmania silhouette | Tasmanian boobook | *Ninox leucopsis* | VII | **E** | — | *(none)* |
| 11 | US flag + red barn | American barn owl | *Tyto furcata* | VII | **R** | IV | **O** |
| 12 | Elf | Elf owl | *Micrathene whitneyi* | II | **I** | XI | **W** |
| 13 | Pharaoh / eagle | Pharaoh eagle-owl | *Bubo ascalaphus* | VII | **C** | IX | **L** |
| 14 | Barred door | Barred owl | *Strix varia* | VII | **A** | I | **S** |

Reading down the table:

```
RED  (14 letters):  B I R D S O F A M E R I C A   →  BIRDS OF AMERICA   = (5,2,7) ✔
BLUE (13 letters):  X O R S U P E R B O W L S     →  XOR SUPERB OWLS    = (3,6,4) ✔
```

\* **The grass piece visibly shows VIII, which would give E and break the word.** On 2026-09-06
the author confirmed the piece carries **one extra blue I by mistake**; the intended numeral is
VII, giving P. Primary source in Section 12. [AUTHOR]

**[ASSUME] — the ordering.** The table's row order is the order that makes both phrases read.
It has *not* been independently established by physically assembling the tabs and notches from
the video, because several pieces are only ever seen edge-on or partly covered. An earlier
attempt to order the pieces by domino-matching numerals (blue of one = red of the next) produced
two competing chains and duplicate values, so numeral-matching is **not** the ordering rule.
The author's own starting hint — "look for a jigsaw puzzle" — implies physical tab/notch
assembly. The order is therefore *confirmed by its output*, which is weaker evidence than
confirming it by the pieces. Section 13 asks a reviewer to attack this.

### 5.2 Red chain: the Audubon extraction [REPRO]

`PLATES` + `BIRDS OF AMERICA` ⇒ the pink numbers are plate numbers in Audubon's *The Birds of
America* (435 Havell plates). The Roman numeral indexes a letter of the plate's **historical
scientific name** (the binomial printed on the original plate, not the modern name). The 24
extracted letters are then placed into **alphabetical slots keyed by the initial of the plate's
old English title** ("Books w/ old names… Alphabetize?").

The 24 old titles cover A–Z except **Q** and **X**. The `QX=TH` sticky fills exactly those two
slots — it is not a generic substitution-cipher crib.

| Slot | Plate | Numeral | Old English plate title | Historical scientific name | Letter |
|---|---|---|---|---|---|
| A | 337 | VI | American Bittern | *Ardea minor* | M |
| B | 102 | III | Blue Jay | *Corvus cristatus* | R |
| C | 039 | VI | Crested Titmouse | *Parus bicolor* | B |
| D | 112 | IX | Downy Woodpecker | *Picus pubescens* | E |
| E | 246 | VIII | Eider Duck | *Fuligula mollissima* | A |
| F | 081 | XIV | Fish Hawk or Osprey | *Falco haliaetus* | S |
| G | 061 | II | Great Horned Owl | *Strix virginiana* | T |
| H | 083 | XI | House Wren | *Troglodytes aedon* | S |
| I | 074 | IX | Indigo Bird | *Fringilla cyanea* | A |
| J | 253 | XIV | Jager | *Lestris pomarina* | N |
| K | 225 | VI | Kildeer Plover | *Charadrius vociferus* | D |
| L | 424 fig. 6 | XVI | Lazuli Finch *(composite plate title)* | *Plectrophanes townsendi* *(figure 6)* | W |
| M | 184 | V | Mangrove Humming Bird | *Trochilus mango* | H |
| N | 275 | III | Noddy Tern | *Sterna stolida* | E |
| O | 042 | V | Orchard Oriole | *Icterus spurius* | R |
| P | 358 | IX | Pine Grosbeak | *Pyrrhula enucleator* | E |
| **Q** | *(sticky)* | — | `QX=TH` | — | **T** |
| R | 101 | II | Raven | *Corvus corax* | O |
| S | 235 | VII | Sooty Tern | *Sterna fuliginosa* | F |
| T | 029 | III | Towee Bunting | *Fringilla erythropthalma* | I |
| U | 245 | VIII | Uria brunnichii | *Uria brunnichii* | N |
| V | 076 | IV | Virginian Partridge | *Perdix virginiana* | D |
| W | 216 | I | Wood Ibiss | *Tantalus loculator* | T |
| **X** | *(sticky)* | — | `QX=TH` | — | **H** |
| Y | 329 | X | Yellow-breasted Rail | *Rallus noveboracensis* | E |
| Z | 162 | V | Zenaida Dove | *Columba zenaida* | M |

Reading A→Z:

```
M R B E A S T S A N D W H E R E T O F I N D T H E M
MRBEASTS AND WHERE TO FIND THEM        = (8,3,5,2,4,4) = 26 letters ✔
```

Strike `MR` (the pad's struck-through `MR`) and replace it with the nine-letter word the pad
asks for:

```
FANTASTIC BEASTS AND WHERE TO FIND THEM   →   red terminal = FANTASTIC (9) ✔
```

**Three source details that must be right or the string breaks:**

1. The cached concordance misspells plate 81's binomial as *Falco halliaetus*. The original
   plate reads **FALCO HALIAETUS**. Verified against the original plate image, cached as
   `work/audubon/plate81.jpg` and `plate81_caption.png` from
   `https://media.audubon.org/boa_illustration/plate-81-fish-hawk-or-osprey.jpg`. [OBS]
2. Plate 424 is a six-figure composite. It sorts under its **first** title (*Lazuli Finch* → slot
   L) but the extraction uses **figure 6** (*Brown Longspur*, *Plectrophanes townsendi*). Verified
   against the plate image `work/audubon/plate424.jpg` / `plate424_caption.png`, and against the
   concordance, whose six rows for plate 424 are in figure order with *Plectrophanes townsendi*
   sixth. [REPRO]
3. Plate 245 must **not** be modernised to *Thick-billed Murre*. Its old title is literally
   "Uria brunnichii", which is what puts it in slot U. [OBS]

Concordance source: `https://de.wikipedia.org/wiki/Liste_der_Vögel_aus_The_Birds_of_America`,
cached as `work/audubon/plate_concordance.html`; a plate-name index derived from the University
of Pittsburgh listing is cached as `work/audubon/havell_plates_pitt.json` (all 435 plates).

**Arithmetic consistency note.** 24 pink pairs + 2 sticky letters = 26 letters = the *corrected*
enumeration (8,3,5,2,4,4). The **uncorrected** (8,3,5,4,4) = 24 matched the 24 pink pairs, and
earlier research treated that as structural confirmation that the pink note alone was the phrase.
That coincidence is now explained away by the author's confirmed missing "2". This is a
superseded conclusion; see Section 12.

### 5.3 The XOR step [REPRO]

`XOR SUPERB OWLS` + `# # How many?` (= 14 pieces) + the CyberChef placeholder's exact case and
punctuation:

```
placeholder :  A a a a a A - a a A a # #
input       :  S u p e r B - o w L s 1 4
```

The mask matches exactly: capitals at positions 1, 6, 10; hyphen at 7; digits at 12–13. Then:

```
Input :  SuperB-owLs14
Key   :  %H6U=)Z7</#bq        (25 48 36 55 3D 29 5A 37 3C 2F 23 62 71)
XOR   :  v=F0OkwXKcPSE
```

The `YouTube link.. watch?` sticky supplies the wrapper:

```
https://www.youtube.com/watch?v=F0OkwXKcPSE
```

That is MrBeast's **"Hi Me In 10 Years"** — recorded 2015, scheduled and published
**2025-10-04**, 3:14, 68,050,776 views. Metadata and official uploaded English captions are
cached as `work/yt/owl14_gateway.info.json` and `owl14_gateway.en.vtt`. [OBS]

### 5.4 The blue sticky decode [REPRO]

The blue monitor sticky's letters, flattened:

```
LSWRTENNHTINHDOTA        (17 letters)
```

Read alternately from the left end and the right end: L, A, S, T, W, O, R, D, T, H, E, N, N, I, N, T, H

```
→  LAST WORD THEN NINTH        = (4,4,4,5) ✔
```

Equivalently the construction is a **two-row transposition with the lower row reversed**:
`plain[::2] + plain[1::2][::-1]` reproduces the sticky exactly. The displayed three-line layout
does **not** make it a standard three-rail fence, and no standard rail-fence configuration
produces it: 2,408 configurations were tested (rail counts 2–17, all phase offsets, normal and
reversed rail orders and reading directions, plus keyed six-rail orders using 251634 and its
inverse with every independent rail direction). **None matched.** `tools/test_blue_alternatives.py`.
[REPRO, negative]

That negative result matters: it removes the most obvious hypothesis that `251634` was the key
to this fence step. The known construction reproduces the sticky exactly and does **not** consume
`251634`.

### 5.5 Applying the instruction [REPRO]

The gateway video's official uploaded English captions contain 506 spoken words.

- Word 1–15: "Hi, me in ten years. I'm gonna schedule **upload** this video ten years in the…"
  → **ninth word = UPLOAD**
- Final cue: "So uh, yeah. Like I said, this is October **fourth**."
  → **last word = FOURTH**

"LAST WORD THEN NINTH" ⇒ **FOURTH UPLOAD** = the `(66)` node. ✔

**[OBS] worth a reviewer's attention:** the word FOURTH is the last word of "this is October
fourth" — a *date*, not an ordinal position. The video was itself a *scheduled* upload (its
ninth word is "upload" precisely because the speaker says "I'm gonna schedule upload this
video"). Both source words sit inside date/scheduling language. Whether "FOURTH UPLOAD" means
"the fourth upload" or something about "October 4th" has never been tested as a fork. One
community solver noted the same ambiguity in passing ("sticky ops on gateway captions — Oct 4th
+ 'upload'") without pursuing it. This is a live, untested fork. [SPEC]

---

## 6. The unsolved step, stated in full

### 6.1 What is left

```
(66) FOURTH UPLOAD   +   251634   →   (6) ??????
```

### 6.2 What "fourth upload" could mean, and what has been checked

Twelve videos have been examined. **Inspection coverage differs enormously between them and is
stated honestly below.** No entry in this table was inspected frame-by-frame with audio.

| # | Hypothesis | Video ID | Title | Actual coverage performed |
|---|---|---|---|---|
| 1 | MrBeast's fourth-oldest currently-public full video | `Y74b7WlcEpk` | *More birds IN MINECRAFT!!* (2013-01-12, 2:05) | **Deepest coverage.** Full video downloaded; 250 frames at 2 fps run through RapidOCR (`work/yt/mb4th_targeted_ocr.json`); contact sheet; six hotbar spawn labels visually confirmed and preserved as an evidence sheet; description followed to its linked mod video; public comments read; thumbnail refetched and inspected. **No frame-by-frame review, no audio listening.** |
| 2 | MrBeast 2, fourth upload (mixed feed) | `h-EL3eeSZeU` | *Unlimited Money Machine* (2020-08-24) | Metadata + captions only. |
| 3 | MrBeast 2, fourth-oldest full-video tab | `jaRfBM7ESfc` | *$1 vs $10,000 Commercial* (2024-03-09) | Metadata + captions only. |
| 4 | DoctorXOR, fourth-oldest | `2asPmHvlkWM` | *140 – Mirror Level 3 Walkthrough (No deaths)* (2017-06-24) | Video downloaded; 10-second-interval contact sheet visually reviewed (`work/yt/xor_fourth_sheet.jpg`); metadata, captions, comments, thumbnail. **No frame-by-frame, no audio.** |
| 5 | DoctorXOR, fourth-newest | `IU89_plbom0` | *Will This Be the Greatest Puzzle Game Ever? – Order of the Sinking Star (Demo)* (2026-08-15) | Metadata + captions only. |
| 6 | MrBeast, fourth-newest full video | `iYlODtkyw_I` | *Survive 30 Days Chained To A Stranger, Win $250,000* (2026-06-27) | Captions + description text checks only. |
| 7 | MrBeast 2, fourth-newest full video | `vyBK-sVBfqg` | *Last Person Standing Wins $5,000,000* (2026-03-01) | Captions + description text checks only. |
| 8 | MrBeast Gaming, fourth-oldest | `CSSsPVweLkc` | *Last to Survive Random Blocks wins $10,000* | Metadata + captions only. |
| 9 | Beast Reacts, fourth-oldest | `67MptG3oS-A` | *Super Satisfying Kinetic Sand DIY* | Metadata + captions only. **Mentions Harry Potter at ~7:35–7:50 — about a winged tennis ball and Quidditch, not Hedwig.** Do not upgrade this into evidence. |
| 10 | Beast Philanthropy, fourth-oldest | `nl79pan4h6U` | *Giving Away 50,000 Cookies!* | Metadata + captions only. |
| 11 | Beast Animations, fourth-oldest | `sKqFzjkiwF8` | *MrBeast Lab – Ep 3: Swarmbies* | Metadata + captions only. |
| 12 | YouTube's own fourth-ever upload (speculative) | `vCfgHo5_Fb4` | *Premature Baldness* (uploader "paul", 2005-04-29) | Captions + description only; the historical ranking itself came from a secondary source and was not verified. |

Also checked, each with metadata + 2-second contact sheet + captions, after realising the Shorts
tabs had never been enumerated separately:

| Rank | ID | Title | Uploaded |
|---|---|---|---|
| MrBeast, 4th-oldest Short | `se50viFJ0AQ` | *Would You Fly To Paris For A Baguette?* | 2022-12-08 |
| MrBeast, 4th-newest Short | `Df5Y-2ndQyU` | *Read My Book, You Could Win $1,000,000* | 2026-07-17 |
| MrBeast 2, 4th-oldest Short | `wdznN3-h_5Y` | *Launching a $40,000 Firework!* | 2020-09-11 |
| MrBeast 2, 4th-newest Short | `KDAlh2S4SfM` | *Can You Spot the Chocolate Object?* | 2026-08-10 |

Additional chained sources checked: `Z8nEEdXTaX0` (*Boxy item mod Minecraft. EPIC*, 2013-01-12, linked from
candidate #1's description) → an ordinary PlanetMinecraft mod page; `jP82d277Cc8` (*Harry Potter Mod In Minecraft! EPIC MUST SEE MOD!!!*,
2012-03-09, MrBeast's second-oldest surviving upload, about Quidditch).

**Rank verification [OBS].** The "fourth oldest" ranks in rows 1 and 2 were checked against the
cached upload listings. `work/yt/mrbeast_uploads.txt` (999 entries, newest first) ends
… *Most Epic minecraft skin EVER (Psy)* · **`Y74b7WlcEpk` More birds IN MINECRAFT!!** ·
`Z8nEEdXTaX0` Boxy item mod · `jP82d277Cc8` Harry Potter Mod · `2XVcLrB7B3Y` Worst Minecraft Saw
Trap Ever??? — so `Y74b7WlcEpk` is the fourth-oldest **currently public** upload.
`work/yt/mrbeast2_uploads.txt` (244 entries) likewise puts `h-EL3eeSZeU` fourth-oldest, behind
`RBB9GSMkLHc`, `xdmuHe_ZDIw` and — worth a reviewer's notice — MrBeast 2's very first upload,
**`fZDUxJ-7Y4A` *Solve This Riddle For $100,000 (Step 1)***. No clue connects that riddle series
to this puzzle; it is recorded because the coincidence of channel and genre is the kind of thing
a reviewer should either use or explicitly dismiss.

**Structural limitation that applies to this entire table [OBS]:** current *public* upload order
is not historical upload order. Deleted and private videos are unavailable, and "fourth newest"
changes every time a channel uploads. The fourth-newest rank as it stood at the puzzle's release
on 2026-09-02 was never captured. Channel snapshot: `work/yt/channel_fourths.tsv` (473 entries),
Shorts listing `work/yt/main_shorts_sep6.tsv` (198 + 200 entries), both captured 2026-09-05/06.

### 6.3 The strongest candidate destination, in detail

Candidate #1 (`Y74b7WlcEpk`, *More birds IN MINECRAFT!!*) is thematically the best fit: MrBeast's
fourth-oldest public upload, published 2013-01-12, and it is **about birds** — matching BIRDS OF
AMERICA and the whole owl theme.

Its Minecraft hotbar holds **exactly six** bird spawn eggs, demonstrated in
`dossier_images/09_spawn_labels.jpg`, each shown with its on-screen label:

| Hotbar slot | Literal on-screen label | Inspected frame time |
|---|---|---|
| 1 | Spawn **Peacock** | 20.0 s |
| 2 | Spawn **Bluebird** | 26.0 s |
| 3 | Spawn **Peahen** | 30.5 s |
| 4 | Spawn **Flamingo** | 33.0 s |
| 5 | Spawn **Roadrunner** | 39.0 s |
| 6 | Spawn **White Peacock** | 48.5 s |

(Times identify inspected frames, not exact first-spawn moments. An earlier note read slot 3 as
"Pelican"; **Peahen** is what is actually on screen. [OBS])

Six labelled items and a six-digit permutation is an attractive fit. It does not work:

- Indexing the six names with 2,5,1,6,3,4 gives **EBPNAT**. [REPRO]
- 120 further literal-label models (with/without the "Spawn" prefix; hotbar / reverse /
  alphabetical / key-reading / key-destination orders; key / inverse-key / position / first /
  fourth / ninth character indexes; counting from either end) produced **no six-letter
  dictionary word at all**. [REPRO, negative — `tools/audit_blue_251634.py`]
- The nearby pond-side board at ~93.5 s is a 3×5 grid of apparently **empty** item frames, not a
  hidden six-symbol message. The inventory screens at ~54 s and ~95 s hold nine additional
  ordinary items alongside the six spawn eggs, so they are not a second clean group of six. [OBS]
- The Exotic Birds mod's own "Book of Birds" reportedly lists scientific names, which would give
  a second name set. But the retrieved mod documentation describes 2016 and 2020 releases, not
  the 2013 build in the video, and **no book is visibly opened in any inspected frame**. No
  scientific-name list was therefore treated as valid input. This is *unproved*, not eliminated. [OBS]

### 6.4 Direct tests on `FOURTH UPLOAD` itself

Because the flowchart says `(66) → (6)`, the reduction might act on the twelve letters directly
rather than on anything at a destination video. Twenty-eight single-source models were run
(instruction phrase, each word, video title, title's last word, both description lines; key and
inverse-key indexes; from either end). **No dictionary match.** [REPRO, negative]

Representative outputs: `UPLOAD` indexed by 251634 → `PAUDLO`; the title indexed by 251634 →
`OBMIRE`.

For this dossier a further bounded check was run on combination models not previously covered —
alternating letters between the two words, concatenation `FOURTHUPLOAD` and `UPLOADFOURTH` with
key and inverse-key indexes and a +6 offset, and interleave-then-index:

```
FOURTH[key]   OTFHUR    UPLOAD[key]   PAUDLO    alt_A_B_key   OAFDUO
FOURTH[inv]   UFTHOR    UPLOAD[inv]   LUADPO    alt_B_A_key   PTUHLR
concat_key    OTFHUR    concat_key+6  PAUDLO    alt_A_B_inv   UUTDOO
concat_inv    UFTHOR    concat_inv+6  LUADPO    alt_B_A_inv   LFAHPR
interleave_key UUFLOP   interleave_key2 PAUDLO
```

**No dictionary word among any of them.** [REPRO, negative, run 2026-09-07]

### 6.5 The 15-asterisk observation

The mock entry form in the ending montage types out an answer that is masked with asterisks.

- **15 asterisks, not 16.** `dossier_images/08_mask_15_asterisks.jpg` is the numbered crop. [OBS]
- Sampled at 10 fps from 1045 s: frames 016–020 (≈17:26.5–17:26.9) each show 15 star-shaped
  connected components at brightness thresholds 170, 185 and 200, agreeing with manual counting.
- A second extraction preserved **every native source frame** across the final typing and the
  cut, at 30000/1001 fps: 13 consecutive frames show 15 stars, then the view cuts to SUBMIT.
  No briefly-displayed 16th star exists in that window.
- Reproduce: `python3 tools/count_submission_mask.py` → `work/video_audit/mask_counts.json`.
- The red required-field marker beside the question is *not* part of the typed answer; miscounting
  it is what produced the earlier "16" figure.

**What this does and does not support.** `FANTASTICHEDWIG` (no space) is 15 characters;
`FANTASTIC HEDWIG` is 16. So the animation is *consistent* with a no-space, 15-character answer.
It is an edited demonstration in a video, not the server's validation rule, and it does not
establish the answer, its length, or the accepted format. [OBS + explicit limitation]

---

## 7. Complete register of tests attempted

Grouped by target. Every row is a **negative** result unless stated. "Limitation" states what the
test does *not* rule out.

### 7.1 Broadcast-layer sweeps (video / audio / captions)

| Test | Method | Result | Limitation |
|---|---|---|---|
| Container & metadata | mp4 atoms, mp3 ID3, trailing bytes | Clean | The 1080p file is a re-encode; original YouTube metadata is gone regardless |
| Full spectrograms | `showspectrumpic` log + linear + L−R difference | No hidden image, no obvious Morse/DTMF bands | Audio is lowpassed ~17 kHz (AAC) |
| Whole-track tone scan | 1024-pt FFT, 600–1700 Hz, top-4-bin energy ratio | Nothing but one 0.1 s blip at 3:58 | Only detects steady pure tones |
| Reversed audio | **NOT DONE** for 17:36–17:47 | — | **Open item.** Listed as "cheap, unchecked" since 2026-09-03 and never completed |
| Outro song ID | Community identification | MrBeast's old-school outro song (nostalgia callback) | Community attribution, not verified |
| Single-frame inserts | 64×36 grayscale over all 31,981 frames; then 160×90 in a 4×4 region grid | Only stylistic flickers/wipes at 0:59, 1:07, 1:23, 2:41, 3:24, 5:07, 5:41, 6:20, 11:44, 12:07, 12:12, 16:10.0, 17:12.0, 17:17.9 | Detects frames differing from both neighbours; a 2-frame insert would score lower |
| Solid-colour frames (base-3 colour cards) | 32×18 RGB, low spatial std | Only white flashes and page backgrounds | — |
| OCR, 1080p | RapidOCR every second, 7,066 distinct tokens (`work/ocr_frames.json`) | No `XXXXXX-XXXX99` token; no "674" | OCR misses handwriting, angled and small text entirely |
| OCR, 4K tiled | 267 frames × 12 tiles every 4 s (`work/ocr4k_seq.json`) | Same | **4-second sampling; ~3 of every 4 seconds unexamined** |
| OCR, targeted 4K | 1 fps of intro laptop screens; 3 fps of ending TV screen | Nothing | — |
| Captions, uploaded EN | 503 unique lines; hyphens, zero-width spaces, speaker colours analysed | All structural (7 ZWSPs per first-line cue, 6 per second) | — |
| Captions, uploaded vs auto | Word-level diff | No inserted words | — |
| Captions, FR/ES/DE/JA | Read | Normal translations | — |
| QR code at 17:32 | OpenCV | Decodes to exactly the sweepstakes URL | — |
| Thumbnail | maxres + two A/B variants | Designed "ACCESS DENIED" board: 17 fake FAILED login dates, `USER ID 127-666-F733` (12 chars, not 13), corkboard stickies, an undecodable QR | A/B-tested thumbnails are unreliable puzzle carriers; the corkboard QR is too blurry for WeChatQRCode or Aruco |
| Digit "rain" shot 17:09 | 34×32 px cell grid, 36×45 cells, cross-frame agreement | **Closed.** Glyphs re-roll randomly each frame (78 % → 36 % → 15 % agreement over 1, 2, 5 frames; no shift). Glyph set `= 4 7 3 2 5 6 9` tracks underlying brightness. Aesthetic effect | — |
| TV static at 17:00 | Mean/std over 73 frames | Nothing | — |
| Bouncing cookie 17:42–17:47 | Centroid tracking | Plain DVD-logo bounce; final frame is a stock cookie PNG with its transparency checkerboard visible | — |
| "INSTRUCTIONS" montage 5:16–5:24 | 10 fps distinct-frame extraction | All 13 cards are PG1–PG13 from the answer-key PDF; no extra card | — |
| ECC-aligned frame stacking | `cv2.findTransformECC` affine over 35–45 frames | Made wall stickies legible; desk note and monitor sticky still too small at 1080p | Superseded by the 4K pull |
| Ending props at 4K | Targeted crops | Box tape blank; TV bezel "zenith / COLOR TV-VCR COMBINATION", no model number; rotary phone has no number card; vault tablet shows "4:51 PM Sun Mar 8" | — |
| Comments | Top 300 + newest 1500 scraped | Only useful signal: the pinned TinyURL, and viewers pointing at the desk paper, the phone and "674" | — |
| Sweepstakes site | Source, cookies, headers, JS bundles | No hidden fields, no comments, no hints | — |

### 7.2 Cipher and wordplay tests

| Test | Result | File |
|---|---|---|
| Blue sticky as anagram | `ADEHHILNNNORSTTTW` is an **exact** anagram of LASTWORDTHENNINTH — but **not unique**: 3,815 (4,4,4,5) multiset solutions, 2,034 using only common words, 134 containing two or more instruction/ordinal words (LAST THEN WORD NINTH, HINT THEN WORD SLANT…). The alternating-ends *mechanical* decode (§5.4) is what makes it a proof rather than a guess. | — |
| Blue sticky as keyed columnar transposition with 251634 | No match, both conventions, both directions | — |
| Blue sticky as rail fence | 2,408 configurations tested, none matched | `tools/test_blue_alternatives.py` |
| Yellow sticky `BOOKSWOLDNAMES` as a (5,2,7) scramble | 48 anagrams, all nonsense. It is plain text, an ordering hint | — |
| "Last word then ninth" applied to the host video's transcript, title, description, pinned comment | "video"/"Bowl", "Puzzle!" — nothing | — |
| XOR gate on every structured string visible in the video (vault codes, tablet text, IDs, prop numbers, stickies, brand names, dates, hashtags) | All junk | `tools/xor_check.py` |
| XOR gate on derived phrase strings (XORSUPERBOWLS, BirdsOfAmerica, FourthUpload, LastWordThenNinth, SuperBowl60…) | All junk — the recipe is a step *inside* the blue chain, not a final-answer check | `tools/xor_check.py` |
| `SuperB-owLs` + all 100 two-digit endings | Only `14` yields a valid YouTube ID | — |
| Pink numbers as MrBeast upload indices (999 uploads, oldest-first) | Gibberish | — |
| Owl-plate ⊕ Super-Bowl-number arithmetic | Only plates 46 and 61 can yield letters; not a bitwise operation in that form | — |
| Audubon extraction with modern names, spaces kept/removed, sorted by plate / modern / Audubon name | No readable sentence (best: `CUODIODS R.N ERTA. BREL DWLI`) — historical names + old-title alphabetisation is the only clean reading | `tools/solve_desk.py` prints all 12 variants |
| 251634 as alphabetical letter ranks | Fits BRAZIL, but also CHANCE, FRESNO, BRAZEN — underdetermined | — |
| HEDWIG anagram search | No ordinary single-word anagram in the installed American/British dictionaries | — |
| Six-channel fourth-upload indexing | Title initials, last/fourth title-word initials, first/ninth/last spoken-word initials, indexed title letters; direct and inverse 251634 | No extraction | `tools/test_blue_alternatives.py`, `work/yt/blue_alternative_results.json` |
| Caption-text HEDWIG search across seven videos | Six-word windows, first/final words of six cues, direct/inverse 251634 ordering, one- and zero-based char indexes — **81,781 tests**, 0 matches | `work/yt/blue_key_text_tests.json` |
| 148 literal-label / single-source 251634 models | No six-letter dictionary match | `tools/audit_blue_251634.py`, `work/yt/blue_251634_audit/results.json` |
| 16 FOURTH/UPLOAD combination models *(new, 2026-09-07)* | No dictionary word (§6.4) | This dossier |

**Cumulative honesty statement.** These are bounded model families over a small number of
sources. They do not constitute proof that any of these videos lacks a clue, and they say
nothing about visual, audio, or on-screen-text extractions that were never modelled.

---

## 8. Reproducing everything

Run from the repository root. Requires Python 3.12 with `lxml`, `opencv-python`, `Pillow`
(installed with `--break-system-packages` in this environment).

```sh
python3 tools/solve_desk.py            # red A-Z, XOR link, blue sticky, gateway captions
python3 tools/check_community_hash.py  # SHA-256 comparison against the public commitment
python3 tools/count_submission_mask.py # 15-asterisk count, three thresholds, native frames
python3 tools/audit_blue_251634.py     # 148 bounded 251634 models + evidence sheet
python3 tools/test_blue_alternatives.py# rail-fence exhaustion + six-channel tests
python3 tools/xor_check.py CANDIDATE   # XOR any 13-char string against the key
python3 tools/verify_dossier.py        # re-verify every table in THIS document
```

`tools/verify_dossier.py` parses this dossier's own markdown tables and re-checks them against
the cached source data: the 14 owl rows against their scientific names, all 26 Audubon rows
against the concordance and the pink note's numerals, the four enumerations, the sticky decode,
the placeholder mask, the XOR, the SHA-256, and the four test-count claims. It exits non-zero on
any mismatch. Last run 2026-09-07: **0 failures.**

Verified output of `tools/solve_desk.py` on 2026-09-07:

```
XOR: SuperB-owLs14 -> https://www.youtube.com/watch?v=F0OkwXKcPSE
Red A-Z with QX=TH: MRBEASTSANDWHERETOFINDTHEM
Red wordplay: replace MR with FANTASTIC (9 letters)
Blue sticky: LASTWORDTHENNINTH
Gateway captions: last word FOURTH ; ninth word UPLOAD
Blue terminal: NOT independently solved; 251634 remains unused
```

---

## 9. Unresolved props, unreadable details, untested hypotheses

### 9.1 Props with no explanation

| Prop | What is known | Why it is still open |
|---|---|---|
| **`251634` sticky** | Six uninterrupted digits, blue sticky, blue ink, therefore a blue-chain clue | **The gap.** No demonstrated role in any step |
| **Silhouette sheet** beside the blue pad | At least five winged/flight-like shapes on a white sheet, partly covered by other papers in every frame | Full contents, symbol count, orientation and relevance unknown. Compared visually against the old hunt's PG6 birds-on-a-wire alphabet (PDF page 35), "Birds of a Feather", the lowercase Bird Silhouettes font, "Birds Wingspans", and two flight-identification charts — **no exact match established.** Do **not** assume it has six symbols and do **not** assign species to make a target word |
| **Printed sheet under the pink note** | Carries a small printed letter/symbol table | Illegible at 4K in every available frame |
| **Wall boxes 6-7-4** and badges 2-1-4 | Stencilled circles on the brick wall | No role found. `+674` is Nauru's dialling code — a location-style answer would fit the old hunt's pattern, but nothing connects it to either chain |
| **Cardboard box handwriting** | Fragment appears to read `JULY` with a lower word starting `JU`; a fuller collage read gives `July 1st 1988 – June 30 89` | Partly hidden by the black case. Do not infer a date instruction |
| **Thumbnail corkboard QR** | Present but too blurry to decode | Thumbnail is A/B-tested, so it is an unreliable carrier anyway |
| **`081 XIV Seahawks?`** | Explained: plate 81 is the Fish Hawk / Osprey and is one of the 24 pink pairs | Resolved — but note the joke assumes the solver notices "sea hawk", so the sticky is a hint, not data |

### 9.2 Coverage genuinely not achieved

Stated so a reviewer does not over-read the negative results:

- **No frame-by-frame visual review of the 17:47 host video at native resolution with a human
  eye.** OCR at 1 fps (1080p) and every 4 s (4K) is the actual coverage.
- **No end-to-end 1× viewing with fresh eyes.** This has been on the plan since 2026-09-03 and
  was never completed.
- **No reversed-audio check of the outro (17:36–17:47).**
- **No frame-by-frame or audio review of any candidate destination video.** Contact sheets sample
  every 2 or 10 seconds.
- **No physical reconstruction of the jigsaw from tabs and notches.** The piece order in §5.1 is
  inferred from its output.
- **No real-time community survey.** Reddit JSON/RSS fetches for the newest thread (`1w7yi43`)
  returned HTTP 403 on 2026-09-06; the files `work/yt/reddit_latest_puzzle_sep6.{json,rss}`
  contain **error responses**, not data. Later community reading came from browser text.

### 9.3 Untested hypotheses worth a reviewer's attention

All [SPEC].

1. **"October fourth" fork.** As noted in §5.5, both extracted words sit inside date/scheduling
   language. "FOURTH UPLOAD" may be a date pointer (an upload on the 4th; an upload on October 4;
   the fourth upload *after* the gateway video) rather than "the fourth-ever upload". Never
   tested as a fork.
2. **`251634` as a destination-order permutation rather than a reading order.** The distinction
   has been analysed (§10.3) but no clue has been found that disambiguates which convention the
   author intends. If a reviewer can find a convention-fixing clue elsewhere in the set, it
   halves the search space.
3. **`251634` acting on the six *jigsaw-chain positions*** rather than on anything at a
   destination. Never tested — but note there are 14 pieces, not 6.
4. **`251634` acting on the six letters of one of the two `(66)` words in a way that also
   consumes the other.** §6.4 tested 16 such models; the family is larger.
5. **The Exotic Birds mod's in-game "Book of Birds" scientific names.** If the 2013 build's book
   listed Latin names for the six hotbar birds, that would exactly rhyme with the jigsaw's own
   "Roman numbers for Roman words" mechanic. Blocked because no 2013-era listing was located and
   no book is opened on screen. **This is the single most promising unexplored source** and it
   fails only on evidence availability, not on logic.
6. **The mod video's own visual content beyond the hotbar** — signs, chat text, world features —
   at frame rates finer than 2 fps.

---

## 10. Community claims, separated from verified evidence

Everything in this section is [CLAIM] unless marked otherwise. It is included because it is
*data about what other solvers believe*, not because it is evidence.

### 10.1 What the community got right, and how we know

| Community claim | Our independent status |
|---|---|
| `(527)` = BIRDS OF AMERICA | **Independently confirmed** — the 14 red numerals spell it from the owl names |
| `(364)` = XOR SUPERB OWLS | **Independently confirmed** — the 13 blue numerals spell it |
| `(4445)` = LAST WORD THEN NINTH | **Independently confirmed** — by mechanical decode, not by anagram |
| Pink numbers = Audubon plates | **Independently confirmed** — the A–Z extraction reads exactly |
| `(66)` = FOURTH UPLOAD | **Independently confirmed** — from the gateway video's official captions |
| Red terminal = **BEASTSAND** (u/gg4999, u/HoldingAdvisory) | **Contradicted.** The exact extraction gives MRBEASTSANDWHERETOFINDTHEM and the struck `MR` makes the terminal FANTASTIC |
| Blue terminal = **STUNTS** (u/gg4999) | Unsupported; no mechanism given |
| "The answer is close to BEASTSANDUPLOAD" (u/HoldingAdvisory) | Rejected by another community member in the same thread; no mechanism given |
| "It's a rail fence cipher" (u/PartyAd2016) | **Partly wrong but useful.** The sticky is *not* a rail fence (2,408 configurations tested); it is a reversed two-row transposition. The community's *output* was right |
| The blue sticky subtitle reads "bird **Fence**" | Better than our own 4K read; adopted as the likely reading with uncertainty flagged |
| Assembled jigsaw reads "SUBSCRIBE TO MRB" | **Contradicted** by the letters actually on the pieces |
| Pink note is a book cipher into MrBeast & Patterson's novel *The Most Dangerous Games* | **Superseded.** It is an Audubon plate index. The novel theory also conflicted with "no purchase necessary" |
| Roman numerals are video timestamps; 26 audio clips; a phone number (u/tehKJM) | Not supported by anything; incoherent with the working chains |
| "674 = Nauru" | Numerically true, no role found |
| "Is the answer related to something that flies, 6 characters?" | An unsourced question, repeated widely as if it were a hint |

### 10.2 The FANTASTIC HEDWIG claim, precisely stated

On 2026-09-05 Reddit user **CiviledXI** posted, in *"6 and 9 letter words solved for"*
(`https://www.reddit.com/r/MrBeast/comments/1w7qx8b/6_and_9_letter_words_solved_for/`):

> "I have figured out both the 9 letter and the 6 letter word. Below is a sha256 hash produced
> from the two words (all caps separated by a space):
> `b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22`
> … I'm unsure if the format of my final answer is correct, but I've utilized and accounted for
> all of the known clues to get to this point. Will post updates if I hear back. As far as I
> know, there is ~10 people that have solved up to the last 2 steps for puzzle 2. Puzzle 1 has
> been mostly solved on this subreddit, but there is still steps to get to the final word that
> nobody has publicly posted."

Locally computed, and reproducible with `python3 tools/check_community_hash.py`:

```
SHA-256("FANTASTIC HEDWIG") = b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22   MATCH
SHA-256("FANTASTICHEDWIG")  = e13e6e2604c5fa6707e1cda6969388a89e32c747d8f954ee0ba6d49c2d922c42   no
SHA-256("HEDWIG FANTASTIC") = (does not match)
SHA-256("FANTASTIC UPLOAD") = (does not match)
SHA-256("FANTASTIC STUNTS") = (does not match)
```

**What this establishes:** that this dossier's candidate phrase, in that exact casing and
spacing, is the same string CiviledXI committed to. That is a real, checkable fact. [OBS]

**What it does not establish:** that the phrase is correct; that CiviledXI derived it
independently rather than from the same public speculation; that the Sponsor accepts that
format; or that anyone — including CiviledXI — has ever produced the blue extraction.
CiviledXI's own post says they are unsure of the format and that nobody has publicly posted the
final steps.

### 10.3 Where "HEDWIG" actually came from, and its provenance problem

The word entered this research from a Reddit comment attributed to **u/psolidgold**:
*"Fantastic Puzzle, u/DoctorXOR. I would be your Hedwig any day."* — a pun, in thread
`1w62u79`, read in a browser on 2026-09-05.

**Audit finding [OBS]:** that thread's comments were **never archived locally**. `work/reddit/`
contains 13 thread dumps; `1w62u79` is not among them, and a full-text search of every cached
file finds "Hedwig" only in a later post titled *"FANTASTIC HEDWIG?"* by u/Street_Pollution7646
and in a search-results feed. The originating pun is therefore **not independently verifiable
from this repository.** A reviewer should treat the word's provenance as: *a pun in a comment,
then a hash commitment by a different user, then wide repetition.*

**Diagnostic, explicitly not a solution [REPRO]:** if `251634` is a direct reading order applied
to six sources, then producing HEDWIG requires the sources to yield `D H I G E W` in slot order;
under the inverse (destination) convention it requires `E I H G D W`. Neither string has been
located anywhere. Against the six literal Minecraft bird names, HEDWIG is **impossible** under
the direct convention (Bluebird has no H, Peacock no D, Peahen no I). Under the destination
convention it can be *forced* by choosing character positions 4,2,4,1,6,7 — but **no clue
supplies those positions**, which is exactly why it is a diagnostic and not an answer.

### 10.4 Other community context

- Two users claimed on 2026-09-03 evening to have "finished" ("we were done around 11:30 EST").
  Colin was streaming the same night and said no winner had been announced.
- u/DoctorXOR replied "😆" to a post titled *"I'm close to solving it Colin…"*. That is not a
  confirmation of anything.
- A reply in thread `1w7yi43` states the fourth-upload step "did not involve transcripts". It
  supplies no mechanism. It is an unverified solver lead, not an author hint.
- CiviledXI separately described a 7:46 / Golden Gate Bridge / Golden Bird route as a **wrong**
  interpretation. Do not resurrect it.
- Many users report the verification email never arriving — relevant to interpreting submission
  status.
- Reposted write-ups (the widely circulated "BEASTSANDSTUNTS" one) are **not** independent
  corroboration; they share a source.

---

## 11. The author: prior work and stated preferences

This section exists to inform priors. **Stylistic similarity is not proof of mechanism.**

### 11.1 On-record statements about this puzzle [AUTHOR]

From Colin's Twitch VOD *"Just a normal Thursday"* (`twitch.tv/videos/2864667604`, started
2026-09-03 21:33 ET). Whisper transcript at `work/twitch/thursday.txt`; timestamps are transcript
seconds.

| Time | Quote (lightly cleaned) |
|---|---|
| ~1449 s | "the current 10k outstanding Mr. Beast puzzle — I made it by myself." |
| ~1468 s | "it is not as big as the Super Bowl puzzle." |
| ~2490 s | "I did make the 10k puzzle myself… I don't want to say too much until it's been officially over with." |
| ~2534 s | "You'd be surprised how many parts of the puzzle were… I want to say accidents, but I have a bad habit of just… stumbling on to the things… Sometimes it doesn't feel like I made the puzzle." |
| ~7821 s | "until someone solves it and Team Beast announces a winner" |
| **~7878–7980 s** | **"the initial question is: have you solved the jigsaw puzzle? … In Mr. Beast's video, the first thing you should do is look for a jigsaw puzzle."** |
| ~7994 s | "and that's as far as I'm going to say right now. It's just to get you started." |
| ~8005 s | "Plenty of people have posted a lot of hints online already that are far beyond that." |

**Important caveat.** In the middle of the jigsaw hint he also mutters "Is there another entry
point, one two three? There's three of them" — but he was simultaneously playing *The Witness*,
and the surrounding lines ("there's a purple", "these little tripods", "that's not fantastic",
"oh, it's gotta be contained") are unmistakably game talk. **Do not read "three entry points"
as a puzzle statement.** [OBS]

Likewise, an earlier note claimed Colin confirmed the $10k puzzle reuses "old hat" mechanics.
Re-reading the passage (~1491–1522 s) shows he was making a general remark about disliking AI
guessing puzzle mechanics, conditional on such mechanics being old. **That was an
overstatement and has been corrected.** [OBS]

### 11.2 A puzzle he definitely authored [OBS]

*Which Prexcyt Dragon Are You?*, Cryptex Hunt 2019 magazine, printed pages 24–25, credited
"Created by DoctorXor".

- Sources: `https://cryptexhunt.com/2019/mag.pdf` and the official solution guide
  `https://cryptexhunt.com/2019/CH2019%20Solution%20Guide.pdf` (page 19). The magazine PDF's
  password, `LOCKBOX`, is published on page 3 of the solution guide. Both cached as
  `work/colin/cryptex2019_mag.pdf` and `cryptex2019_solutions.pdf` with `.txt` extractions.
- Mechanism: a questionnaire conceals five groups of references. The solver identifies each
  group's common theme and its associated number, indexes the indicated words to produce
  **MOTTO**, then uses a *separately clued* Pythagorean step to reach the final answer
  **ALL IS NUMBER**.

**What this supports:** a design habit of (a) grouping references, (b) numeric letter-indexing,
(c) a final step that is clued separately from the extraction. That is a reason to keep looking
for a *concrete clued role* for `251634` rather than for a clever transformation. **What it does
not support:** any particular mechanism, any particular destination, or the existence of an extra
stage beyond the two chains. [SPEC beyond the mechanism description]

### 11.3 Stated preferences [OBS]

From his Salesforce interview (2026-05-19,
`https://www.salesforce.com/news/stories/how-colin-sanders-solved-mr-beast-puzzle/`): he
describes liking minimalist visual puzzles with sound internal logic, and disliking fragile
associations and excessive red herrings. He describes keeping a complete clue inventory and
returning to a previously photographed clue when the old hunt stalled.

Two cautions the research team recorded and a reviewer should keep:

- That interview credits the $1M hunt to **Lone Shark Games**. The 84-page answer key documents
  puzzles Colin *solved*, not puzzles he wrote. Do not mine it for his authorial style.
- Puzzles he *praises* (Jack Lance, mezzacotta) are other authors' work.

### 11.4 Other attributions checked, with limits [OBS]

- Rankk credits him with *Dice Where?*, *Arckeyologist*, *Master Arckeyologist*
  (`rankk.org/contributors.py`, `rankk.org/user/DoctorXOR`). Only titles and credits were
  retrieved, **not mechanisms**. Titles alone do not justify a dice, archive, or keyboard reading.
- The 2019 Cryptex site lists him as a contributor; the 2020 site as a tester. The 2025 site's
  embedded people data contains his biography, but its active Designers list does not include him.
  Do not infer 2025 authorship from a search snippet.
- His GitHub profile shows zero public repositories. Paradox Puzzlehunt's about page does not list
  him as an author; his videos there are solve-throughs.

---

## 12. Corrections table — what is superseded

Historical notes in `FINDINGS.md` contain conclusions that later work overturned. This table is
the authoritative reconciliation. **Do not reason from the superseded column.**

| # | Superseded conclusion | Where it appears | Correct position | Basis |
|---|---|---|---|---|
| 1 | "The CyberChef placeholder's case pattern is NOT literal; no readable plaintext can produce it" | FINDINGS §1, §5 | **Wrong.** The mask *is* literal. `SuperB-owLs14` matches it exactly and XORs to `v=F0OkwXKcPSE`, a valid YouTube ID | The original test rejected the output because it was not English prose. It is a URL suffix; the neighbouring `YouTube link.. watch?` sticky supplies that context |
| 2 | "Somewhere in the video is a 13-character string; find it" | FINDINGS §1 | **Wrong framing.** The 13-character string is *constructed* from the jigsaw, not printed anywhere. Every OCR sweep was searching for something that does not exist | Superseded by the solved blue chain |
| 3 | The submission animation shows **16** asterisks | early FINDINGS | **15.** Re-counted at three thresholds across 5 sampled and 13 consecutive native frames | `tools/count_submission_mask.py`, `VIDEO_AUDIT.md` |
| 4 | Red terminal is **BEASTSAND** (community) | FINDINGS §17, candidates.md Tier 8 | **FANTASTIC.** The exact extraction yields MRBEASTSANDWHERETOFINDTHEM; MR is struck and replaced | `tools/solve_desk.py` |
| 5 | The African grass owl piece shows VIII, breaking XORSUPERBOWLS — treat as an unresolved discrepancy | FINDINGS §16b, §20 | **Production error.** The author confirms an extra blue I; intended VII → P | Author, 2026-09-06 |
| 6 | The red pad's `(8,3,5,4,4)` = 24 letters matches the 24 pink pairs — "structural confirmation" | FINDINGS §18 | **Coincidence, now explained.** The author confirms a missing 2: intended (8,3,5,2,4,4) = 26 = 24 plate letters **+ 2 from the QX=TH sticky** | Author, 2026-09-06 |
| 7 | The `(8,3,5,4,4)` node is a further extraction *instruction* to be discovered | HANDOFF §3, §7 | **No.** It is the enumeration of the completed title | §5.2 |
| 8 | `QX=TH` is a generic cryptogram crib for the pink note | FINDINGS §9b, §9e | **No.** It supplies the two alphabet slots (Q, X) that no Audubon plate title begins with | §5.2 |
| 9 | The pink note is a book cipher into a Patterson novel / Goosebumps / the Bible | FINDINGS §15, §15b | **No.** Audubon plate index | §5.2 |
| 10 | The jigsaw pieces are ordered by domino-matching numerals (blue of one = red of next); "a unique chain of 8 is far too clean to be chance" | FINDINGS §16 | **Withdrawn in §16c.** With corrected colours the rule gives two competing chains and duplicate values. Physical tabs/notches order the pieces | FINDINGS §16b–16c |
| 11 | The `(364)→(62)→(6)` note in the ending scene is a separate/extra flowchart | community, FINDINGS §3 | Same blue pad at a worse angle; the "62" is `(66)` | §4.1 |
| 12 | Blue sticky subtitle reads "bird **food**" | FINDINGS §8, §9e, HANDOFF §3 | Likely "bird **Fence**" per the community collage; our own crop is not decisive. **Flagged uncertain**; does not affect the decode | §4.3 |
| 13 | The blue sticky is a rail-fence cipher | community | Two-row transposition with the lower row reversed. 2,408 rail-fence configurations fail | §5.4 |
| 14 | Slot 3 of the Minecraft hotbar is "Pelican" | early notes | **Peahen**, visible at ~30.5 s | `dossier_images/09_spawn_labels.jpg` |
| 15 | Colin confirmed on stream that this puzzle reuses an old mechanic | FINDINGS §14 | **Overstated.** The remark was a general, conditional comment about AI and puzzle mechanics | FINDINGS §27 |
| 16 | "There are three entry points" is a puzzle statement by the author | FINDINGS §14 | **No.** He was narrating *The Witness* while speaking | §11.1 |
| 17 | Files `work/yt/reddit_latest_puzzle_sep6.{json,rss}` are community data dumps | filenames | They contain **HTTP 403 error responses.** Do not parse them as data | FINDINGS §25 |
| 18 | `puzzle.pdf` might contain the new props | FINDINGS §9f | All 84 pages checked. It contains none of them | FINDINGS §9f–9g |

---

## 13. Prioritised questions for the independent reviewer

Ordered by expected value. **P1** items could plausibly close the puzzle; **P3** items are
housekeeping.

### P1 — the missing step

1. **What rule consumes `251634` and reduces `(66)` to `(6)`?** State the clue that licenses your
   rule *before* you state its output. If your rule needs a source with six items, name where in
   the video the solver is told to find those six items.
2. **Is "FOURTH UPLOAD" an ordinal or a date?** The gateway video's last words are "this is
   October fourth" and its ninth word comes from "I'm gonna schedule upload this video". Argue
   for one reading and say what it points at.
3. **Whose fourth upload?** No clue we have found names a channel. The gateway video is on the
   main MrBeast channel; the host video is on MrBeast 2; six channels are linked in the
   description. Which does the puzzle's own logic select, and why?
4. **Is the (6,6) → (6) arrow a *selection* or a *transformation*?** The red chain's final arrow
   is a substitution licensed by a drawn strike-through. The blue pad has **no strike-through
   anywhere**. Does that asymmetry tell us the blue reduction is a different kind of operation?

### P1 — attacking what we believe

5. **Break the jigsaw ordering.** §5.1's row order is confirmed only by its output. Reconstruct
   the order from the visible tabs and notches in `dossier_images/07_jigsaw_pieces.jpg`,
   `10_piece_atlas.jpg` and `01_desk_prop_collage.jpg`. If the physical order differs from ours,
   the blue *source* phrase may be wrong and everything downstream is suspect.
6. **Attack the Audubon table.** Three source choices had to be made (plate 81's spelling, plate
   424's split sort/extract, plate 245's un-modernised title). Each was chosen because it made
   the sentence read. Is any of them independently justified, or are we curve-fitting?
7. **Is FANTASTIC really the terminal?** The struck `MR` licenses replacing MR with a 9-letter
   word to complete *Fantastic Beasts and Where to Find Them*. Is there a competing 9-letter
   reading of the same wordplay?

### P2 — sources we could not reach

8. **The Exotic Birds mod's 2013-era "Book of Birds".** If its scientific names for Peacock,
   Bluebird, Peahen, Flamingo, Roadrunner and White Peacock can be established for the build in
   the 2013 video, that is the highest-value untested input in this whole dossier — it would
   rhyme exactly with the jigsaw's "Roman numbers for Roman words". Where would you look?
9. **The silhouette sheet.** Five-plus winged shapes on a partly covered sheet beside the blue
   pad. Identify the chart. Resist the temptation to make it have six symbols.
10. **The printed table under the pink note.** Any route to a legible source (BTS stills, a
    different camera angle, a higher-quality community capture)?

### P2 — coverage gaps we know about

11. Which of these is worth the time first: a 1× human viewing of the host video, reversed audio
    on the outro, or dense frame extraction of the Minecraft video?
12. Is there a systematic way to enumerate "fourth upload" candidates that accounts for
    **historical** rather than current public upload order?

### P3 — status and format

13. Given the rules quoted in §2.4, is there *any* observation that would distinguish "the
    submitted answer was wrong" from "the answer was right and verification is in progress"?
    We believe there is not; confirm or refute.
14. If a solver did want to hedge on format, does the 15-asterisk animation justify a no-space
    variant, or is reading an edited demonstration as a spec error in itself?

---

## 14. File inventory

### 14.1 Deliverables produced by this pass

| File | Size | Contents |
|---|---|---|
| `LLM_REVIEW_PACKET.md` | this file | Self-contained master dossier |
| `LLM_REVIEW_PACKET.docx` | 1.8 MB | Same content, 37 pages, with the twelve clue images embedded and captioned |
| `LLM_REVIEW_PACKET.pdf` | 2.3 MB | PDF rendering of the above |
| `dossier_images/` | 1.8 MB | Twelve clue images, listed below |
| `LLM_REVIEW_EVIDENCE.zip` | 2.1 MB, 40 files | Compact evidence bundle: this document, all images, all nine scripts, the small result JSONs, the gateway captions, the Audubon concordance and plate index, the channel and Shorts snapshots, the author's stream transcript, and the contest rules |

### 14.2 Clue images

| File | Shows | Source |
|---|---|---|
| `01_desk_prop_collage.jpg` | Nearly every prop in one frame: monitor stickies, pink note, case stickies, red pad, "Boo! Five of these", wall boxes, jigsaw pieces | Community collage, `work/reddit/img/r02.png` |
| `02_case_stickies.jpg` | The six alternating case stickies including `251634` | 4K crop, 12:45 |
| `03_blue_flowchart.jpg` | `(364)`/`(4445)` → `(66)` → `(6)`, plus the silhouette sheet at right | 4K crop, 12:45 |
| `04_red_pad.jpg` | `(527)` → `(83544)` → struck `MR` `(9)` | Collage crop |
| `05_pink_note.jpg` | All 24 (plate, numeral) pairs, legible | Community collage |
| `06_monitor_stickies.jpg` | `LSWRTE/NNHTIN/HDOTA` + "Books w/ old names… Alphabetize?" | 4K crop, 9:04 |
| `07_jigsaw_pieces.jpg` | Elf (II/XI), barred door (VII/I), bar chart (VIII/IX) — clearest view of the two-colour numerals and the tabs | Community collage |
| `08_mask_15_asterisks.jpg` | The completed entry animation with all 15 asterisks numbered | `tools/count_submission_mask.py` |
| `09_spawn_labels.jpg` | The six Minecraft hotbar bird labels with their frames | `tools/audit_blue_251634.py` |
| `10_piece_atlas.jpg` | Per-piece crop atlas (some crops missed their piece; included for completeness) | 4K frames |
| `11_boo_five_of_these.jpg` | The "Boo!" book poster: BOO + BOOK = boobook, five of them | Community collage |
| `12_wall_boxes_674.jpg` | Left wall strip rotated 90°; read right→left = top→bottom: 6, 7, 4, then badges 2, 1, 4; also the Tasmania piece with red VII | Community collage |

### 14.3 Pre-existing research files (preserved, unchanged)

| Path | Role |
|---|---|
| `HANDOFF.md` | Single-page entry point for the next agent; latest results at the top, historical notes below |
| `SOLUTION_PROGRESS.md` | The verified derivations and their source caveats |
| `FINDINGS.md` | Full chronological log, 29 sections. **Contains superseded conclusions — see §12** |
| `VIDEO_AUDIT.md` | The 15-asterisk correction and the targeted prop re-inspection |
| `candidates.md` | Guess shortlist and submission mechanics, with a submission log |
| `council.md` | 2026-09-03 five-persona council on where to spend effort |
| `tools/*.py` | Nine scripts (seven analytical, two OCR helpers); all reproduce their claims with asserts. `verify_dossier.py` was added by this pass |

### 14.4 Large local material — deliberately NOT bundled

These stay on the original machine at `/home/jayant/Desktop/mrbeast-challenge/`. Total ~6 GB.

| Path | Size | Why omitted |
|---|---|---|
| `work/orig_4k.webm` | 1.7 GB | Original 3840×2160 VP9 stream of the host video. Re-obtainable with `yt-dlp -f 313 82CX6WULNA0` (needs yt-dlp ≥ 2026.08 with deno, or YouTube truncates at 92 MB) |
| `vidssave… 1080P.mp4` | 337 MB | 1080p re-encode |
| `vidssave… 256KBPS.mp3` | 25 MB | Audio track |
| `work/colin/` | 1.3 GB | Colin's two videos at 1080p, plus extracted frames |
| `work/frames/` | 1.0 GB | 1 fps 1080p frames and contact sheets |
| `work/frames4k/` | 632 MB | 4K frames and prop crops (`desk765/`, `notes/`, `cards/`, `pink/`, `rain/`, `tvm/`) |
| `work/twitch/` | 571 MB | Colin's 3 h 10 m Twitch VOD + 16 kHz WAV. **The 133 KB transcript `thursday.txt` is worth keeping** |
| `work/yt/` | 285 MB | Downloaded candidate videos, metadata, captions, thumbnails |
| `work/cc_official/`, `work/cyberchef/` | 226 MB | Official and linked CyberChef builds, kept for the tamper diff |
| `work/audio/` | 51 MB | Spectrograms, mono WAV |
| `puzzle.pdf` | 70 MB | The 84-page $1M answer key. Public at `mrb.gg/p/puzzle` |
| `CyberChef_73a55e35….zip` | 83 MB | The linked offline build. Verified stock |
| `work/ocr_colin_howto.json` | 7.7 MB | Partial OCR of Colin's walkthrough (stopped at ~590 of 1867 frames) |
| `work/reddit/` | 9.5 MB | RSS/JSON dumps and collage images. **`img/r02.png` is the important one and is bundled as image 01** |

**A reviewer needs none of these.** Every claim in this dossier is either stated in full here,
shown in an embedded image, or reproducible from the bundled scripts plus the small data files
in the ZIP.

### 14.5 Environment notes

- `yt-dlp` must be ≥ 2026.08 with `deno` installed, or YouTube truncates the 4K stream at 92 MB
  with HTTP 403.
- `rapidocr_onnxruntime` and `opencv-contrib-python-headless` were installed with
  `pip --break-system-packages`.
- `tools/solve_desk.py` needs `lxml` and the cached concordance + gateway captions.
- Dictionary filters use `/usr/share/dict/american-english` and `british-english`. These are a
  **filter, not an oracle**: proper nouns, including HEDWIG, are absent from them.

---

## 15. Closing statement of what is true

- The red chain is solved: **FANTASTIC**, derived exactly, no fudging.
- The blue chain is solved to **FOURTH UPLOAD**, derived exactly.
- One clue, **251634**, is written on the desk in the blue chain's own colour and has no role.
- One step, **(66) → (6)**, has no demonstrated mechanism.
- **FANTASTIC HEDWIG** is a candidate that matches another solver's public commitment. Its
  six-letter half has never been extracted by anyone, publicly or here.
- The contest's status is unknown, and the rules are structured so that an entrant cannot learn
  it from silence.

Anything beyond that is speculation, and this dossier tries hard to say so wherever it applies.
