"""Count the completed masked entry in five frames of the original video."""

import json
from pathlib import Path

import cv2
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "work/video_audit"
ROI = (560, 520, 1320, 640)


def stars(frame, threshold, cropped=False):
    left, top, right, bottom = ROI
    region = frame if cropped else frame[top:bottom, left:right]
    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    _, _, stats, _ = cv2.connectedComponentsWithStats(
        (gray > threshold).astype("uint8")
    )
    return sorted(
        (list(map(int, box)) for box in stats[1:]
         if 20 <= box[2] <= 50 and 20 <= box[3] <= 50 and box[4] > 150),
        key=lambda box: box[0],
    )


def main():
    results = []
    for index in range(16, 21):
        path = AUDIT / "typing" / f"frame_{index:03d}.jpg"
        frame = cv2.imread(str(path))
        if frame is None:
            raise FileNotFoundError(path)
        counts = {str(t): len(stars(frame, t)) for t in (170, 185, 200)}
        assert set(counts.values()) == {15}, (path, counts)
        results.append({
            "frame": str(path.relative_to(ROOT)),
            "approx_seconds": 1045 + (index - 1) / 10,
            "counts_by_threshold": counts,
        })

    annotated = Image.open(path).crop(ROI)
    draw = ImageDraw.Draw(annotated)
    for number, (x, y, width, height, _) in enumerate(stars(frame, 185), 1):
        draw.rectangle((x, y, x + width, y + height), outline="#55ff88", width=1)
        draw.text((x + 8, max(0, y - 18)), str(number), fill="#55ff88")
    annotated.resize((1520, 240)).save(AUDIT / "mask_15_numbered.png")

    native = []
    for native_path in sorted((AUDIT / "native_mask").glob("*.png")):
        native_frame = cv2.imread(str(native_path))
        native.append(len(stars(native_frame, 185, cropped=True)))
    assert len(native) == 27, "Expected the 0.9-second native-frame extraction"
    assert max(native) == 15 and native[7:20] == [15] * 13, native
    report = {
        "source": "work/orig_4k.webm",
        "sampling": "10 fps from 1045 seconds, scaled to 1920x1080",
        "roi_ltrb": ROI,
        "frames": results,
        "native_sequence_counts": native,
        "native_sequence_sampling": "All source frames from 1046.3 for 0.9 seconds",
        "conclusion": "15 visible asterisks, not 16",
        "limitation": "An edited demonstration does not establish server matching rules.",
    }
    (AUDIT / "mask_counts.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
