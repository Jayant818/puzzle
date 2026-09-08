# Original video audit, 2026-09-05

Source: `work/orig_4k.webm`, the cached 3840x2160 stream of
https://www.youtube.com/watch?v=82CX6WULNA0

## Confirmed correction: 15 masked characters

The completed typing animation contains **15 asterisks**, not 16. The earlier
count in FINDINGS.md was wrong. The red required-field marker beside the
question is not part of the typed answer.

- Newly extracted sequence: `work/video_audit/typing/frame_001.jpg` through
  `frame_035.jpg`, sampled at 10 fps from approximately 17:25.0 to 17:28.4.
- Five complete-entry frames: 016-020, approximately 17:26.5-17:26.9.
- The next sample cuts to SUBMIT; no further character appears in these samples.
- Each of the five frames has 15 star-shaped connected components at brightness
  thresholds 170, 185, and 200, agreeing with manual inspection.
- A second extraction preserved every source frame around the final typing/cut
  at the native 30000/1001 fps. Frames 008-020 have 15 stars continuously; the
  remaining frames show the SUBMIT view. No briefly displayed 16th star appears.
- Numbered crop: `work/video_audit/mask_15_numbered.png`.
- Full sequence overview: `work/video_audit/typing_overview.jpg`.
- Reproduce counting with `python3 tools/count_submission_mask.py`; results are
  written to `work/video_audit/mask_counts.json`.

Extraction command (requires the output directory to exist):

```sh
ffmpeg -hide_banner -loglevel error -ss 1045 -i work/orig_4k.webm -t 3.5 -vf fps=10,scale=1920:-1 -q:v 2 work/video_audit/typing/frame_%03d.jpg
ffmpeg -hide_banner -loglevel error -ss 1046.3 -i work/orig_4k.webm -t 0.9 -vf scale=1920:-1,crop=760:120:560:520 -fps_mode passthrough work/video_audit/native_mask/frame_%03d.png
```

FANTASTIC has 9 letters and HEDWIG has 6, so FANTASTICHEDWIG fits 15 characters.
The spaced form has 16. This is limited support for a no-space variant, not
proof of the solution, the intended answer length, or the server's spacing
rules. This count does not complete the missing 251634 step.

## Other objects reviewed

Compared cached original-video frames/crops around 0:18, 5:36, 9:04, 12:45,
13:22, and the ending TV sequence. This was targeted visual inspection, not a
new exhaustive inspection of every frame or a fresh audio analysis.

| Object | Result |
|---|---|
| Blue flowchart | Still (3,6,4) + (4,4,4,5) -> (6,6) -> (6). |
| Six case stickies | Still alternate red/blue. 251634 is clear and remains unused. |
| Silhouette sheet beside blue pad | Several flight-like shapes are visible, but full sheet, count, identity, and relevance remain unknown. |
| Handwriting on cardboard box under US/barn card | A fragment appears to say JULY, with a lower word starting JU. The black case hides the rest; do not infer a date or new instruction. |
| Phone / TV / green box tape | No new legible extraction instruction found in the reviewed crops. |
| Wall sticky labels | Reviewed DASHES and CODE ON DOOR labels describe visible old-hunt material, not a demonstrated new blue step. |

The silhouette sheet was compared visually with Birds of a Feather, the
lowercase Bird Silhouettes font, Birds Wingspans, and two flight-identification
charts. No exact match was established. These comparisons do not prove that
it is unrelated to the puzzle.
