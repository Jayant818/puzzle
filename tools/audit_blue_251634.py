"""Bounded, answer-blind indexing tests for the fourth-upload candidate."""

import json
import re
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work/yt"
OUTPUT = WORK / "blue_251634_audit"
KEY = (2, 5, 1, 6, 3, 4)
INVERSE = tuple(KEY.index(i) + 1 for i in range(1, 7))
ITEMS = (
    ("Peacock", 41),
    ("Bluebird", 53),
    ("Peahen", 62),
    ("Flamingo", 67),
    ("Roadrunner", 79),
    ("White Peacock", 98),
)


def letters(value):
    return re.sub("[^A-Z]", "", value.upper())


def extract(values, indices, from_end=False):
    result = []
    for value, index in zip(values, indices, strict=True):
        value = value[::-1] if from_end else value
        result.append(value[index - 1:index] or "?")
    return "".join(result)


def item_tests():
    rows = []
    for form in ("name", "full_spawn_label"):
        values = [letters(("Spawn " if form == "full_spawn_label" else "") + name)
                  for name, _ in ITEMS]
        orders = {
            "hotbar": tuple(range(6)),
            "reverse_hotbar": tuple(reversed(range(6))),
            "alphabetical": tuple(sorted(range(6), key=values.__getitem__)),
            "key_read_order": tuple(i - 1 for i in KEY),
            "key_destination_order": tuple(i - 1 for i in INVERSE),
        }
        indices = {
            "key": KEY, "inverse_key": INVERSE, "position": tuple(range(1, 7)),
            "first": (1,) * 6, "fourth": (4,) * 6, "ninth": (9,) * 6,
        }
        for order_name, order in orders.items():
            ordered = [values[i] for i in order]
            for index_name, index_values in indices.items():
                for from_end in (False, True):
                    rows.append({
                        "form": form, "order": order_name, "sources": ordered,
                        "index_rule": index_name, "indices": index_values,
                        "from_end": from_end,
                        "output": extract(ordered, index_values, from_end),
                    })
    return rows


def single_source_tests():
    info = json.loads((WORK / "mb4th.info.json").read_text())
    sources = {
        "instruction": "FOURTH UPLOAD", "instruction_first_word": "FOURTH",
        "instruction_last_word": "UPLOAD", "video_title": info["title"],
        "title_last_word": info["title"].split()[-1],
    }
    for i, line in enumerate(info["description"].splitlines(), start=1):
        if line.strip() and not line.startswith("download:"):
            sources[f"description_line_{i}"] = line
    rows = []
    for name, value in sources.items():
        clean = letters(value)
        for index_name, indices in (("key", KEY), ("inverse_key", INVERSE)):
            for from_end in (False, True):
                rows.append({
                    "source": name, "text": value, "normalized": clean,
                    "index_rule": index_name, "indices": indices,
                    "from_end": from_end,
                    "output": extract([clean] * 6, indices, from_end),
                })
    return rows


def evidence_sheet():
    sheet = Image.new("RGB", (1280, 900), "white")
    draw = ImageDraw.Draw(sheet)
    for i, (name, frame) in enumerate(ITEMS):
        source = Image.open(WORK / "mb4th_scan" / f"frame_{frame:04d}.jpg")
        x, y = (i % 2) * 640, (i // 2) * 300
        draw.text((x + 10, y + 8),
                  f"Slot {i + 1}: {name}; {(frame - 1) / 2:.1f} s", fill="black")
        # Keep the label and hotbar together; resizing adds no new evidence.
        crop = source.crop((320, 540, 960, 700)).resize((640, 160))
        sheet.paste(crop, (x, y + 35))
        overview = source.resize((160, 90))
        sheet.paste(overview, (x + 10, y + 202))
    path = OUTPUT / "spawn_labels.jpg"
    sheet.save(path, quality=95)
    return str(path.relative_to(ROOT))


def dictionary_matches(rows):
    words = set()
    dictionaries = []
    for name in ("american-english", "british-english"):
        path = Path("/usr/share/dict") / name
        if path.exists():
            dictionaries.append(str(path))
            words.update(word.upper() for word in path.read_text().splitlines()
                         if re.fullmatch("[A-Za-z]{6}", word))
    return dictionaries, [row for row in rows if row["output"] in words]


def main():
    assert INVERSE == (3, 1, 5, 6, 2, 4)
    assert "".join("ABCDEF"[i - 1] for i in KEY) == "BEAFCD"
    assert "".join("BEAFCD"[i - 1] for i in INVERSE) == "ABCDEF"
    assert extract([letters(name) for name, _ in ITEMS], KEY) == "EBPNAT"
    assert extract(["AB"] * 6, (3,) * 6) == "??????"
    assert extract(["ABCDEF"] * 6, KEY, True) == "EBFADC"
    OUTPUT.mkdir(exist_ok=True)
    item_rows, single_rows = item_tests(), single_source_tests()
    dictionaries, matches = dictionary_matches(item_rows + single_rows)
    report = {
        "scope": "Literal hotbar labels and selected title/description/instruction "
                 "text only. No invented species names, ASR, arbitrary offsets, "
                 "anagrams, substitutions, or claim of exhaustive coverage. "
                 "Dictionary matches are leads, not answer validation.",
        "video": "https://www.youtube.com/watch?v=Y74b7WlcEpk",
        "key": KEY, "inverse": INVERSE,
        "evidence_sheet": evidence_sheet(),
        "items": [{"slot": i + 1, "label": "Spawn " + name,
                   "frame": f"work/yt/mb4th_scan/frame_{frame:04d}.jpg",
                   "seconds": (frame - 1) / 2}
                  for i, (name, frame) in enumerate(ITEMS)],
        "item_tests": item_rows, "single_source_tests": single_rows,
        "dictionaries": dictionaries, "dictionary_matches": matches,
    }
    path = OUTPUT / "results.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{len(item_rows)} item tests; {len(single_rows)} single-source tests")
    print("Dictionary matches:", json.dumps(matches, indent=2))
    print("Report:", path.relative_to(ROOT))
    print("Evidence:", report["evidence_sheet"])


if __name__ == "__main__":
    main()
