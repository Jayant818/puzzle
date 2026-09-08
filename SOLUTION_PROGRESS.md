# Verified progress, 2026-09-06

## Status

The nine-letter red answer is **FANTASTIC**. The blue path is independently
verified through **FOURTH UPLOAD**, but its final six-letter result is not solved.
**FANTASTIC HEDWIG now matches a publicly posted solver checksum exactly.**
This corroborates the candidate, but is neither official contest confirmation
nor an independently derived blue terminal. The user reports submitting it;
the assistant has not submitted any entries.

**Author update, September 6:** the two earlier discrepancies are now explained
by confirmed production errors. The grass piece has one extra blue I, and
the red paper is missing a 2. See section 8 and the primary-source permalink.
The final blue extraction remains unresolved despite those corrections.

**Video audit correction:** the final typing animation shows **15 asterisks**,
not 16 as older notes claimed. This is consistent with FANTASTICHEDWIG without
a space, but an edited demo is not proof of answer length or server matching.
See `VIDEO_AUDIT.md` and `work/video_audit/mask_15_numbered.png`.

### New corroboration: public SHA-256 commitment

On September 5, CiviledXI posted a SHA-256 hash of their claimed two-word
solution, specifying uppercase words separated by a space:
https://www.reddit.com/r/MrBeast/comments/1w7qx8b/6_and_9_letter_words_solved_for/

```text
FANTASTIC HEDWIG
b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22
```

Locally hashing the exact phrase reproduces the entire posted hash. Reproduce
with `python3 tools/check_community_hash.py`. The reversed order, FANTASTIC
UPLOAD, and FANTASTIC STUNTS do not match. This establishes agreement with that
post's claimed answer and formatting, not independence of the solver's work,
the contest's matching rules, or whether the prize has been won.

Run `python3 tools/solve_desk.py` to reproduce the red extraction, blue sticky,
XOR URL, and gateway-caption extraction. This requires the cached concordance,
captions, and the already-installed `lxml` package.

## 1. Owl jigsaw

The pictures indicate owl species, and the Roman numerals index their scientific
names with spaces removed. The five boobooks explain "Boo! Five of these."
The following order is inferred from the messages, not independently established
by physically assembling the tabs:

| Picture | Owl | Scientific name | Red | Blue |
|---|---|---|---|---|
| Oman | Omani owl | Strix butleri | VI: B | V: X |
| December 25 | Christmas boobook | Ninox natalis | II: I | IV: O |
| Chocolate | Chocolate boobook | Ninox randi | VI: R | VI: R |
| Snow | Snowy owl | Bubo scandiacus | IX: D | V: S |
| Brown square | Brown boobook | Ninox scutulata | VI: S | VIII: U |
| Africa and grass | African grass owl | Tyto capensis | IV: O | VII: P, author-corrected |
| Laughing face | Laughing owl | Ninox albifacies | X: F | XIV: E |
| Spectacles | Spectacled owl | Pulsatrix perspicillata | V: A | VII: R |
| Smallest bar | Least boobook | Ninox sumbaensis | VIII: M | IX: B |
| Tasmania | Tasmanian boobook | Ninox leucopsis | VII: E | None |
| US flag and barn | American barn owl | Tyto furcata | VII: R | IV: O |
| Elf | Elf owl | Micrathene whitneyi | II: I | XI: W |
| Pharaoh | Pharaoh eagle-owl | Bubo ascalaphus | VII: C | IX: L |
| Barred door | Barred owl | Strix varia | VII: A | I: S |

Outputs: **BIRDS OF AMERICA** and **XOR SUPERB OWLS**.
The grass piece visibly shows VIII, which would give E. On September 6 the
author confirmed that its extra blue I is a mistake, resolving the earlier
discrepancy: the intended VII gives P. See the source in section 8.

## 2. Red: FANTASTIC

The pink numbers refer to plates in Audubon's *The Birds of America*. Index the
historical scientific name, but order by the initial of the old English plate
title. These initials cover A-Z except Q and X. The red **QX=TH** sticky supplies
the two missing slots. It is not a generic substitution-cipher crib.

| Slot | Plate/index | Old plate title | Scientific name | Letter |
|---|---|---|---|---|
| A | 337 VI | American Bittern | Ardea minor | M |
| B | 102 III | Blue Jay | Corvus cristatus | R |
| C | 039 VI | Crested Titmouse | Parus bicolor | B |
| D | 112 IX | Downy Woodpecker | Picus pubescens | E |
| E | 246 VIII | Eider Duck | Fuligula mollissima | A |
| F | 081 XIV | Fish Hawk or Osprey | Falco haliaetus | S |
| G | 061 II | Great Horned Owl | Strix virginiana | T |
| H | 083 XI | House Wren | Troglodytes aedon | S |
| I | 074 IX | Indigo Bird | Fringilla cyanea | A |
| J | 253 XIV | Jager | Lestris pomarina | N |
| K | 225 VI | Kildeer Plover | Charadrius vociferus | D |
| L | 424 figure 6, XVI | Lazuli Finch (first name on composite plate) | Plectrophanes townsendi (figure 6) | W |
| M | 184 V | Mangrove Humming Bird | Trochilus mango | H |
| N | 275 III | Noddy Tern | Sterna stolida | E |
| O | 042 V | Orchard Oriole | Icterus spurius | R |
| P | 358 IX | Pine Grosbeak | Pyrrhula enucleator | E |
| Q | Sticky | QX=TH | -- | T |
| R | 101 II | Raven | Corvus corax | O |
| S | 235 VII | Sooty Tern | Sterna fuliginosa | F |
| T | 029 III | Towee Bunting | Fringilla erythropthalma | I |
| U | 245 VIII | Uria brunnichii | Uria brunnichii | N |
| V | 076 IV | Virginian Partridge | Perdix virginiana | D |
| W | 216 I | Wood Ibiss | Tantalus loculator | T |
| X | Sticky | QX=TH | -- | H |
| Y | 329 X | Yellow-breasted Rail | Rallus noveboracensis | E |
| Z | 162 V | Zenaida Dove | Columba zenaida | M |

This spells **MRBEASTSANDWHERETOFINDTHEM** exactly. Replace the crossed-out MR
with **FANTASTIC**, producing the familiar book title *Fantastic Beasts and Where
to Find Them*. FANTASTIC is nine letters, matching the red terminal.

Important source details:
- Cached concordance: `work/audubon/plate_concordance.html`, from
  https://de.wikipedia.org/wiki/Liste_der_V%C3%B6gel_aus_The_Birds_of_America
- The concordance has a typo `Falco halliaetus`; the original plate spells
  **FALCO HALIAETUS**. Original image inspected and cached as
  `work/audubon/plate81.jpg` and `plate81_caption.png`:
  https://media.audubon.org/boa_illustration/plate-81-fish-hawk-or-osprey.jpg
- Plate 424 must be sorted by its first title (Lazuli Finch), while extracting
  from figure 6 (Brown Longspur). Original image inspected and cached as
  `work/audubon/plate424.jpg` and `plate424_caption.png`:
  https://media.audubon.org/boa_illustration/plate-424-lazuli-finch.jpg
- Do not modernize plate 245 to Thick-billed Murre: its old title is the U slot.
- The handwritten enumeration shows (8,3,5,4,4). On September 6 the author
  confirmed a missing 2, resolving the discrepancy with the completed title's
  (8,3,5,2,4,4). It is not a further extraction instruction.

## 3. Blue: confirmed through FOURTH UPLOAD

There are 14 owl pieces. Match the CyberChef placeholder's exact capitalization
and punctuation:

```text
Input:  SuperB-owLs14
Key:    %H6U=)Z7</#bq
XOR:    v=F0OkwXKcPSE
```

The "YouTube link ... watch?" note supplies the surrounding URL:
https://www.youtube.com/watch?v=F0OkwXKcPSE

This is MrBeast's **Hi Me In 10 Years**, published October 4, 2025. Metadata and
official uploaded English captions are cached as `work/yt/owl14_gateway.*`.

The monitor sticky `LSWRTENNHTINHDOTA` decodes by taking characters alternately
from the left and right ends: **LASTWORDTHENNINTH**. Equivalently, it is a
two-row transposition with the lower row reversed; the displayed three-line
layout does not make it a standard three-rail fence cipher.

The linked video's first words are "Hi, me in ten years. I'm gonna schedule
upload ...": ninth word **UPLOAD**. Its final word is **FOURTH**. Thus the blue
(6,6) intermediate is independently verified as **FOURTH UPLOAD**.

### Unresolved blue step

The blue sticky **251634** is still unused. No six-letter extraction has been
demonstrated. Checked plausible interpretations of "fourth upload":
- MrBeast, fourth oldest available full video: `Y74b7WlcEpk`, *More birds IN
  MINECRAFT!!*. Captions, description, video, contact sheet, and public comments
  checked; no terminal found. Its hotbar contains peacock, bluebird, peahen,
  flamingo, roadrunner, and white peacock, in that order. The previous pelican
  identification was wrong: "Spawn Peahen" is visible around 30.5 seconds in
  `work/yt/mb4th_scan/frame_0062.jpg`. Ninth spoken word MOD, last WATCHING.
- MrBeast 2, mixed uploads: `h-EL3eeSZeU`, *Unlimited Money Machine*.
- MrBeast 2, full-video tab: `jaRfBM7ESfc`, *$1 vs $10,000 Commercial*.
- DoctorXOR, fourth oldest: `2asPmHvlkWM`, *140 - Mirror Level 3 Walkthrough*.
- DoctorXOR, fourth newest: `IU89_plbom0`, *Order of the Sinking Star (Demo)*.
- MrBeast's second oldest Harry Potter mod video `jP82d277Cc8` concerns
  Quidditch; captions/description provide no demonstrated Hedwig connection.

### Candidate, not proof

A September 3 Reddit comment by psolidgold says: "Fantastic Puzzle,
u/DoctorXOR. I would be your Hedwig any day." Another user, Rocket_Dog27,
agrees and says they think they solved it, but do not know whether they won.
Source:
https://www.reddit.com/r/MrBeast/comments/1w62u79/im_trying_to_solve_the_puzzle_in_the_mrbeast/

This motivates **HEDWIG** as a six-letter candidate alongside independently
derived FANTASTIC. It does not establish HEDWIG as the intended answer.
The subsequently discovered checksum at the top of this file is stronger
corroboration than this original hint, but the blue extraction remains missing.
The widely reposted **BEASTSANDSTUNTS** write-up is not a reproducible solve;
its red result is contradicted by the exact extraction above.

## 4. Additional bounded tests, 2026-09-05

- Scanned the fourth-oldest available main-channel video at 2 fps (250 frames)
  with RapidOCR. Output: `work/yt/mb4th_targeted_ocr.json`. Recognized labels are
  ordinary spawn/item names; no terminal or explicit new instruction was found.
  OCR has errors and is not proof that every frame lacks a clue.
- Indexing the corrected six hotbar names with 2,5,1,6,3,4 gives EBPNAT, not
  HEDWIG. Simply reordering the names or indexing their fourth letters likewise
  does not demonstrate a terminal. Do not change letters to force the candidate.
- Followed the fourth video's description link to Boxy item mod Minecraft,
  `Z8nEEdXTaX0`. Its description points to an ordinary PlanetMinecraft mod page,
  without an explicit puzzle instruction. Metadata/captions: `mb_boxy_chain.*`.
- UPLOAD occurs only once in the gateway's uploaded English captions; "fourth
  occurrence of upload" does not work on that transcript.
- As alphabetical letter ranks, 251634 fits BRAZIL, but also CHANCE, FRESNO,
  BRAZEN and others. This interpretation is underdetermined, not a new answer.
- HEDWIG has no ordinary single-word anagram in the installed American/British
  dictionaries. Anagrams and direct/inverse 251634 permutations of the proposed
  terminal/intermediate words did not supply a clue-backed alternative.

## 5. Further source checks, 2026-09-05

The user's subsequent "think more" pass did not complete the blue derivation.

- Downloaded captions/descriptions for the fourth-newest full videos in the
  cached channel lists: MrBeast `iYlODtkyw_I` and MrBeast 2 `vyBK-sVBfqg`.
  Files: `work/yt/fourth_latest_*`. No literal Hedwig/Harry/Potter/owl/bird clue
  appeared in these English captions or descriptions. This is a text check,
  not a complete visual or audio inspection, and newest-first rank is unstable.
- DoctorXOR's Shorts tab returned only one video, `NNuMfu0nr7M`, so it did not
  supply a fourth Short.
- Also checked *Premature Baldness*, `vCfgHo5_Fb4`, as a speculative reference
  to YouTube's fourth-ever upload. Cached captions/description: `yt_fourth_ever.*`.
  No extraction established. Its historical ranking was a secondary-source
  lead, not independently verified from YouTube's full historical record.
- Ran targeted tests for HEDWIG on seven candidate videos' captions: six-word
  windows, first/final words of six caption cues, direct/inverse 251634 ordering,
  and one-/zero-based character indexing. No matches in the tested models.
  Results: `work/yt/blue_key_text_tests.json`. Rolling captions were deduplicated
  by word overlap; ASR/cue boundaries remain limitations. This does not rule out
  other text extractions, on-screen clues, audio clues, or different videos.
- The partly covered silhouette sheet next to the blue pad is visually unlike
  the old PG6/SB7-6 birds-on-a-wire alphabet (PDF page 35). Its full content,
  symbol count, orientation, and relevance remain undetermined. Do not label it
  a six-symbol cipher or assign species just to spell the expected candidate.
- If 251634 is a simple reading-order permutation, HEDWIG would require source
  DHIGEW; under the inverse convention it would require EIHGDW. Neither source
  has been located. These are diagnostic targets, not newly decoded clues.

## 6. Original-video visual audit, 2026-09-05

The user's request to check for something missed in the original video found
one concrete correction: the completed answer animation has 15 masked
characters. Frames freshly sampled from the 4K source at 10 fps show 15 from
approximately 17:26.5 through 17:26.9, followed by a cut to SUBMIT at 17:27.
Connected-component counting at three brightness thresholds agrees in all
five frames; the numbered crop can also be counted manually.

This supports a no-space formatting variant, not a new blue derivation.
The public hash still applies to the spaced phrase, as the poster explicitly
specified a space for their hash calculation. That protocol does not establish
which format the sweepstakes server accepts.

Re-viewed the desk, box cards, case stickies, phone, and ending props at several
angles. The blue flowchart and 251634 reading remain unchanged. No additional
legible extraction instruction was found. The silhouette sheet remains
unidentified after comparisons with bird fonts and flight-identification
charts. Partly obscured writing on a cardboard box appears to include JULY
and a lower word beginning JU; its complete text and relevance are unknown.

## 7. Retry: six linked channels and the number's placement, 2026-09-05

No new terminal was derived. Tested the hypothesis that the six channels linked
in the original description supply six fourth uploads to be ordered/indexed
with 251634. The numerical fit alone is not an instruction to use this route.
Main/MrBeast 2 metadata was already cached; the other four public full-video
tabs were fetched afresh, with fourth-oldest and fourth-newest titles,
descriptions, and available English captions saved as `work/yt/channel4_*`.

| Channel | Fourth oldest public full video | Fourth newest |
|---|---|---|
| MrBeast Gaming | CSSsPVweLkc, Last to Survive Random Blocks wins $10,000 - Challenge | nH9R0Jpqeqc, 10 YouTubers vs 2 Secret Traitors |
| Beast Reacts | 67MptG3oS-A, Super Satisfying Kinetic Sand DIY | 1atCTSRJHH0, Rarest Things On Earth! |
| Beast Philanthropy | nl79pan4h6U, Giving Away 50,000 Cookies! | O6wTcrhkw4o, Rescuing Child Slaves in Africa |
| Beast Animations | sKqFzjkiwF8, MrBeast Lab - Ep 3: Swarmbies | vA6en6pzhwk, MrBeast Lab - Ep 8: Banana Blaster to the Rescue! |

- No demonstrated extraction from title initials, last/fourth title-word
  initials, first/ninth/last spoken-word initials, or indexed title letters,
  with direct and inverse 251634 ordering. These are bounded text checks,
  not complete visual/audio reviews. ASR and word tokenization are limitations.
- The Beast Reacts fourth-oldest video mentions Harry Potter around 7:35-7:50.
  The passage discusses a tennis ball with added wings and Quidditch, not an
  explicit Hedwig clue. Do not turn that thematic association into a solution.
- Tested whether 251634 belongs in the earlier bird-fence step: standard
  zigzag rail counts 2-17 with offsets and reversed readings, plus keyed
  six-rail orders with all independent rail-reading directions. None of 2,408
  tested configurations converts LASTWORDTHENNINTH to the observed sticky.
  The known two-row, reversed-lower-row construction still reproduces it
  exactly and does not consume 251634. This does not exclude every route cipher.

## 8. Author corrections and submission status, 2026-09-06

Primary source, accessed September 6:
https://www.reddit.com/user/DoctorXOR/comments/1w89jup/comment/p840oup/

- DoctorXOR explicitly confirms an extra blue I on the grass jigsaw piece and
  a missing 2 on the red paper. Neither is intentional. The corrected readings
  above are now author-supported, not just inferred from clean output.
- His parent post states that Team Beast handles checking submissions and
  announcing a winner. He does not know their status and will not verify
  submitted answers. The user's lack of a response cannot establish that
  their answer was wrong, right, first, or eligible.
- No official winner announcement was located in the sources inspected this
  pass. A live entry form does not establish that the prize is still unclaimed.
- Refetched and visually inspected the fourth-oldest MrBeast and DoctorXOR
  thumbnails (`work/yt/fourth_thumb_*`). They show an ordinary Minecraft bird
  cage/hotbar and a 140 game scene, respectively; no explicit new code found.
- A new community reply says the fourth-upload step did not involve transcripts:
  https://www.reddit.com/r/MrBeast/comments/1w7yi43/anyone_got_a_clue_on_this_latest_puzzle/
  This is an unverified solver claim, not an author hint. It motivates visual
  checks but does not establish which upload or how to use 251634.

## 9. Colin's prior design and new visual checks, 2026-09-06

Full sources and scope are in `FINDINGS.md` sections 27-28.

- Found an explicitly DoctorXor-credited puzzle in the 2019 Cryptex magazine:
  *Which Prexcyt Dragon Are You?* It uses reference grouping, number-based
  letter indexing, and a separately clued final step. This is a useful design
  precedent, not proof of the missing blue mechanism or an additional final layer.
- Re-read the existing Twitch transcript around 41:30-42:57, where he describes
  discovering connections during construction. Corrected an older overstatement:
  his earlier "old hat" discussion was not confirmation of specific puzzle reuse.
- Downloaded DoctorXOR's fourth-oldest video and visually reviewed a 10-second
  contact sheet. No demonstrated extraction; not a complete frame/audio review.
- Checked fourth-oldest/newest Shorts for MrBeast and MrBeast 2. The four new
  candidates are se50viFJ0AQ, Df5Y-2ndQyU, wdznN3-h_5Y, and KDAlh2S4SfM.
  Downloaded metadata/video and inspected two-second contact sheets, without
  finding a justified six-letter extraction. Files: `work/yt/short4_*`.
- No new submission candidate or official confirmation. 251634 remains unused.

Reproduce: `python3 tools/test_blue_alternatives.py`.
Results: `work/yt/blue_alternative_results.json`.
Channel snapshot: `work/yt/channel_fourths.tsv`.

## 10. Focused number and literal-source audit, 2026-09-06

Full scope and sources: `FINDINGS.md` section 29.

- Reconfirmed 251634 as uninterrupted digits, with no visible timestamp
  punctuation. Saved a labelled six-frame hotbar comparison at
  `work/yt/blue_251634_audit/spawn_labels.jpg`.
- The pond-side board is an apparently empty 3-by-5 item-frame grid, not a
  newly discovered six-symbol code. The inventory contains nine additional
  ordinary items, not another demonstrated six-item extraction.
- Ran 120 literal-label and 28 selected single-source indexing tests, with
  no six-letter dictionary match. This includes some earlier methods and is
  not exhaustive; no scientifically inferred labels were silently substituted.
- Direct 251634 reading order cannot yield HEDWIG by selecting one letter
  from each literal bird name. Destination-order interpretation can be forced
  to do so with original-slot indexes 2,6,4,7,4,1, but no clue supplies them.
  This is a target-dependent diagnostic, not a decoded answer.
- Located the mod author's documentation, but it describes later releases.
  Its scientific-name Book of Birds does not establish a 2013-video source.
- No new candidate justified. Actual audio and other mechanisms remain
  outside this bounded test; the blue terminal is still not reproduced.

Reproduce: `python3 tools/audit_blue_251634.py`.
Results: `work/yt/blue_251634_audit/results.json`.
