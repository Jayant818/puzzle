# MrBeast $10,000 Video Puzzle — Plan, Findings, Log

> Start with `HANDOFF.md` (single-page summary for the next agent). This file is the full chronological log.

**Current status, 2026-09-06:** red independently resolves to **FANTASTIC**;
blue independently resolves through **FOURTH UPLOAD**, with **251634** still
unused. **FANTASTIC HEDWIG** matches a community solver's published checksum,
but the final blue extraction and official correctness are unverified. The
user reports submitting it and receiving no team response; the assistant has
not submitted entries. The author has now confirmed two production errors:
an extra blue I on the grass piece and a missing 2 on the red pad (section 25).
Older sections are historical and contain explicitly superseded conclusions,
especially the rejected case-mask theory, BEASTSAND/STUNTS, and the 16-star count.
The latest tests and practical lessons are in sections 24-28.


Video: "How 1 Person Solved A $1,000,000 Puzzle!" (@MrBeast2, id `82CX6WULNA0`, published 2026-09-02, 17:47, 1067 s, 31981 frames @ 29.97 fps).
Puzzle author: Colin Sanders (DoctorXOR, winner of the $1M puzzle). First correct answer at https://puzzle-video-sweepstakes.mrbeast.app/ wins $10k.
Working dir for all extracted material: `work/` (frames, audio, OCR, subtitles, site dumps).

---

## 1. The single most important lead (confirmed)

The **pinned comment** by @MrBeast on the video says:

> Make sure you check out Colin's profile 👀 https://tinyurl.com/xorprofile

That tinyurl 301-redirects to a **CyberChef recipe**:

```
https://gchq.github.io/CyberChef/#recipe=XOR({'option':'UTF8','string':'%H6U=)Z7</#bq'},'Standard',false)&input=QWFhYWFBLWFhQWEjIw
```

- Operation: **XOR**, key = UTF-8 string `%H6U=)Z7</#bq` (13 bytes: `25 48 36 55 3D 29 5A 37 3C 2F 23 62 71`), scheme Standard, null-preserving off.
- Input placeholder (base64 `QWFhYWFBLWFhQWEjIw`) decodes to **`AaaaaA-aaAa##`** — 13 characters.
- Interpretation: somewhere in the video is a 13-character string. Paste it into that recipe and the XOR output is the answer (or the next step). The placeholder is a shape hint: 13 chars, letters, a hyphen at position 7, two digits at the end.
- The exact case pattern is NOT literal: I tested it. If the ciphertext had exactly that case pattern the XOR output is garbage (`d)W4\hwV]nBAR`), and no readable plaintext can produce that exact case pattern. So treat the placeholder as "13 chars, letters + hyphen + 2 trailing digits", something like a serial number / model number / code.
- Constraint from the key (useful for filtering candidates): for the XOR output to be readable text, the found string must have letters where the key does, and the found string's positions 2, 4, 7 XOR to digits/punct/space, positions 12–13 XOR to uppercase/digits. `tools/xor_check.py` tests any candidate.

The person who sent you the "AaaaaA-aaAa##" analysis was correct about the URL contents. Their regex `^[A-Z][a-z]{4}[A-Z]-[a-z]{2}[A-Z][a-z]\d{2}$` is too strict (see above); search for any 13-char `XXXXXX-XXXX99`-shaped token.

## 2. What is in the description / linked material

- Description links only: mrb.gg/p/puzzle (returns 403 to scripts; it is the 84-page answer-key PDF you already have), the sweepstakes site, Colin's channel @doctorxor, and Colin's video https://youtu.be/XCOkRKUe3Nc ("How to Solve a $1,000,000 Puzzle", 31 min, walkthrough of the 9 Phase-0 puzzles plus a "Riddle #1" brain teaser at 0:25 whose answer per comments is "oh").
- **CyberChef zip** (`CyberChef_73a55e35…zip`): stock GitHub Actions build of CyberChef at commit `73a55e35` (2026-09-01, "fix: use defaults for blank number ingredients"). Compared file-by-file to the official v11.4.0 release zip: identical file list, HTML differs only in version string/build time. **Not tampered.** It is just the offline tool; the recipe is in the tinyurl above.
- **puzzle.pdf**: full solution book for the $1M hunt (84 pages, made 2026-08-12 on macOS). Useful as a style guide for Colin/Lone Shark puzzle idioms: A=1 letter mapping, ASCII, base-3 colors, Morse (incl. reversed video), semaphore, Caesar shifts by count, pigpen, Braille-like dots, atomic numbers, birthstones, Scrabble tiles, acrostics/first letters, what3words, closed-caption hyphen tricks (SB12), single-frame inserts (OP1 jigsaw, 20 frames). Expect the $10k puzzle to reuse one of these idioms.
- **Sweepstakes site**: Next.js static page. Form: "Guess the answer" (free text, multiple guesses allowed), email, 18+ checkbox. No cookies, no hidden fields, no HTML comments, no hints. Official rules: first 100%-correct answer wins; clues are "in the Video".

## 3. Video structure (from 1 fps contact sheets, `work/frames/sheet_*.jpg`)

- 0:00–0:45 intro (vault, laptop, playlist recap), 0:45–15:40 Jimmy in a "detective office" set (corkboard wall of props, desk with monitor) recapping the 91 locations, 15:40–16:55 Colin at the vault, 17:00–17:47 **new ending scene**: a vintage Zenith TV/VCR combo on a desk plays "PAUSE ⏸", then a fast recap montage, a "?" over Jimmy, Colin interview B-roll, a mock of the sweepstakes form being typed (15 asterisks; corrected in section 23), SUBMIT, "$10,000", the QR code (decodes to exactly `https://puzzle-video-sweepstakes.mrbeast.app/`, nothing else), "thank you for watching", then black with "SUBSCRIBE FOR A COOKIE" and a bouncing cookie that ends by filling the screen.
- Props on the ending desk: orange rotary phone, cardboard box with a green tape strip (no legible writing at 1080p), a green sticky, and a **handwritten note** partly hidden by the box reading `(364)` → `(62…` ↓ `(6)`. The rest is under the box in every frame (camera is static). Unexplained so far; could be Colin's scratch paper prop or a clue.
- Detective-office props: sticky notes "LIMA PERU", "LIGHT BLINKS", "COOKIES?"-looking note, monitor stickies ("Books w/ old name… alphabetize?", a blue one with block capitals `SWRTE / NNRTIN / NOOTA …` — unreadable at 1080p), "META PUZZLES" label, box labels "Puzzle Clues"/"Rules". These look like $1M-hunt set dressing, but the blue monitor sticky has not been read yet.


### 3b. Main thumbnail details (`work/yt/thumb_82CX6WULNA0.jpg`, 1280×720)
- Left panel "LOGIN ATTEMPTS LOG", 17 rows, all FAILED: 04-12, 04-12, 04-23, 04-29, 04-27, 04-23, 04-27, 05-01, 05-05, 05-06, 05-10, 05-12, 05-15, 05-20, 05-21, 05-23, 05-28 (all -26). Day→letter and other trivial mappings give nothing.
- "ACCESS DENIED / INCORRECT PASSWORD", "ENTER PASSWORD" with 10 dots, SUBMIT.
- Green terminal text: SYSTEM STATUS: LOCKED, NETWORK CONNECTION: INTERNAL, USER ID: 127-666-F733 (12 chars, not 13), LOCATION: VIRGINIA, 1235?, STATUS: OFFLINE, plus log lines (19:07:2?), (10:00:26), (10:00:16) GC…, (19:00:18) LOCA…, (16:00:15) ALERT: B….
- Corkboard: #1 smoke grenade "1+1=1", #2 a QR code (too blurry to decode even with WeChatQRCode/Aruco; centre has a round logo) with sticky "Scan on phone — what is it?", #3 photo, #4 phone with emojis, stickies "Emma, Boston server logs? access logs?", "Brass. Book. I saw one like it in dream. Or was it not real?", "No face ID bypass? Check #5 version", "16-3-4" (→ P-C-D), "Key to … free … 2…", "Colors vs …?", Salesforce logo, Rubik's cube, gold vault "$1,000,000".
- Verdict: looks like thumbnail-team flavour, not Colin's cipher. Keep as low-priority lead (the QR would be worth decoding if a sharper source appears).

## 4. Technical sweeps done and their results

| Sweep | Method | Result |
|---|---|---|
| Container/metadata | mp4 atoms, mp3 ID3, trailing bytes | Clean. Only ftyp/free/mdat/moov; ID3 has only encoder tag. vidssave re-encode (Lavf62), so any original YouTube metadata is gone anyway. |
| Full-video spectrogram | ffmpeg showspectrumpic log/lin, L−R difference | No hidden image in high frequencies, no obvious Morse/DTMF bands. Audio is lowpassed ~17 kHz (AAC). |
| Outro audio 17:37–17:47 | zoomed linear spectrogram | Synth "boing/wah" tones synced to the bouncing cookie, plus a noise burst when the cookie explodes. Not DTMF (has harmonics). A commenter claims the 17:36 music is from the film *Obsession*. Not yet checked for reversed speech. |
| Single-frame inserts | 64×36 grayscale of all 31981 frames, anomaly score = frame differs from both neighbours while neighbours match; then repeated at 160×90 in a 4×4 region grid | Found only stylistic flickers/wipes: 1:07, 6:20 (glitch transitions), 16:10.0–16:10.2 (Colin/black alternating ×3), 17:12.0 (TV image/black ×5), 17:17.9 (flash), and half-white wipe frames at 0:59, 1:23, 2:41, 3:24, 5:07, 5:41, 11:44, 12:07, 12:12. **No hidden text frame** at either resolution. |
| Scene list | 691 cuts >25 mean-diff | Used to build sheets. |
| Solid-colour frames (base-3 colour cards, Kabul-style) | 32×18 RGB, low spatial std | Only white flashes, beast.travel page backgrounds and the money wall. Nothing. |
| Multi-frame averaging of small props (monitor sticky, desk note) | median-filtered mean over static shots | Smeared: camera drifts. Needs feature alignment (ECC/ORB) before averaging. |
| QR code | OpenCV | Exactly the sweepstakes URL. |
| Closed captions (EN, uploaded, speaker-coloured) | yt-dlp VTT dump, dedupe | 503 unique lines. 100 hyphens are ordinary (`Lap--`, `ninety-one`, `R-62…`). Zero-width spaces (10162) are structural (7 per first-line cue, 6 per second-line cue), not a bit-stream. Speaker colours map to speakers. First-letter acrostic is noise. FR/ES/DE/JA tracks are normal translations. |
| OCR of all 1 fps frames | rapidocr, `work/ocr_frames.json`, 7066 distinct tokens | **Done, no match.** No token of shape `X{6}-X{4}99`; the only 13-char letter+digit tokens are crossword clue fragments, `R62L39R05L736`, `bacothetaco95`, `JamesDean49AM`. 13-digit `3131413323331` is the tents-puzzle column numbers. Rare-token dump reviewed for frames 0–1067. |
| Whole-track pure-tone scan (DTMF/Morse) | 1024-pt FFT, 600–1700 Hz, top-4-bin energy ratio | Nothing. One 0.1 s blip at 3:58. |
| Uploaded vs auto-generated captions | word-level diff | No inserted/extra words in the uploaded track. Auto captions transcribe the outro song as vocals ("oh baby"), i.e. the 17:36 music has lyrics; song not identified yet. |
| TV static at 17:00 | mean/std of 73 frames of the "PAUSE" static | No hidden image; just the PAUSE label and the following wall shot bleeding through. |
| Bouncing cookie 17:42–17:47 | centroid tracking at 480×270 | Simple DVD-logo style bounce, no encodable pattern found. |
| ECC-aligned frame stacking | cv2.findTransformECC affine, 35–45 frames | Wall stickies now legible: "LIMA PERU", "X'S ON BELT", "LIGHT BLINKS" ($1M-hunt set dressing). Desk note and monitor sticky still too small/blurred at 1080p. |
| Video thumbnail(s) | maxresdefault + A/B variants maxres2/maxres3 | Main thumbnail is a designed "ACCESS DENIED" hacker board (see §3b). The two A/B alternates are plain stills (Botez sisters; Jimmy). Because the thumbnail is A/B-tested it is an unreliable puzzle carrier, but its details are logged below. |
| Colin's channel assets | banner, avatar, about | Banner = repeating "DOCTORXOR" text, avatar = D-shaped XOR-gate logo, about = Twitch schedule + a Steinbeck quote. No puzzle content. |
| Rapid "instructions" montage 5:16–5:24 | 10 fps distinct-frame extraction | All cards are the PG1–PG13 instruction cards from the PDF (Salina Turda, Seoul, Lower Hutt, Tbilisi, Toad Suck, Tijuana, Kandi, Ankara, Doha, Cairo, Maputo, Armavir). No extra card. |
| TV recap montage 17:00–17:30 | 3 fps crops of the screen | All clips are from this video or the $1M footage. New elements: "?" graphic, Colin interview B-roll, mock form. |
| Comments (top 300) | yt-dlp | Only useful one is the pinned tinyurl. One comment: "It's definitely only with the things you can see in the investigation room MrBeast is in right?" (unverified). |

## 5. Dead ends (don't redo)

- CyberChef zip tampering — clean.
- Sweepstakes site source/cookies/headers — nothing.
- VTT zero-width spaces / hyphens / colours — structural.
- QR code — plain URL.
- Placeholder case-pattern as literal cipher shape — mathematically impossible with this key.
- Foreign caption tracks — normal translations.
- Whole-track DTMF/Morse tone scan — nothing.
- TV static averaging — nothing.
- Login-date letter mappings in the thumbnail — nothing.
- Every 13-char guess tried so far (`tools/xor_check.py`): contest dates, hashtags, Slack channel names, names — all junk after XOR.

## 6. Plan (ordered) — updated after the second pass

1. ~~OCR sweep~~ done, no match.
2. ~~Higher-resolution hidden-frame pass~~ done, no match.
3. **Read the small text in the set**: the blue monitor sticky (`SWRTE/NNRTIN/NOOTA`), the ending-desk note `(364)→(62…→(6)`, the box tape. Use the frames where each is largest/brightest; stack/average multiple frames to denoise.
4. **Audio**: (a) reverse the outro and the intro and listen/spectrogram for speech; (b) scan the whole track for two-tone (DTMF) or on/off (Morse) segments with a tonality detector; (c) identify the outro music (Shazam-type) since a commenter flagged it.
5. **Frame-accurate look at the flickers** (16:10.0, 17:12.0, 17:17.9): count on/off pattern as binary/Morse.
6. **Cross-reference Colin's video** (`work/yt/colin_plain.txt`): any 13-char string or hint there; "Riddle #1" is unrelated per comments.
7. **Get a better source.** Everything above used a 1080p re-encode from vidssave. Download the original 1080p/1440p/4K stream with yt-dlp (`-f bestvideo`) and redo the prop zooms (desk note, monitor sticky, box tape, TV bezel) — if the clue is small printed text this is the single highest-value step.
8. **Watch the video end-to-end at 1× with fresh eyes** for anything OCR/anomaly detection cannot catch: spoken asides, on-screen text that is only briefly legible, background monitors, gestures.
9. Candidate testing: every 13-char string found goes through `tools/xor_check.py` (prints XOR output and whether it is printable/readable). Submit only readable outputs.
10. Track community progress (r/MrBeast, Colin's Twitch/Instagram) — nothing public found yet as of 2026-09-03.

## 7. Files

- `work/frames/sheet_00..17.jpg` — 1 fps contact sheets (60 s each).
- `work/frames/anom_sheet.jpg`, `end_sheet_*.jpg`, `tvm_sheet.jpg`, `instr_sheet.jpg`, `typing_sheet.jpg`, `last_sheet.jpg` — targeted sheets.
- `work/frames/paper_sheet.png`, `paperzoom_*.png`, `desk_*.png`, `d544_*.png`, `w53z_*.png` — prop zooms.
- `work/audio/*.png`, `work/audio/full16k.wav` — spectrograms and mono WAV.
- `work/yt/` — description, info.json (with comments), EN + FR/ES/DE/JA captions, Colin's video description/captions, `mrbeast_plain.txt`, `colin_plain.txt`.
- `work/site/` — sweepstakes HTML, headers, official rules.
- `work/cyberchef/`, `work/cc_official/` — linked and official CyberChef builds.
- `work/ocr_frames.json` — OCR output per frame.
- `tools/xor_check.py` — candidate tester for the CyberChef recipe.

## 8. 4K pass (2026-09-03, original stream `work/orig_4k.webm`, format 313 VP9 3840×2160)

Getting it required updating yt-dlp (was 2026.03.17, now 2026.08.19) and installing deno; the old build truncated at 92 MB with HTTP 403.

| Prop | 4K result |
|---|---|
| Ending-desk handwritten note | Reads `(36·4)` → `(6 2…` ↓ `(6)`. The rest is under the box in every frame of the static shot. Still unexplained. |
| Box tape | Blank green masking tape. |
| TV | "zenith", "COLOR TV-VCR COMBINATION", VHS logo, tiny feature text. No model number visible. |
| Rotary phone | No number card in the dial. |
| Vault tablet 16:12 | iPad status bar "4:51 PM Sun Mar 8", 51 % battery. |
| Monitor stickies 9:04 | Blue: `LSWRTE / NNHTIN / HDOTA / should I call it bird food?`. Yellow: `Books w/ old names… Alphabetize?`. Desk sticky: `Roman numbers for Roman words?`. Wall stickies: `CODE ON DOOR`, `DASHES`, `X'S ON BELT`, `LIGHT BLINKS`, `LIMA PERU`. All read as detective-notes about the $1M puzzles (SB3, SB12, SB2, SB4, SB2; PG6 bird code; PG11/12). The blue grid's 17 letters (ADEHHILNNNORSTTTW) anagram to nothing obviously meaningful; column/boustrophedon reads are noise. Probably prop humour ("Red Herring Bank"), kept as a low-priority lead. |
| User-supplied `thumbnail.avif` | 720×404, lower than the 1280×720 already pulled; QR still undecodable. |
| Colin's channel | Banner/avatar/about contain nothing. |

Net: the 4K pass did not surface a 13-character token. The desk note remains the only unexplained prop in the new footage.

### 8b. New leads found during the 4K pass

- **Digit "rain" shot at 17:09–17:10 — CLOSED.** Grid analysis (34×32 px cells, 36×45 grid) shows the glyph at each cell re-rolls randomly frame to frame (78 % agreement between consecutive frames, 36 % after two frames, 15 % after five; no vertical/horizontal shift explains it), so there is no fixed text to read. It is a flicker effect. Original note follows for the record. **Digit "rain" shot at 17:09–17:10 (inside the TV montage, not present anywhere else in the video).** Colin walks toward camera while the previous shot dissolves into a grid of glowing digits. At 4K the glyph set is `= 4 7 3 2 5 6 9`, and the glyph chosen at each cell tracks the brightness of the underlying footage (sky → 9/6, mid-tones → 5/2/3, shadows → 4/7/=). It behaves like a standard "ASCII-art" transition effect, so it is probably aesthetic. Kept as a lead because it is new footage; a full grid transcription is in `work/frames4k/rain/` (frames r_006–r_045 are the static part) if someone wants to test T9/multi-tap or Polybius readings. Rows read so far: `73=32=52=`, `==44=35555555==`, `==3335=55233==`, `4353255533`, `==3225553355`, `4444===`, `66696`, `99696`, `=3=33`.
- **A viewer on Colin's newest video** ("The Ramblings of a Million Dollar Winner (Riddle #0: The Hat Trick)", uploaded 2026-09-02, id `aFo8P073eSY`) asked Colin about "the numbers 674 on the right" in the MrBeast video. No "674" appears in the 1080p OCR or in the 4K OCR of the studio/ending frames; the 4-second 4K tiled OCR sweep (`work/ocr4k_seq.json`) is checking the rest. Colin did not reply. That video itself contains three story riddles ("Riddle #0") that Colin says cannot be solved "until I push a button somewhere"; its transcript (`work/yt/ramblings_plain.txt`) has no reference to the $10k puzzle.
- **Mock sweepstakes form in the TV montage** is titled "BEAST SWEEPSTAKES", placeholder "Type your answer here...". Correction, 2026-09-05: the completed animation has **15**, not 16, asterisks; see section 23 and `VIDEO_AUDIT.md`.

### 8c. 4K tiled OCR sweep (every 4 s, 267 frames × 12 tiles) — done

- No token matching the `XXXXXX-XXXX99` shape anywhere.
- No "674". The only 67/74 tokens are crossword clue numbers (67A/74A, 167A/174A, 67D/74D) during the crossword section 10:44–11:16, which sit on the right half of the frame. Most likely explanation of the "674 on the right" comment: a viewer reading "67" and "4" from the clue list. Treat as noise unless Colin replies.
- Full token dump: `work/ocr4k_seq.json` (267 frames, positions in 4K pixel coordinates).
- Separate 1 fps 4K OCR of the intro laptop screens (0:17–0:47) is in `work/ocr4k_intro.json` (checks the fake YouTube page/comments for a planted code).

## 9. Set-dressing inventory from the 4K source (2026-09-03, third pass) — the real candidate material

Commenters on the video and on Colin's channel kept pointing at "the paper at the end", "the phone", and "674 on the right". At 4K these all resolve to props on Jimmy's detective-office desk, which is the same desk (same orange rotary phone) that appears in the ending TV scene. Best frames: 0:18 (`work/frames4k/desk765/d_18.png`, widest view of the boxes), 5:40 (`frames4k/notes/n_340_full.png`), 12:45 (`frames4k/desk765/d_765.png`, clearest desk), 17:00–17:47 (ending).

### 9a. Handwritten number notes (parenthesised numbers joined by arrows)
- Red ink notepad (5:40 and 12:45): `(527)` ↓ `(83544)` ↓ `M̶R̶ (9)` — "MR" written then struck out before the (9).
- Blue ink sheet (12:45, and partly visible under the box at 17:00–17:47): `(364)` and `(4445)` both arrow into `(66)`, which arrows to `(6)`.
- Purple doodle sheet: `$10,000!`, and a sheet of bird silhouettes (PG6 bird code).
- Reading: these look like crossword/cryptic **enumerations** (word lengths): (3,6,4)=13 letters, (4,4,4,5)=17, (6,6)=12, (6); (5,2,7)=14, (8,3,5,4,4)=24, (9). Note 13 = the CyberChef placeholder length. Not proven. Trivial alternatives tested and rejected: A1Z26, digit sums/products, phone-keypad (T9) words, US area codes, octal/hex.

### 9b. Sticky notes on the black equipment case (right of desk, 12:45)
`081 XIV Seahawks?` · `## How many?` · `QX=TH` · `251634` · `PLATES` · `YouTube link.. watch?`
- `QX=TH` is a cryptogram crib (Q→T, X→H). `251634` is a permutation of 1–6 (a reading order). `PLATES` matches PG7. `081 XIV` and Seahawks: Super Bowl XIV was 1980, Seahawks were not in it; unexplained.

### 9c. Picture cards with Roman numerals, stuck on the boxes (0:18 wide shot is the best view)
Each card is a notched/tabbed tile (jigsaw-like, they can chain) with a picture and TWO Roman numerals, one red and one blue:
elf (II/XI) · window (I/VII) · falling bar chart with arrow (VIII/IX) · ribbon bow (V/VII) · orange door (VI/VIII) · snow cloud (IX/V) · laughing-crying emoji (XIV/X) · hedgehog+eagle (IX/VII) · Route 66 shield (IV/II) · teal phone/ticket (VI/VI) · Oman flag (VI/V) · Africa map + pineapple (VIII/IV) · US flag + red barn (IV/VII) · black bull (VII/?) · plus more on the far boxes not yet resolved.
- The pictures are drawn in emoji style. Hypotheses: (a) emoji names indexed by the numerals (SB8/OP1 style), (b) cards chain domino-style by matching numerals and the pictures read out a message, (c) the sticky `251634` gives the reading order. None tested yet: a complete, unambiguous card inventory is needed first.
- Desk sticky "Roman numbers for Roman words?" clearly refers to these cards.

### 9d. "674"
Three stencilled electrical boxes on the right brick wall carry numbered circles 6 (blue), 7 (pink), 4 (white/black), top to bottom (`frames4k/desk765/wallboxes_18.png`). This is what the commenter meant. Meaning unknown; colours resemble the SB7 screen-colour scheme.

### 9e. Other desk items
Pink note with rows of handwritten capitals (9:04, left of keyboard) — almost certainly the cryptogram that `QX=TH` refers to, but too small/angled even at 4K; blue sticky `LSWRTE/NNHTIN/HDOTA — should I call it bird food?` and yellow `Books w/ old names… Alphabetize?` on the monitor; yellow `Roman numbers for Roman words?` on the keyboard.

### 9f. Checked against the PDF
Pages 22–63 (SB6–SB12, PG1–PG13, GC1–GC11, OP1–OP10) contain nothing resembling the number notes, the stickies or the Roman-numeral cards. So they are either red-herring set dressing (the hunt's theme is literally "Red Herring Bank") or Colin's new puzzle. Given that the enumeration (3,6,4) equals the 13-character target and the cards are the only untested structured object in the video, this is the current best lead.

### 9g. Status after checking the whole PDF and every wide shot
- PDF pages 64–84 (OP11–OP14, MP1–MP40, MM1–MM4) also contain nothing like the number notes, the case stickies or the Roman-numeral cards. Nothing in the 84-page answer key explains them.
- The pink cryptogram note (9:04, left of the keyboard) has about nine rows of hand-printed capital-letter groups. Even isolated at 4K and sharpened (`work/frames4k/pink/pinknote_545.0.png`) it is motion-blurred beyond legibility. The white sheet next to it carries a small printed letter/symbol table.
- Card inventory so far (14 cards, from `work/frames4k/cards/right_sheet.jpg` and `frames4k/desk765/boxes_d_18.png`): elf II/XI · window I/VII · falling bar chart VIII/IX · ribbon V/VII · orange door VI/VIII · snow cloud IX/V · laughing-crying emoji XIV/X · hedgehog+eagle IX/VII · Route 66 shield IV/II · teal ticket/phone VI/VI · Oman flag VI/V · Africa+pineapple VIII/IV · US flag+red barn IV/VII · black bull VII/?. Several cards are only ever seen edge-on or half-covered, so the set is probably incomplete.
- Nothing in these props has yet produced a 13-character string to feed the XOR recipe. Everything above is documented so the next person does not have to re-find it.

## 10. Recommended next steps (in order)
1. Get legible source for the props: MrBeast/Beast Industries behind-the-scenes photos or shorts of this set, Colin's Thursday Twitch stream (he may discuss it), or ask in r/MrBeast for anyone with 4K screenshots of the pink note.
2. Treat the enumeration notes as instructions: find a (3,6,4) 13-letter phrase and a (4,4,4,5) phrase in the video (spoken or shown) whose combination yields a (6,6) and then a 6-letter word; similarly (5,2,7) → (8,3,5,4,4) → 9-letter word. Candidate finals are what the sweepstakes form may want.
3. Finish the Roman-numeral card inventory and test: emoji-name indexing by the numerals; domino chaining by matching numerals; ordering by the `251634` sticky.
4. Keep `tools/xor_check.py` as the gate: any 13-character candidate must XOR to something readable before it is submitted.

## 10b. Persona council (2026-09-03)
Five-persona council (Einstein, Da Vinci, Satoshi, MrBeast persona, Munger) was unanimous for decoding the desk props over further video sweeps; full verdicts, exit conditions and the Reckoning predictions are in `council.md`.

## 11. Submission mechanics and hit-and-trial (2026-09-03)
The site's JS shows the flow: POST /api/entries {guess,email,agree} → entryId → emailed 6-digit code → POST /api/entries/verify → "You're in the running… You can submit another guess anytime." No client-side check, no correctness feedback, 500-char free-text guess. Multiple guesses are invited; automated submission would breach the tampering clause, so guesses go in by hand. A ranked shortlist lives in `candidates.md`. XOR of every structured string visible in the video (vault code, tablet text, IDs, prop numbers, stickies) against the key yields nothing readable, so no derived candidate yet outranks the thematic guesses.
- MrBeast brand/history strings (Feastables, MrBeast Burger, Lunchly, Beast Games, Team Trees/Seas/Water, Viewstats, Step, MrBeast6000) were XOR-tested as 13-char ciphertexts: all junk. Added as Tier 5 blind guesses in `candidates.md`; the cookie ending most plausibly nods at Feastables' Cookies & Creme bar.

## 12. Anagram check on the blue monitor sticky (2026-09-04)
- Claim (from an outside AI write-up): `LSWRTE NNHTIN HDOTA` (17 letters) anagrams to **LAST WORD THEN NINTH** (4,4,4,5), matching the `(4445)` node on the blue desk note.
- Verified: the letter multiset `ADEHHILNNNORSTTTW` is an exact anagram of LASTWORDTHENNINTH. The 4K crop (`work/frames4k/d544_mon_stickies.png`) confirms the transcription and the yellow neighbour "Books w/ old names… Alphabetize?".
- Uniqueness: NOT unique. Dictionary enumeration gives 3815 (4,4,4,5) multiset solutions, 2034 using only common words, 134 containing two or more instruction/ordinal words (e.g. LAST THEN WORD NINTH, SALT THEN WORD NINTH, HALT NEST WORD NINTH, HINT THEN WORD SLANT). LAST WORD THEN NINTH is the most sentence-like, so treat it as the leading reading, not a proof.
- Not a keyed columnar transposition with the `251634` sticky (both conventions, both directions tested).
- Applied naively: transcript last word "video", 9th word "Bowl"; title last word "Puzzle!"; nothing meaningful yet. The instruction probably applies to the still-unfound (3,6,4) 13-letter phrase or to the Roman-numeral cards.
- The yellow sticky `BOOKSWOLDNAMES` (14 letters) was tested as a (5,2,7) scramble for the red chain: 48 anagrams, none instruction-like (BOOKS WE ALMONDS…). It is plain text, likely a hint ("alphabetize" = an ordering step; "old names" may point at Latin/Roman names or old book names).
- OCR of every frame (1080p 1 fps, 4K every 4 s) contains no all-caps (3,6,4) block and no unexplained 13-letter block, so if the (3,6,4) phrase is on set it is handwritten and unread (pink note) or must be constructed (cards).

## 13. New avenues started 2026-09-04 ("try something else")
- Colin's own two videos (`XCOkRKUe3Nc` 31 min, `aFo8P073eSY` 12 min) downloaded at 1080p to `work/colin/`, frames at 1 fps, tiled OCR running → `work/ocr_colin_howto.json`, `work/ocr_colin_ramb.json`. Rationale: the MrBeast description says "Check out Colin" and links these; the original hunt hid pieces in linked videos and pinned comments, and neither video has been scanned for a 13-char token.
- Colin's Twitch VOD "Just a normal Thursday" (v2864667604, ~3 h 10 m, most recent stream) audio downloaded to `work/twitch/` for transcription with faster-whisper; grep targets: 10,000 / MrBeast / puzzle / props / desk / XOR / CyberChef / hint. Satoshi's and Munger's exit conditions (Colin on record about the props) could be settled here.
- Outro music identified from comments as MrBeast's old-school outro song (nostalgia callback), so the "song ID" item is closed.

## 14. Colin on record (Twitch VOD "Just a normal Thursday", 2026-09-03 21:33 ET start; transcript `work/twitch/thursday.txt`)
Whisper transcript, quotes lightly cleaned:
- ~24:09 "the current 10k outstanding MrBeast puzzle — I made it by myself." / "It is not as big as the Super Bowl puzzle."
- ~24:51 on AI: he discusses AI guessing familiar mechanics. Correction from a fuller September 6 transcript review: the "old hat" remark is conditional/general, not confirmation that the $10k puzzle copies a particular earlier puzzle. See section 27.
- ~41:30 "I did make the 10k puzzle myself… I don't want to say too much until it's been officially over with."
- ~2:10:20 "I can't discuss it until someone solves it and Team Beast announces a winner" → as of Thursday night no winner had been announced, so the Reddit "we were done at 11:30" claims are unconfirmed.
- ~2:11:05 STARTING HINT: "The initial question is: have you solved the jigsaw puzzle? … In MrBeast's video, the first thing you should do is look for a jigsaw puzzle. That's as far as I'm going to say." (He also mutters "is there another entry point, one two three, there's three of them" but he was playing The Witness at the time, so that may be game talk.)
- ~2:13:25 "Plenty of people have posted a lot of hints online already that are far beyond that."
Implication: the fourteen notched emoji/Roman-numeral cards on the boxes are the jigsaw and the intended first step; the rest of the desk (enumeration tracker, stickies, pink index) comes after.

## 15. Community state (r/MrBeast via RSS, 2026-09-02 → 04; dumps in `work/reddit/`)
- Blue sticky subtext is "Should I call it bird FENCE?" (rail fence). Community reading of the letters: LAST WORD THEN NINTH (same as ours; still an anagram, not a mechanical transposition — all rail/columnar decodes tested, none produce it).
- Pink note transcribed by three users (two-column list of number + Roman numeral): 029 III · 037/039 VI · 042/044 V · 061/062 II · 074/079 IX · 076 IV · 081 XIV · 083 XI · 101/102 II · 102 III · 112 IX · 162 V · 184 V · 216 I · 225 VI · 235 VII · 245 VIII · 246 VIII · 253 XIV · 275 III · 329 X/XXVI · 337 VI · 358 IX · 424-6 XVI. Read as a book-cipher index (page + line/word). "081 XIV" matches the case sticky "081 XIV Seahawks?". Tested as video seconds + caption word/letter index: nothing. Candidate books: MrBeast & James Patterson's novel "The Most Dangerous Games" (released 2026-09-01, a "book with an old name" after the 1924 story), a Goosebumps book (one user), Bible books. Unresolved; no-purchase rules argue against the novel.
- Cards: users report the pieces physically interlock; one claims the assembled 14 read SUBSCRIBE TO MRB (unverified); another user's list of pieces: Oman flag, calendar (the "25" card), Feastables chocolate bar (our "orange door"), rain cloud, …, jail door. Latin-name indexing was tried and fails (chocolate has no Latin).
- 674 = Nauru's country calling code (+674) — a location-style answer candidate.
- One knowledgeable poster: "finish the owl → XOR → fourth upload chain"; another asks if the answer "is related to something that flies" and has 6 characters. Note OSPREY (a sea hawk) is 6 letters and flies; "Seahawks?" is on the case sticky.
- Two users claim to have finished on 2026-09-03 evening; unverified and contradicted by Colin's "until someone solves it".
- Many users report the verification email never arrives; keep that in mind when submitting.

### 15b. Pink note now legible (from a community collage, `work/reddit/img/r02.png`, crop `img/collage_pink.png`)
Two columns, hand-printed. Left: 029 III · 042 V · 074 IX · 081 XIV · 101 II · 112 IX · 184 V · 225 VI · 245 VIII · 253 XIV · 329 X · 358 IX · 424-6 XVI. Right: 039 VI · 061 II · 076 IV · 083 XI · 102 III · 162 V · 216 I · 235 VII · 246 VIII · 275 III · 337 VI. Twenty-four (number, Roman numeral) pairs, numbers ascending 29→426, numerals I–XVI. It sits on top of a printed sheet with a small table (illegible).
Candidate readings, none confirmed: (a) book cipher page+line/word into MrBeast & Patterson's "The Most Dangerous Games" (hardcover 480 pp, released 2026-09-01; the title is an old story name → "Books w/ old names"); (b) Beast Games player numbers + episode numerals (a Redditor tied the 6-7-4 wall boxes to "player 674" and to Nauru's +674 code); (c) video seconds + caption index (tested, nothing). The "Boo! Five of these" black book poster (0:17-0:19) probably names the book source ("Boo" + k). Rules say no purchase necessary, which argues against a paid novel unless preview pages suffice.
Other props now confirmed from the collage: a second set of numbered wall badges 2 (teal), 1 (white), 4 (orange) beside the 6-7-4 boxes; box handwriting "July 1st 1988 – June 30 89"; a box labelled INVOICES 2008-02; the desk monitor boots a "MrBeast XP" screen; jet tail number N407TC; the GC9 road-sign board (170, 12, 20, 20, 8, 126, 199, 30, 101, 38, 4, 880) is a recap prop.
- Colin's own videos: OCR of the 31-min walkthrough (571+ frames so far) shows only TV-show years and puzzle text, no 13-char token; Ramblings OCR pending.
- 2026-09-04: the background OCR of Colin's two videos was stopped at ~590 of 1867 frames of the walkthrough (nothing found in that portion); the Ramblings video was never OCR'd. Re-run with `tools/ocr_tiles.py` on `work/colin/frames_howto/` and `work/colin/frames_ramb/` if wanted; low expected value.

## 16. Jigsaw chain test (2026-09-04) — a real structural result
Using the best-read numerals (red, blue) per card: elf (II, XI) · window (VII, I) · falling chart (VIII, IX) · ribbon (V, VII) · Feastables bar (VI, VIII) · snow cloud (IX, V) · laughing face (X, XIV) · owl/eagle (VII, IX) · calendar-25 (IV, II) · teal ticket (VI, VI) · Oman flag (VI, V) · Africa+pineapple (IV, VIII) · US flag+barn (VII, IV) · bull (VII, ?).
Rule tested: a card's BLUE numeral equals the next card's RED numeral (domino). Result: a unique longest chain of 8 —
**ticket (VI,VI) → Feastables (VI,VIII) → chart (VIII,IX) → cloud (IX,V) → ribbon (V,VII) → flag+barn (VII,IV) → calendar-25 (IV,II) → elf (II,XI)** — every link matches, and the reverse rule gives the same chain reversed. That is far too clean to be chance: the cards are meant to be chained by matching numerals, which is exactly Colin's "solve the jigsaw first".
Gaps: the chain needs a card with red XI after elf, and the laughing face (X, XIV) needs a card with red XIV; the pink index also uses III and XVI which appear on no card seen. So at least 2–3 cards are unread (edge-on or hidden), and window (VII,I), owl/eagle (VII,IX), Oman (VI,V), Africa (IV,VIII), bull (VII,?) have not been placed — duplicate reds (VII×3, VI×2, IV×2) mean some of my colour/numeral reads are wrong or the pieces form more than one chain (Colin: "is there another entry point… there's three of them").
Next: (1) get exact numerals and colours for every card (frames 0:18, 5:36, 9:04, 12:45; `work/frames4k/piece_atlas*.png`, `cards_*.png`); (2) complete the chain(s); (3) extract letters — most likely the picture's word indexed by the linking numeral (SB8/OP1 style) — and test the result as the (3,6,4) phrase / XOR input.

### 16b. Corrected card reads from the community collage (`work/reddit/img/collage_*.png`)
Colours re-read at 5x: elf (red II, blue XI) · jail door [was "window"] (red VII, blue I) · falling chart (red VIII, blue IX) · ribbon (red V, blue VII) · Feastables bar (red VI, blue VIII) · snow cloud (red IX, blue V) · laughing face (red X, blue XIV) · calendar-25 (red II, blue IV) [previously reversed] · cassette/ticket (red VI, blue VI) · Oman flag (red VI, blue V) · Africa+pineapple (red IV, blue VIII) · US flag+barn (red VII, blue IV) · black animal silhouette (red VII, blue unseen) · owl/eagle (red VII?, blue IX?).
Edge shapes noted: chart has a semicircular notch on its right; elf a notch on its left; cloud a zigzag right edge and flag+barn a zigzag left edge (they mate); ribbon notch top-left; Feastables tab bottom-left; jail door is L-shaped; Africa card zigzag right; Oman card zigzag left.

### 16c. Chain re-test after the colour corrections, and a better structural hypothesis
- With corrected colours the pure domino rule (blue of one = red of next) no longer gives a unique chain: two competing 7-card chains, and reds contain VII×4 and VI×3, so numeral-matching is NOT how the pieces order. The physical tabs/notches order the pieces (Colin: "solve the jigsaw").
- Count match: 14 cards carry 14 red numerals; only 13 blue numerals are visible (the black-animal card shows red VII and no blue). The red desk note's source phrase is (5,2,7) = 14 letters; the blue note's is (3,6,4) = 13 letters. Hypothesis: each card's picture is a word; its RED numeral indexes a letter for the red (5,2,7) phrase and its BLUE numeral indexes a letter for the blue (3,6,4) phrase; the assembled jigsaw fixes the letter order. The colour split of the two desk notes (red ink / blue ink) matches. Then blue phrase + LAST WORD THEN NINTH → (6,6) → 6-letter final; red phrase + the unknown (8,3,5,4,4) instruction → 9-letter final.
- Picture words are still ambiguous (e.g. black silhouette may be Tasmania rather than a hedgehog; teal card may be a cassette rather than a ticket), which is why letter extraction has not been run to completion.

## 17. Community solution structure surfaced 2026-09-04/05 (r/MrBeast threads "Solution to the puzzle", "If we don't work together…", "Possibly at phase 3"; dumps `work/reddit/new_*.rss`) — UNVERIFIED, treat as data
Two posters (gg4999, HoldingAdvisory) claim the desk chart resolves as:
- Red pad: (5,2,7) = **BIRDS OF AMERICA** → the pink (number, Roman numeral) pairs are Audubon plate numbers (Birds of America has 435 plates; all pink numbers are ≤ 426) with the numeral indexing a letter of the bird's name → 24 letters → "Alphabetize" → strike MR → a 9-letter word they give as BEASTSAND.
- Blue pad: (3,6,4) = **XOR SUPERB OWLS** ("superb owl" = Super Bowl; Super Bowls carry Roman numerals; owls are Audubon plates) → (6,6) = **FOURTH UPLOAD** → LAST WORD THEN NINTH → a 6-letter final (one says STUNTS, one hints the join is "close to BEASTSANDUPLOAD"). Another poster (CiviledXI) says both sinks are still incomplete and points at the CyberChef link plus the remaining stickies.
- Consistency with our own work: 14 red numerals ↔ BIRDS OF AMERICA (14 letters) and 13 blue numerals ↔ XOR SUPERB OWLS (13 letters) exactly matches §16c. The community's picture words: Oman flag, twenty-fifth (calendar), Feastables chocolate bar (the teal card), rain cloud, brown square, Africa+plant, face with tears of joy, glasses (our "ribbon"), declining graph, American red barn, Christmas gnome (our "elf"), Egyptian hawk (our "owl/eagle"), white door (our "jail door").
- Colin replied "😆" to a Redditor's "I'm close to solving it" post; no winner announced as of 2026-09-05 morning; the sweepstakes page was redeployed (new deployment id) with identical content.
- Tested: 'SuperB-owLs' + any two digits fits the CyberChef placeholder mask exactly but XORs to junk for all 100 values, so the recipe input is not that literal string.

## 18. Red chain, computed (2026-09-05) — `work/audubon/havell_plates_pitt.json` holds all 435 Havell plate names (University of Pittsburgh index)
Structural confirmation: the pink note has **24** (plate, numeral) pairs and the red pad's second node is **(8,3,5,4,4) = 24 letters**. So the pink note is the extraction table for the red chain: BIRDS OF AMERICA → 24 letters → a 24-letter (8,3,5,4,4) instruction phrase → (with MR struck) → the 9-letter red final. The community's reading is consistent with this.
Plate names for the pink numbers (Audubon's Havell titles per Pitt): 29 Towhe Bunting · 39 Crested Titmouse · 42 Orchard Oriole · 61 Great Horned Owl · 74 Indigo Bird · 76 Virginian Partridge · 81 Fish Hawk or Osprey · 83 House Wren · 101 Raven · 102 Blue Jay · 112 Downy Woodpecker · 162 Zenaida Dove · 184 Mangrove Humming Bird · 216 Wood Ibiss · 225 Kildeer Plover · 235 Sooty Tern · 245 Thick-billed Murre · 246 Eider Duck · 253 Jager · 275 Noddy Tern · 329 Yellow-breasted Rail · 337 American Bittern · 358 Pine Grosbeak · 424 composite (1 Lazuli Finch, 2 Crimson-necked Bull-Finch, 3 Gray-crowned Linnet, 4 Cow-pen Bird, 5 Evening Grosbeak, 6 Brown Longspur) — so "424-6" most likely means plate 424, figure 6.
Extraction attempt (numeral-th letter of the Audubon title, spaces removed), plate order: `WEARRGR?AUDIRWEELC?DACBM`; ordered alphabetically by bird name ("Alphabetize?"): `CUEDCRR?MR?ERDABAELWGWAI` — note MR appears as an adjacent pair. Two indexes overflow (83 XI on House Wren; 253 XIV on Jager), which means the intended names are partly the MODERN names (Pomarine Jaeger is exactly 14 letters) or full titles; the extraction is therefore not yet clean. The unknown pieces are: exact name form per plate, whether spaces count, and the alphabetization key. Once those give a readable (8,3,5,4,4) sentence with "MR" in it, striking MR and applying the sentence yields the 9-letter red final.
Owl plates in the Havell list (for the blue chain "XOR SUPERB OWLS"): 46 Barred Owl · 61 Great Horned Owl · 97 Little Screech Owl · 121 Snowy Owl · 171 Barn Owl · 199 Little Owl · 351 Great Cinereous Owl · 378 Hawk Owl · 380 Tengmalm's Owl · 383 Long-eared Owl · 432 composite (Burrowing, Large-headed Burrowing, Little Night, Columbian, Short-eared). Note pink plate 61 is an owl and plate 81 is the Osprey (the "Seahawks?" sticky sits next to "081 XIV").

- Second extraction pass with MODERN common names (Eastern Towhee, Tufted Titmouse, …, Pomarine Jaeger, Chestnut-collared Longspur) and with Audubon titles, spaces kept or removed, sorted by plate / by modern name / by Audubon name: none yields a readable (8,3,5,4,4) sentence (e.g. modern+nospace+alpha-by-modern = `CUODIODS R.N ERTA. BREL DWLI`). Two indexes still overflow under either name set (83 XI and either 81 XIV or 253 XIV), so the intended reference is probably the full Audubon plate caption or the octavo-edition names, or the pink numbers are not Havell plate numbers. Table and code path: `work/audubon/`. This is the exact point where the red chain stalls; a human with Susanne Low's concordance (Audubon title ↔ modern name ↔ plate) could finish it in minutes.

## 19. Further tests (2026-09-05, "go on")
- Pink numbers as MrBeast upload indices (oldest-first, 999 uploads listed in `work/yt/mrbeast_uploads.txt`) with the Roman numeral as word/letter index → gibberish (`rkoVrtHrpweecIem…`). Rejected.
- Owl-plate ⊕ Super-Bowl-number arithmetic can only yield letters for plates 46 and 61, so "XOR SUPERB OWLS" is not a bitwise owl/Super-Bowl operation in that simple form.
- Phrase strings through the CyberChef key (XORSUPERBOWLS, Superb Owls, BirdsOfAmerica, FourthUpload, LastWordThenNinth, SuperBowl60…) → all junk.
- FOURTH UPLOAD check: MrBeast's fourth-ever upload (12 Jan 2013) is "More birds IN MINECRAFT!!" (`Y74b7WlcEpk`, a birds mod) — a striking thematic fit with BIRDS OF AMERICA, so the community's (66) reading may be right. Its title's last word MINECRAFT is 9 letters; transcript last word "watching", 9th word "Mod"; description is three lines with a link to upload #3. No 6-letter output yet. MrBeast2's fourth upload is "Unlimited Money Machine"; Colin's oldest uploads are the "140 - Mirror Level" walkthroughs.

## 20. Verified breakthroughs, 2026-09-05

Full reproducible account: `SOLUTION_PROGRESS.md`; script: `tools/solve_desk.py`.

- **Red terminal is FANTASTIC**, not BEASTSAND. Historical scientific-name
  indexing, A-Z ordering by original English plate titles, and the QX=TH sticky
  give **MRBEASTSANDWHERETOFINDTHEM** exactly. Q/X are the only missing title
  initials, filled with T/H. Original plate 81 fixes the concordance typo
  HAL LIAETUS -> HALIAETUS; plate 424 is sorted under Lazuli Finch but indexed
  using figure 6's Plectrophanes townsendi.
- **XOR case-mask rejection was wrong.** `SuperB-owLs14` gives
  `v=F0OkwXKcPSE`, a working YouTube URL suffix. The video is *Hi Me In 10 Years*.
- **Blue sticky mechanically decoded:** flatten `LSWRTENNHTINHDOTA`, read
  alternating left and right ends -> LASTWORDTHENNINTH. The linked video's last
  word FOURTH and ninth word UPLOAD produce the (6,6) intermediate.
- Owl pictures index scientific names, including five boobooks. Red letters
  reproduce BIRDSOFAMERICA; blue reproduces XORSUPERBOWLS except the African
  grass owl requires VII where previous visual reads had VIII. Physical tab
  order remains inferred from the messages.
- **Final six-letter answer not established.** 251634 remains unused.
  FANTASTIC HEDWIG is a candidate motivated by psolidgold's Reddit comment,
  not a full solve. No answer was submitted.

## 21. New checksum corroboration and corrected video labels, 2026-09-05

- A newly found CiviledXI post gives the SHA-256 of their claimed uppercase,
  space-separated answer:
  https://www.reddit.com/r/MrBeast/comments/1w7qx8b/6_and_9_letter_words_solved_for/
  `b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22`.
  **FANTASTIC HEDWIG matches exactly**, computed locally. Reproduce with
  `python3 tools/check_community_hash.py`. Reversed order and FANTASTIC
  UPLOAD/STUNTS do not match. This corroborates a community claim, not official
  correctness or a fully reproduced blue path. The user had already submitted
  FANTASTIC HEDWIG before this checksum was found.
- Fourth main-channel video scanned at 2 fps, 250 frames; generated OCR is
  `work/yt/mb4th_targeted_ocr.json`. Visually confirmed **Spawn Peahen**, not
  Pelican, at about 30.5 seconds (`mb4th_scan/frame_0062.jpg`). Correct hotbar
  order: Peacock, Bluebird, Peahen, Flamingo, Roadrunner, White Peacock.
- Straight 2,5,1,6,3,4 indexing of those names still gives EBPNAT. The numerical
  sticky remains unexplained. Rank-key interpretation (BRAZIL, CHANCE, FRESNO,
  etc.) and dictionary anagrams do not uniquely identify a terminal.
- The fourth video's description leads to the older Boxy mod video and then a
  PlanetMinecraft mod page, not an explicit puzzle instruction. The gateway
  transcript contains UPLOAD only once, ruling out its fourth occurrence there.

## 22. Further blue-source checks, 2026-09-05 ("think more")

No new terminal derivation. Added fourth-newest main/MrBeast 2 captions and
descriptions (`fourth_latest_*`), checked DoctorXOR Shorts (one result only),
and checked *Premature Baldness* as a speculative fourth-ever YouTube upload
(`yt_fourth_ever.*`). Targeted direct/inverse 251634 indexing and acrostic tests
on seven videos' caption words/cue endpoints found no HEDWIG match; results are
in `work/yt/blue_key_text_tests.json`. This is limited to those models and
imperfect caption data, not an exhaustive rejection of the videos.

Re-viewed the partly covered silhouette sheet beside the blue pad and compared
it with PDF page 35. It does not look like the old birds-on-a-wire alphabet;
it has not been identified or decoded. Full content and symbol count are not
visible. See `SOLUTION_PROGRESS.md` section 5 for scope and remaining gaps.

## 23. Original-video reinspection: mask count corrected, 2026-09-05

The earlier 16-asterisk count was wrong. Fresh 10-fps sampling of the original
4K video shows 15 asterisks in the completed entry at approximately 17:26.5-
17:26.9, immediately before the cut to SUBMIT. Five frames agree at three
brightness thresholds and by visual inspection. Reproduce with
`python3 tools/count_submission_mask.py`; see `VIDEO_AUDIT.md` and the numbered
crop `work/video_audit/mask_15_numbered.png`.

This makes the 15-character FANTASTICHEDWIG a reasonable format variant if the
user's earlier entry contained a space. The animation does not prove the
answer or the server's matching behavior. 251634 remains unsolved.

Other targeted desk/ending crops revealed no new legible extraction. The
partly covered silhouette sheet remains unidentified. Obscured handwriting
under the US/barn card appears to include JULY and a lower JU fragment, but
the rest cannot be read reliably and no inference is established.

## 24. Broader fourth-upload and rail-fence tests, 2026-09-05 ("try again")

This pass was previously recorded in `SOLUTION_PROGRESS.md` section 7 and is
included here so the chronological log covers the work too. No new terminal
was derived.

### Six linked channels

Hypothesis: the six channel links in the original description supply six
fourth uploads, with 251634 ordering or indexing them. The numerical fit is
only a hypothesis; no clue explicitly instructs this channel collection.

Main/MrBeast 2 fourth-upload metadata was already cached. The other four
public full-video tabs were fetched and saved as `work/yt/channel_fourths.tsv`
(473 entries total). Their fourth-oldest and fourth-newest metadata,
descriptions, and available English captions are in `work/yt/channel4_*`.

| Channel | Fourth oldest public full video | Fourth newest in cached list |
|---|---|---|
| MrBeast Gaming | CSSsPVweLkc, Last to Survive Random Blocks wins $10,000 - Challenge | nH9R0Jpqeqc, 10 YouTubers vs 2 Secret Traitors |
| Beast Reacts | 67MptG3oS-A, Super Satisfying Kinetic Sand DIY | 1atCTSRJHH0, Rarest Things On Earth! |
| Beast Philanthropy | nl79pan4h6U, Giving Away 50,000 Cookies! | O6wTcrhkw4o, Rescuing Child Slaves in Africa |
| Beast Animations | sKqFzjkiwF8, MrBeast Lab - Ep 3: Swarmbies | vA6en6pzhwk, MrBeast Lab - Ep 8: Banana Blaster to the Rescue! |

- Tested title initials, last/fourth title-word initials, first/ninth/last
  spoken-word initials, and indexed title letters, with direct and inverse
  251634 orders. No demonstrated answer extraction.
- The Beast Reacts fourth-oldest video mentions Harry Potter around 7:35-7:50,
  but discusses a winged tennis ball and Quidditch, not an explicit Hedwig clue.
- Captions were stripped of tags and rolling overlaps. ASR wording and word
  boundaries remain limitations. These checks are not full visual/audio reviews.
- Current public upload order is not necessarily historical upload order:
  deleted/private videos are unavailable, and newest-first rank can change.
  The fourth-newest rank at the puzzle's September 2 release was not verified.

### Does 251634 belong in the earlier fence step?

- Tested standard zigzag rail counts 2-17, phase offsets, normal/reversed rail
  orders and reading directions, plus keyed six-rail permutations with all
  independent rail-reading directions.
- None of **2,408** tested configurations encodes LASTWORDTHENNINTH as
  LSWRTENNHTINHDOTA. This excludes those models, not every possible route cipher.
- Positive control: `plain[::2] + plain[1::2][::-1]` exactly reproduces the
  sticky. This known construction still does not use 251634.
- Script: `python3 tools/test_blue_alternatives.py`.
  Results: `work/yt/blue_alternative_results.json`.

## 25. Author errata and renewed source checks, 2026-09-06

### Confirmed author corrections

Primary source, accessed September 6:
https://www.reddit.com/user/DoctorXOR/comments/1w89jup/comment/p840oup/

DoctorXOR says the grass jigsaw piece contains one extra blue I, and the red
paper on the desk is missing a 2. He explicitly says neither is intentional.

- African grass owl: the visible VIII is corrected to VII. Index 7 of
  TYTOCAPENSIS is P, resolving the mismatch in XORSUPERBOWLS.
- Red enumeration: the visible (8,3,5,4,4) is corrected to (8,3,5,2,4,4),
  matching MRBEASTS AND WHERE TO FIND THEM. QX=TH still supplies the two
  absent alphabetical slots; the missing 2 is an enumeration error, not an
  instruction to remove two letters.
- This supersedes the earlier unresolved-discrepancy warnings. It supports
  the existing red and XOR derivations, not the missing HEDWIG step.

### What no response does and does not mean

In the same parent post, DoctorXOR explains that Team Beast checks entries and
announces a winner. He designed the puzzle but does not know the contest's
administrative status and will not confirm submitted answers.

- Silence does not establish acceptance, rejection, eligibility, or who was
  first. His examples of possible delays are possibilities, not status updates.
- The official entry page was still accessible when checked:
  https://puzzle-video-sweepstakes.mrbeast.app/
  That does not establish the prize is unclaimed.
- No official winner announcement was located in the sources inspected this
  pass. This is a limited search result, not proof that no announcement exists.
- The user reports already submitting the candidate. No entries, emails,
  public comments, or messages to the organizers were sent by the assistant.

### Community checks: evidence versus repetition

- Rechecked CiviledXI's checksum post and recent puzzle discussions. The hash
  agreement in section 21 remains corroboration of that poster's claim, not
  official verification or a substitute for an extraction.
- A new reply states that the fourth-upload step did not involve transcripts:
  https://www.reddit.com/r/MrBeast/comments/1w7yi43/anyone_got_a_clue_on_this_latest_puzzle/
  The reply supplies no mechanism. Treat this as an unverified solver lead,
  not a puzzle-author hint. The parent write-up's MRBEASTSAND/VIDEO IS route
  is not a reproduced solution, even though it names FANTASTIC HEDWIG.
- CiviledXI described the 7:46/Golden Gate Bridge/Golden Bird route as a wrong
  interpretation. Do not promote that account into a new extraction hint.
- Searches for the diagnostic strings DHIGEW and EIHGDW found no relevant
  source. An unrelated OCR-text match was not treated as evidence.
- Direct Reddit JSON and RSS fetches for thread 1w7yi43 both returned HTTP
  403. Files `work/yt/reddit_latest_puzzle_sep6.json` and `.rss` contain error
  responses, not usable discussion snapshots. Browser/search text supplied
  the public comments inspected here. Do not mistake file extensions for
  successful structured data downloads.

### Fresh visual checks

- Refetched the fourth-oldest MrBeast and DoctorXOR thumbnails and metadata:
  `work/yt/fourth_thumb_Y74b7WlcEpk.{jpg,info.json}` and
  `work/yt/fourth_thumb_2asPmHvlkWM.{webp,info.json}`.
- MrBeast's thumbnail shows the Minecraft bird cage and six occupied hotbar
  slots. DoctorXOR's shows a geometric scene from 140. Neither yielded an
  explicit new code. Metadata for More birds IN MINECRAFT!! has no chapters
  and retains the previously inspected Boxy-mod description link.
- Re-viewed `work/yt/mb4th_sheet.jpg` and selected full frames, including
  `mb4th_scan/frame_0170.jpg` and `frame_0185.jpg`. The nearby display board
  is visible, but no new readable extraction was established from those views.
- Re-viewed the original-video silhouette crop at
  `/tmp/mrbeast_silhouettes_upright.png`. At least five winged shapes are
  visible; the partly covered sheet's full contents, orientation, symbol count,
  and relevance are still unknown. Do not assume six symbols or assign bird
  names to force HEDWIG. The temporary crop may not persist across sessions;
  original desk frames remain under `work/frames4k/desk765/`.
- No fresh direct audio listening or complete visual review of DoctorXOR's
  fourth-oldest video was performed in this pass. Earlier caption/OCR work
  must not be described as those checks.

## 26. Lessons and the remaining gap

- **Use derived evidence to constrain guesses.** FANTASTIC is an independently
  reproduced answer. HEDWIG is a checksum-corroborated candidate. They do not
  have the same evidential status.
- **Validate outputs in context.** Earlier code rejected SuperB-owLs14 because
  its XOR output was not ordinary prose; `v=F0OkwXKcPSE` is a valid URL suffix.
  The nearby YouTube sticky supplies that context.
- **Preserve contradictions until resolved.** VII and the red enumeration
  initially required caveats. The author's September 6 correction now resolves
  both; neither should continue generating speculative extra layers.
- **Read actual labels.** Peahen, not Pelican, is visible in the Minecraft
  source. The corrected name still does not solve the indexing attempt.
- **Name the scope of negative tests.** Caption extraction, sparse OCR,
  thumbnails, and contact sheets are distinct checks, not proof that a video
  contains no further clue. Public upload ranks also have historical limits.
- **Do not force six letters from six digits.** 251634 can be a permutation or
  index list, but neither role has been established. If it is a direct reading
  order producing HEDWIG, the source must be DHIGEW; under the inverse
  convention the diagnostic source is EIHGDW. Neither has been located.
- **Separate solver agreement from correctness.** Reposted guesses may share
  a source. The 15-star edited form animation is also not server validation.
- **Current missing link:** explain FOURTH UPLOAD plus the unused blue 251634
  sticky with a reproducible six-letter extraction. Do not report the puzzle
  as independently solved until that link, or an official solution, exists.

## 27. Research from Colin's perspective, 2026-09-06

The user asked whether Colin had authored or solved something similar before.
This pass found a directly credited older puzzle and useful comments about his
design preferences, but no source identifying the missing blue mechanism.

### A verified puzzle he authored

The 2019 Cryptex magazine's printed pages 24-25 contain *Which Prexcyt Dragon
Are You?*, explicitly credited "Created by DoctorXor". Its questionnaire hides
five groups of references. Identify each group's common theme and associated
number, index the indicated words to produce MOTTO, then use a separate
Pythagorean clue to finish with ALL IS NUMBER. This is an actual precedent for
reference identification, numerical extraction, and a final clue-driven step.

Primary material and official explanation:
- https://cryptexhunt.com/2019/mag.pdf
- https://cryptexhunt.com/2019/CH2019%20Solution%20Guide.pdf (page 19)
- Cached as `work/colin/cryptex2019_mag.pdf` and `cryptex2019_solutions.pdf`,
  with corresponding `.txt` files. The magazine's password, LOCKBOX, is
  publicly supplied in the official solution guide, page 3.

**Inference for this puzzle:** a terminal should have an identifiable source,
an extraction rule, and an ordering rule. The precedent supports looking for
a concrete role for 251634; it does not tell us which video or six objects to
use. It also does not establish a mandatory extra stage after FANTASTIC HEDWIG.

### His own stated preferences

In his May 19 Salesforce interview, Colin describes liking minimalist visual
puzzles with sound internal logic, and disliking fragile associations and
excessive red herrings. He also describes keeping a complete clue inventory
and returning to a previously recorded photo clue when the old hunt stalled.
These are useful solving habits, not new contest instructions:
https://www.salesforce.com/news/stories/how-colin-sanders-solved-mr-beast-puzzle/

The interview credits the million-dollar hunt to Lone Shark Games. Its solution
book documents puzzles Colin solved, not a catalogue of puzzles he authored.
Likewise, the Jack Lance and mezzacotta examples he praises are other authors'
work. The linked mezzacotta PDF could not be fetched by the web tool this pass;
no comparison with its actual mechanism was made.

### A previously underused stream passage

Re-read `work/twitch/thursday.txt` around 2490-2577 seconds (41:30-42:57), from
https://www.twitch.tv/videos/2864667604?t=00h41m30s

In the existing Whisper transcript, Colin says he made the $10k puzzle himself
and describes discovering interesting connections while constructing puzzles.
He characterizes some such connections as things he stumbled upon. This is
not the same as the production-error errata and is not an extraction hint.
The wording is machine-transcribed; no fresh direct audio review was performed.

**Inference:** an older video might supply an existing pattern that he built
around. That is a reason to inspect its actual content, not proof that the
Minecraft fourth upload or any specific pattern is intended.

Also re-read the 1491-1541-second AI passage. The earlier section 14 summary
overstated it: his familiar-mechanics discussion does not specifically confirm
reuse of an old puzzle in this challenge. Corrected that summary above.

### Other author-history checks and limits

- Rankk credits him with *Dice Where?*, *Arckeyologist*, and *Master
  Arckeyologist*. Retrieved titles/credits, not their puzzle mechanics:
  https://www.rankk.org/contributors.py
  https://www.rankk.org/user/DoctorXOR
  These titles alone do not justify a dice, archive, or keyboard interpretation.
- The 2019 Cryptex site lists him as a contributor; the 2020 site lists him as
  a tester. The 2025 page's embedded shared people data includes his biography,
  but its active Designers list does not include him. Do not infer 2025 puzzle
  authorship merely from that search snippet.
- His GitHub profile showed zero public repositories. Paradox Puzzlehunt's
  about page did not identify him as an author. His stream describes solving
  Paradox puzzles, consistent with the videos being solve-throughs.
- Fresh community searches still repeated FANTASTIC HEDWIG and speculation
  about another stage, without a newly reproducible 251634 extraction. Neither
  repeated agreement nor frustration at no response establishes correctness.

## 28. New visual coverage and Shorts alternatives, 2026-09-06

### DoctorXOR's fourth-oldest public video

Downloaded `2asPmHvlkWM`, *140 - Mirror Level 3 Walkthrough (No deaths)*,
which earlier passes had checked mainly through metadata/captions/comments.
Video: `work/yt/xor_fourth_video.mp4`.
Contact sheet: `work/yt/xor_fourth_sheet.jpg`, sampled every 10 seconds.

The sampled frames show geometric platforming and a rotating-square boss
sequence, not an explicit letter message or a demonstrated 251634 extraction.
This closes a sparse visual-coverage gap, not a full frame-by-frame or audio
analysis. No terminal was found.

### Main-channel Shorts, a previously incomplete scope

Fetched the public Shorts tabs separately: 198 results for MrBeast and 200
for MrBeast 2. Listing: `work/yt/main_shorts_sep6.tsv`. These are current public
rankings, not proof of historical rank at the puzzle's release.

| Channel and rank | ID | Title | Upload date |
|---|---|---|---|
| MrBeast, fourth oldest Short | se50viFJ0AQ | Would You Fly To Paris For A Baguette? | 2022-12-08 |
| MrBeast, fourth newest Short | Df5Y-2ndQyU | Read My Book, You Could Win $1,000,000 | 2026-07-17 |
| MrBeast 2, fourth oldest Short | wdznN3-h_5Y | Launching a $40,000 Firework! | 2020-09-11 |
| MrBeast 2, fourth newest Short | KDAlh2S4SfM | Can You Spot the Chocolate Object? | 2026-08-10 |

Downloaded all four videos, metadata, descriptions, thumbnails and available
English auto-captions. Files: `work/yt/short4_*`; full videos use
`short4_video_ID.mp4`; contact sheets use `short4_sheet_ID.jpg` and sample
every two seconds. Visually inspected all four contact sheets.

- The chocolate-object Short was a concrete object-identification lead. It
  shows a small set of stationery and a chocolate imitation of a board eraser;
  no justified six-item/index pairing or HEDWIG extraction was established.
- The other sheets show the Paris trip, a firework display, and promotion of
  the separate James Patterson book contest. No visible new code or explicit
  instruction using 251634 was found in these sampled views.
- The separate book-contest promotion is not evidence that buying the novel
  is required for the $10k video puzzle. No purchase or entry was made.
- Sparse sampling can miss brief content. These checks do not rule out every
  visual/audio method, but they do not justify recommending another answer.

### Result of this pass

The author's past work provides a concrete comparison, not a solved blue step.
FANTASTIC remains reproduced; HEDWIG remains checksum-corroborated rather than
independently extracted. The next successful step must connect FOURTH UPLOAD
and 251634 to a specific source and an unambiguous six-letter result.

## 29. Focused 251634 audit, 2026-09-06

The user agreed to focus on the unused number and the fourth-upload source.
This pass did not identify a new answer. It tightened the literal evidence
and separated two different meanings of the permutation.

### Number and visual source

- Reinspected `work/frames4k/desk765/c_case_stickies.png` and the full
  `d_765.png`. The blue sticky reads one uninterrupted 251634, without
  visible colons, decimal points, separators, or arrows. A timestamp reading
  would require supplying punctuation not shown on the sticky.
- Rechecked the six hotbar labels in MrBeast's fourth-oldest currently public
  main-channel video, https://www.youtube.com/watch?v=Y74b7WlcEpk.
  Preserved a readable label-and-hotbar comparison in
  `work/yt/blue_251634_audit/spawn_labels.jpg`.
- The nearby pond-side display at about 93.5 seconds is a 3-by-5 grid of
  apparently empty item frames, not a located six-symbol message. Reference:
  `work/yt/mb4th_scan/frame_0188.jpg`. The inventory views around 54 and 95
  seconds have nine occupied ordinary-item slots as well as the six spawn
  slots; they are not a second obvious group of exactly six labelled items.

| Hotbar slot | Literal spawn name | Reference time |
|---|---|---|
| 1 | Peacock | 20.0 s |
| 2 | Bluebird | 26.0 s |
| 3 | Peahen | 30.5 s |
| 4 | Flamingo | 33.0 s |
| 5 | Roadrunner | 39.0 s |
| 6 | White Peacock | 48.5 s |

These times identify inspected frames, not exact first-spawn timestamps.
No fresh direct audio listening was performed.

### Reproducible tests, without selecting a desired output

Added `tools/audit_blue_251634.py`. Run:

```sh
python3 tools/audit_blue_251634.py
```

The script saves the evidence sheet and `work/yt/blue_251634_audit/results.json`.
It tests 120 literal-label models: names with/without the Spawn prefix;
hotbar, reverse, alphabetical, key-reading and key-destination orders;
key/inverse/position/first/fourth/ninth character indexes; counting from either
end. It also tests 28 single-source models on FOURTH UPLOAD, its component
words, the video title and its last word, and the two prose description lines.

No output matched a six-letter entry in the installed American/British
dictionaries. Some of these models overlap earlier tests; the contribution
is an explicit bounded inventory and reproducible record, not 148 wholly new
ideas. These dictionaries are a filter, not an answer oracle. Proper names,
untried mechanisms and different sources are not excluded by this result.

Examples, removing spaces and using one-based indexes:
- Hotbar names, indexed with 251634: EBPNAT, reproducing the earlier result.
- Title letters, indexed with 251634: OBMIRE.
- UPLOAD, indexed with 251634: PAUDLO. This is only a rearrangement, not a
  derived reason to submit UPLOAD or another anagram.

### Target-dependent diagnostic: ordering is not extraction

Separately checked the already-proposed HEDWIG against these literal names.
This is a constraint test, explicitly not an independent solution:

- Reading slots 2,5,1,6,3,4 gives Bluebird, Roadrunner, Peacock, White Peacock,
  Peahen, Flamingo. HEDWIG is impossible by selecting one literal letter per
  name in this order: Bluebird has no H, Peacock has no D, and Peahen no I.
- Assigning destination labels 2,5,1,6,3,4 to the original slots instead gives
  reading order 3,1,5,6,2,4. HEDWIG can then be forced by picking character
  positions 4,2,4,1,6,7 respectively. In original hotbar order the required
  indexes are 2,6,4,7,4,1, producing EIHGDW before rearrangement.
- No clue supplying those indexes has been found. This demonstrates why a
  possible rearrangement is not enough, while avoiding the overly broad
  claim that the six names could never supply the candidate under any rule.

### Research checks and limitations

Located the Exotic Birds mod author's own documentation:
- https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1282698-exotic-birds-herons-owls-pelicans-and-more
- https://www.planetminecraft.com/mod/exotic-birds/

The forum description says its Book of Birds contains scientific names, but
the retrieved description was last edited in 2020, and the PlanetMinecraft
page describes a 2016 update. Neither is a verified snapshot of the 2013
version in MrBeast's video. No book is visibly consulted in the inspected
video frames. Consequently no arbitrary six-species Latin-name list was
treated as confirmed input or added to the literal-label tests. A scientific
name continuation remains unproved, not newly eliminated.

Fresh public searches and the accessible solver posts did not supply a
reproducible 251634 step. Profile/comment fetches exposed differing cached
snapshots, so they are not an exhaustive or real-time community survey.
No submissions or messages to other solvers/organizers were made.

**Result:** FANTASTIC remains independently reproduced. HEDWIG retains the
earlier community-checksum corroboration, but this pass does not validate it
or justify recommending an additional guess. The missing information is the
actual extraction rule/source, not merely a nicer-looking anagram.

## 30. Consolidated review dossier, 2026-09-07

The user asked for a standalone packet that can be handed to another model with the
question "are we missing anything?". This pass produced no new answer. It audited the
existing record, re-verified every load-bearing claim against the cached evidence,
and found several documentation errors, listed below.

### New deliverables

| File | Contents |
|---|---|
| `LLM_REVIEW_PACKET.md` | Self-contained master dossier, 15 sections, ~79 KB. Includes the ready-to-use reviewer prompt, all clue transcriptions, both extraction tables in full, the reproducible derivations, the fourth-upload candidate table with honest per-video coverage, the complete test register, a corrections table, and 14 prioritised reviewer questions. |
| `LLM_REVIEW_PACKET.docx` / `.pdf` | Same content, 37 pages, with the twelve clue images embedded and captioned. Built by a script kept in the session scratchpad; regenerate by re-running the docx builder then `libreoffice --headless --convert-to pdf`. |
| `REVIEW_PROMPT.txt` | Section 0's reviewer prompt on its own, for pasting as the chat message alongside the uploaded dossier. |
| `dossier_images/` | Twelve clue images at readable sizes, sourced from `work/frames4k/`, `work/reddit/img/r02.png`, `work/video_audit/` and `work/yt/blue_251634_audit/`. |
| `LLM_REVIEW_EVIDENCE.zip` | 2.1 MB, 40 files: the dossier, all images, all nine scripts, the small result JSONs, the gateway captions, the Audubon concordance and plate index, the channel/Shorts snapshots, the Twitch transcript and the contest rules. Excludes the ~6 GB of video, audio and 4K frames; section 14.4 of the dossier lists every omission and how to re-obtain it. |
| `tools/verify_dossier.py` | Parses the dossier's own markdown tables and re-checks them against the cached source data: 14 owl rows, all 26 Audubon rows against the concordance and the pink numerals, four enumerations, the sticky decode, the placeholder mask, the XOR, the SHA-256, four test-count claims, and the image references. Exits non-zero on mismatch. **0 failures on 2026-09-07.** |

### Verification performed this pass

- Re-ran `solve_desk.py`, `check_community_hash.py`, `count_submission_mask.py`. All
  reproduce their documented outputs.
- Independently recomputed the owl index table from the scientific names: red spells
  BIRDSOFAMERICA, blue spells XORSUPERBOWLS, with the author-corrected VII on the grass piece.
- Independently recomputed the A-Z Audubon extraction: MRBEASTSANDWHERETOFINDTHEM.
- Confirmed plate 424's six concordance rows are in figure order with *Plectrophanes
  townsendi* sixth, so "424-6 XVI" is well defined.
- Confirmed the placeholder mask `AaaaaA-aaAa##` accepts `SuperB-owLs14` exactly.
- Read the pink note, case stickies, both pads, monitor stickies, the "Boo! Five of these"
  poster and the wall boxes directly from the cached images rather than trusting the notes.
- Summed the caption-test JSON: 81,781 tests across seven videos, 0 matches.

### Documentation errors found and fixed in the dossier

1. **The 24-pair / 24-letter "structural confirmation" in section 18 is superseded.** With the
   author's corrected (8,3,5,2,4,4) the instruction phrase is **26** letters: 24 from the pink
   plates plus the two supplied by QX=TH. The old coincidence was an artefact of the missing 2.
2. **The blue monitor sticky's subtitle.** Sections 8/9e and `HANDOFF.md` say "bird food?".
   The community collage reads "bird **Fence**?", which is thematically coherent. Our own 4K
   crop is not decisive at any zoom. Recorded as uncertain in the dossier; it does not affect
   the decode.
3. **The psolidgold Hedwig comment has no local archive.** `work/reddit/` holds 13 thread
   dumps; thread `1w62u79` is not among them, and a full-text search of every cached file finds
   "Hedwig" only in a later post title and a search feed. The pun's provenance is a browser read,
   not a cached source. The dossier states this explicitly.
4. **The six case stickies alternate by chain, not just by colour.** Three yellow stickies in
   red ink serve the red chain (081 XIV Seahawks?, QX=TH, PLATES); three blue stickies in blue
   ink serve the blue chain (## How many?, 251634, YouTube link.. watch?). Two of the three blue
   clues are consumed, which sharpens the gap: **251634 is the only clue on either side of the
   puzzle with no role.**
5. **The `## How many?` sticky is the source of the `14`** in `SuperB-owLs14`. This was implicit
   in `SOLUTION_PROGRESS.md`; it is now stated.

### One new bounded test

The flowchart's `(66) -> (6)` implies a reduction acting on twelve letters, so sixteen
combination models on FOURTH/UPLOAD that earlier passes had not covered were run: alternating
letters between the words, `FOURTHUPLOAD` and `UPLOADFOURTH` with key and inverse-key indexes
and a +6 offset, and interleave-then-index. Outputs include OTFHUR, UFTHOR, OAFDUO, PTUHLR,
UUTDOO, LFAHPR, UUFLOP. **No dictionary word.** This confirms the gap is real rather than an
artefact of untried combinations, and it is recorded in dossier section 6.4.

### New observation offered to the reviewer, not a lead

Both words extracted from the gateway video sit inside date/scheduling language: the ninth word
comes from "I'm gonna **schedule upload** this video" and the last word from "this is October
**fourth**". Whether `FOURTH UPLOAD` means an ordinal position or a date has never been tested
as a fork. One community solver noted the same ambiguity in passing without pursuing it.
This is speculation and is labelled as such in the dossier.

**No answer was derived, no entry was submitted, and nobody was contacted.**

## 31. DoctorXOR channel refresh, 2026-09-08

The user supplied https://www.youtube.com/@doctorxor. This is the same channel
already investigated in sections 27-28, not a newly identified alternative
account. A fresh public metadata check found additional description links worth
preserving, but no new upload or independently derived blue answer.

### Upload comparison

- The Videos tab still returns **21 videos**, with exactly the same video IDs
  **in the same order** as `work/yt/doctorxor_uploads.txt`.
- The Shorts tab returns the same single Short, `NNuMfu0nr7M`, titled
  *Is This Paradox Puzzlehunt?*.
- Fourth-oldest remains `2asPmHvlkWM`, *140 - Mirror Level 3 Walkthrough
  (No deaths)*. Fourth-newest remains `IU89_plbom0`, the *Order of the Sinking
  Star* demo. Earlier inspection limits still apply: the former had sampled
  visual coverage, the latter metadata/caption coverage, not a full visual audit.
- Two titles differ from the old flat upload list. `XCOkRKUe3Nc` now reads
  *I Solved MrBeast's $1,000,000 Puzzle*, previously *How to Solve a $1,000,000
  Puzzle*. `IU89_plbom0` now reads *How to Accidentally Win a Puzzle Duel -
  Order of the Sinking Star (Demo)*, previously *Will This Be the Greatest
  Puzzle Game Ever? - Order of the Sinking Star (Demo)*.
- **Do not date both title changes to this pass.** The separately cached
  `xor_fourth_latest.info.json` already contains the latter title. Its title,
  description, date and duration exactly match the fresh per-video metadata.
  A difference from an older listing is not evidence of a new puzzle signal.
- `aFo8P073eSY` (*The Ramblings of a Million Dollar Winner*) has the same
  description, title, date and duration as `ramblings.info.json`.

### Additional links in the walkthrough description

The current description of https://www.youtube.com/watch?v=XCOkRKUe3Nc differs
from `work/yt/colin.info.json`: it adds thanks to 40 teammates and links to the
MrBeast2 puzzle video, the old hunt's official solution PDF, a published Google
Sheet, and a podcast interview. The exact edit time is not established. These
links are additions relative to our cached description, not proof the linked
material itself is new.

1. **Colin's working spreadsheet:**
   https://docs.google.com/spreadsheets/d/e/2PACX-1vSjNm2FMKSHMJd6P0S68ThM3oxZHuY-TMNgQJiIXkXKMgBFXfpX9Rv_uV-OP3UQT01qsOMJWChh_wTP/pubhtml
   The document is titled *MrBeast/Salesforce Super Bowl Puzzle*. Its published
   index lists Phase 0, Phase 1, grid, and numbered puzzle tabs. This pass read
   **only the index, Phase 0 and #4**, not every sheet. Phase 0 contains the
   known nine-word location instruction. Its fourth row is Experiences ->
   **TOWARDS**. Tab #4 shows the street-intersection/city-grouping solution
   producing TOWARDS. This is primary corroboration of the already recorded
   old-playlist route, not a new six-letter extraction. It does not establish
   that FOURTH UPLOAD means the fourth entry of that old playlist.

2. **Hello, Puzzlers! interview:**
   https://www.iheart.com/podcast/1119-hello-puzzlers-114688861/episode/behind-the-scenes-on-a-worldwide-1-million-puzzle-340335517/
   The episode page dates *Behind the Scenes on a Worldwide $1 Million Puzzle*
   to **August 5, 2026**, with a displayed duration of 58 minutes. Its description
   says A.J. interviews designer Mike Selinker and is later joined by the
   winner. It concerns the earlier million-dollar hunt and predates the
   September 2 launch of this $10,000 puzzle. **Only the episode page was
   inspected; no audio listening or full transcript review occurred.** It is
   a potential source on Colin's solving approach, not evidence that he
   disclosed this puzzle's final step there.

The original walkthrough's "Riddle #1" description paragraph was already in
the cached metadata and earlier notes; it is not a newly discovered clue.

### Saved evidence and limits

- `work/yt/doctorxor_sep8_DoctorXOR - Videos.txt` and
  `work/yt/doctorxor_sep8_DoctorXOR - Shorts.txt`: current ordered ID/title lists.
- Matching `.info.json` files: channel/tab metadata. These playlist metadata
  files do not contain the entry lists; use the text snapshots for comparisons.
- `work/yt/doctorxor_sep8_{XCOkRKUe3Nc,aFo8P073eSY,IU89_plbom0}.info.json`
  and matching `.description` files: fresh per-video metadata and descriptions.
- `work/yt/doctorxor_sep8_phase0_sheet.html`: the spreadsheet's published index,
  despite the initial filename. `doctorxor_sep8_sheet_phase0.html` and
  `doctorxor_sep8_sheet_puzzle4.html` contain the two inspected sheet bodies.
- `work/yt/doctorxor_sep8_podcast.html`: the episode page, not a transcript.
- These are current public listings, not a reconstruction of channel order on
  launch day. Deleted, unlisted, private, and separate live-stream uploads are
  not covered by the Videos/Shorts comparison. No new comments audit occurred.
- The September 7 review packet and evidence ZIP remain dated snapshots; they
  have not been regenerated to include this addendum.

**Result:** The new description links improve source coverage but supply no
reproducible role for **251634**. FANTASTIC remains independently solved;
HEDWIG remains a community-checksum-corroborated candidate with the final
derivation missing. No additional submission is justified by this pass.
No entry was submitted and nobody was contacted.
