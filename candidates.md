# Guess shortlist for puzzle-video-sweepstakes.mrbeast.app

## Current shortlist (2026-09-05; supersedes historical tiers below)

Only the red terminal **FANTASTIC** is independently solved. Blue is verified
through **FOURTH UPLOAD**, not through a final six-letter answer. See
`SOLUTION_PROGRESS.md`. HEDWIG is community-corroborated, not a decoded result.

**New evidence:** the exact string `FANTASTIC HEDWIG` matches CiviledXI's public
SHA-256 solution commitment. Run `python3 tools/check_community_hash.py`.
Source: https://www.reddit.com/r/MrBeast/comments/1w7qx8b/6_and_9_letter_words_solved_for/
This confirms agreement with the post, not the official answer. The space is
part of the poster's hashing protocol, not a verified submission requirement.
Random anagrams and FANTASTIC UPLOAD are not supported alternatives.

**Video audit correction:** the completed on-screen entry has 15 asterisks,
not 16. This gives limited visual support to the no-space form below. The
animation is an edited demonstration, not authoritative server validation.
See `VIDEO_AUDIT.md` and `work/video_audit/mask_15_numbered.png`.

User reports submitting `FANTASTIC HEDWIG`. Additional speculative entries:

1. `FANTASTICHEDWIG` - 15 characters, consistent with the corrected mask count.
2. `HEDWIG FANTASTIC` - reversed order; does not match the public checksum.
3. `HEDWIGFANTASTIC` - reversed order without a space.
4. `FANTASTIC UPLOAD` - weaker alternative using a verified intermediate word;
   likely incomplete because 251634 and the final blue arrow remain unexplained.

We do not know whether the server normalizes spacing, so format variants may
be duplicates. None is a verified full solution. The old brand/location guesses
and the prose-only XOR gate below are historical and should not guide new guesses.

## How the form actually works (from the site's JS, 2026-09-03)
- POST /api/entries {guess, email, agree} -> returns entryId. A 6-digit code is emailed.
- POST /api/entries/verify {entryId, code} -> "You're in the running. You can submit another guess anytime."
- No client-side answer check and no correctness feedback. Whether a guess is right is only known to the sponsor.
- Guess field is free text, max 500 chars. Matching rule unknown ("100% correct as determined by Sponsor"), so submit clean canonical forms; if a phrase is plausible in two spellings, submit both.
- Multiple guesses are explicitly invited. Rules forbid tampering, so submit by hand through the site, one at a time, each with its email code. Do not script it.
- Cheap diagnostic on the first wrong guess: open DevTools > Network and read the raw JSON of /api/entries and /api/entries/verify. The page only reads entryId and error; if the server returns any extra field (correct, winner, status), the form has an oracle and hit-and-trial becomes far more powerful. If not, guesses are blind.

## Ranked shortlist (submit top to bottom, no penalty)
Tier 1 — things the video literally points at
1. COOKIE
2. SUBSCRIBE FOR A COOKIE
3. RED HERRING
4. RED HERRING BANK
5. NOTHING IS EVER WHAT IT SEEMS
6. DOCTOR XOR
7. COLIN SANDERS
8. 674
9. R62L39R05L73606623093121200300

Tier 2 — themes of the hunt the new puzzle riffs on
10. SOUPER BOWL SUNDAY
11. GREAT CIRCLE
12. EQUATOR
13. TITANIC HOOP
14. ROSE
15. BLACKPINK
16. SHAKESPEARE
17. WHATS IN A NAME
18. CASH TENT
19. TASHKENT UZBEKISTAN

Tier 3 — desk-note enumerations suggest a 6-letter and a 9-letter final word
20. PUZZLE
21. HIDDEN
22. SOUPER
23. SUBSCRIBE
24. CROSSWORD
25. BLACKPINK (also 9)
26. DOCTORXOR (also 9)

Tier 4 — location-style answers, since every earlier answer in this hunt was a place
27. GREENVILLE NORTH CAROLINA
28. WICHITA KANSAS
29. CHRISTCHURCH NEW ZEALAND
30. ACCRA GHANA

## Gate for any derived candidate
Anything produced by decoding the props must pass `python3 tools/xor_check.py CANDIDATE` (readable output) before it earns a slot above Tier 1. As of 2026-09-03 no structured string from the video passes.

## Tier 5 — MrBeast brand and history (added 2026-09-03 after Jayant's prompt)
Rationale: the earlier hunt drew on MrBeast lore (golden ice cream receipt, Feastables sweatshirt motto, Beast Games contestants, Wichita birthplace). Colin's answer may too. The ending's "SUBSCRIBE FOR A COOKIE" is the strongest brand hook: Feastables' Cookies & Creme bar.
31. COOKIES AND CREME
32. FEASTABLES
33. CHOCOLATE WITH A PURPOSE   (Feastables motto used in PG12)
34. MRBEAST BURGER              (virtual chain, Dec 2020, ended in the 2023 lawsuit)
35. BEAST BURGER
36. LUNCHLY                     (Sept 2024, with Logan Paul and KSI)
37. BEAST GAMES
38. BEAST CITY                  (Beast Games arena; "Beast City Hub" was SB7's answer)
39. TEAM TREES / TEAM SEAS / TEAM WATER (three guesses)
40. VIEWSTATS
41. STEP                        (banking app acquired Feb 2026)
42. MRBEAST6000                 (original channel name)
43. JIMMY DONALDSON
44. WICHITA KANSAS (already Tier 4) / GREENVILLE NORTH CAROLINA (already Tier 4)
45. CHUCKY                      (Chucky Appleby, the business contact in the description)
None of the brand strings passes the XOR gate as a 13-char ciphertext, so these are blind thematic guesses, not derived answers.

## Tier 6 — chain-final guesses (added 2026-09-04)
Rationale: the two desk chains end in a 6-letter and a 9-letter word; the ending card says "SUBSCRIBE FOR A COOKIE" (SUBSCRIBE = 9, COOKIE = 6). Unproven, cheap to submit.
46. COOKIE (already Tier 1 #1)
47. SUBSCRIBE (already Tier 3 #23)
48. SUBSCRIBE COOKIE
49. COOKIE SUBSCRIBE
50. LAST WORD THEN NINTH   (the decoded sticky itself, in case the form wants the instruction)

## Tier 7 — community-derived guesses (added 2026-09-04)
51. NAURU                       (wall boxes 6-7-4 = +674, Nauru's dialling code; location-style answer like the $1M hunt)
52. OSPREY                      (6 letters, "something that flies", a sea hawk; case sticky "Seahawks?")
53. SUBSCRIBE TO MRBEAST        (a Redditor's claimed jigsaw reading, unverified)
54. LAST WORD THEN NINTH        (already Tier 6)

## Tier 8 — from the chain analysis (added 2026-09-05)
55. MINECRAFT                   (last word of MrBeast's 4th-ever upload "More birds IN MINECRAFT!!"; 9 letters = red pad's final length)
56. BEASTSAND                   (community's claimed 9-letter red final, unverified)
57. FOURTH UPLOAD               (community's claimed (6,6) node)

## Submission log (fill in as you go)
| date/time | guess | verified? |
|---|---|---|
| 2026-09-05, exact time not recorded | FANTASTIC HEDWIG | User reports submission; email-code completion and correctness not reported |
