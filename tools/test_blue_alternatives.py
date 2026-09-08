"""Test bounded blue-path alternatives without selecting a desired answer."""

import csv
import itertools
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work/yt"
KEY = (2, 5, 1, 6, 3, 4)
INVERSE = tuple(KEY.index(i) + 1 for i in range(1, 7))
CHANNELS = (
    "UCX6OQ3DkcsbYNE6H8uQQuVA",
    "UC4-79UOlP48-QNGgCko5p2g",
    "UCIPPMRA040LQr5QPyJEbmXA",
    "UCUaT_39o1x6qWjz7K2pWcgw",
    "UCAiLfjNXkNv24uhpzUgPa6A",
    "UCZzvDDvaYti8Dd8bLEiSoyQ",
)
WORDS = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
TITLE_WORDS = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?|\$?\d[\d,]*(?:\.\d+)?")


def caption_words(path):
    words = []
    for block in path.read_text().split("\n\n"):
        lines = block.splitlines()
        times = next((i for i, line in enumerate(lines) if " --> " in line), None)
        if times is None:
            continue
        text = re.sub(r"<[^>]*>", "", " ".join(lines[times + 1:]))
        text = re.sub(r"\[[^\]]*\]", "", text)
        current = [word.upper() for word in WORDS.findall(text)]
        overlap = next(
            (n for n in range(min(len(words), len(current)), 0, -1)
             if words[-n:] == current[:n]),
            0,
        )
        words.extend(current[overlap:])
    return words


def rail_tests():
    plain = "LASTWORDTHENNINTH"
    cipher = "LSWRTENNHTINHDOTA"
    assert plain[::2] + plain[1::2][::-1] == cipher
    results = []
    tested = 0
    for rails in range(2, len(plain) + 1):
        period = 2 * (rails - 1)
        orders = {tuple(range(rails)), tuple(reversed(range(rails)))}
        if rails == 6:
            orders.update(tuple(n - 1 for n in key) for key in (KEY, INVERSE))
        for offset in range(period):
            rows = [[] for _ in range(rails)]
            for i, char in enumerate(plain):
                phase = (i + offset) % period
                row = min(phase, period - phase)
                rows[row].append(char)
            for order in orders:
                for reverse_rows in (False, True):
                    encoded = "".join(
                        "".join(rows[r][::-1] if reverse_rows else rows[r])
                        for r in order
                    )
                    tested += 1
                    if encoded == cipher:
                        results.append({"rails": rails, "offset": offset,
                                        "order": order, "reverse_rows": reverse_rows})
    # A stronger six-rail test permits each rail to run in either direction.
    for offset in range(10):
        rows = [[] for _ in range(6)]
        for i, char in enumerate(plain):
            phase = (i + offset) % 10
            rows[min(phase, 10 - phase)].append(char)
        for key in (KEY, INVERSE):
            for reversed_flags in itertools.product((False, True), repeat=6):
                encoded = "".join(
                    "".join(rows[r - 1][::-1] if reversed_flags[r - 1] else rows[r - 1])
                    for r in key
                )
                tested += 1
                if encoded == cipher:
                    results.append({"rails": 6, "offset": offset, "order": key,
                                    "reverse_flags": reversed_flags})
    return {"models_tested": tested, "matches": results}


def channel_tests():
    groups = {}
    with (WORK / "channel_fourths.tsv").open() as source:
        for channel, rank, video, title in csv.reader(source, delimiter="\t"):
            groups.setdefault(channel, []).append((int(rank), video, title))
    report = {}
    for ordering, main, second in (
        ("oldest", "mb4th", "mb2_fourth_full"),
        ("newest", "fourth_latest_iYlODtkyw_I", "fourth_latest_vyBK-sVBfqg"),
    ):
        prefixes = [main, second]
        for channel in CHANNELS[2:]:
            entries = sorted(groups[channel], reverse=ordering == "oldest")
            prefixes.append("channel4_" + entries[3][1])
        details = []
        for prefix in prefixes:
            info_path = WORK / (prefix + ".info.json")
            if not info_path.exists():
                details.append({"prefix": prefix, "missing": True})
                continue
            info = json.loads(info_path.read_text())
            captions_path = WORK / (prefix + ".en.vtt")
            if not captions_path.exists():
                captions_path = WORK / (prefix + ".en-orig.vtt")
            spoken = caption_words(captions_path) if captions_path.exists() else []
            title_words = [word.upper().lstrip("$")
                           for word in TITLE_WORDS.findall(info["title"])]
            letter_title = "".join(WORDS.findall(info["title"])).upper()
            corpus = " ".join(spoken) + " " + info.get("description", "").upper()
            details.append({
                "id": info["id"], "channel": info.get("channel"),
                "title": info["title"], "upload_date": info.get("upload_date"),
                "title_initial": title_words[0][:1],
                "title_last_initial": title_words[-1][:1],
                "title_fourth_initial": title_words[3][:1] if len(title_words) > 3 else "?",
                "title_letters": letter_title,
                "spoken_first": spoken[0] if spoken else "?",
                "spoken_ninth": spoken[8] if len(spoken) > 8 else "?",
                "spoken_last": spoken[-1] if spoken else "?",
                "target_terms": sorted(set(re.findall(
                    r"\b(?:HEDWIG|HARRY|POTTER|OWL|OWLS)\b", corpus))),
            })
        outputs = {}
        if not any(item.get("missing") for item in details):
            for field in ("title_initial", "title_last_initial", "title_fourth_initial",
                          "spoken_first", "spoken_ninth", "spoken_last"):
                initials = "".join(item[field][0] for item in details)
                outputs[field] = {
                    "original": initials,
                    "key": "".join(initials[n - 1] for n in KEY),
                    "inverse": "".join(initials[n - 1] for n in INVERSE),
                }
            for name, key in (("key", KEY), ("inverse", INVERSE)):
                outputs["title_index_" + name] = "".join(
                    item["title_letters"][n - 1:n] or "?"
                    for item, n in zip(details, key)
                )
        report[ordering] = {"videos": details, "extractions": outputs}
    return report


def main():
    assert caption_words(WORK / "owl14_gateway.en.vtt")[8] == "UPLOAD"
    assert caption_words(WORK / "owl14_gateway.en.vtt")[-1] == "FOURTH"
    report = {
        "scope": "Public full-video tabs, both end orderings; captions are approximate ASR. "
                 "No claim about untested visual/audio extractions or unavailable uploads.",
        "rail_fence": rail_tests(), "six_channels": channel_tests(),
    }
    path = WORK / "blue_alternative_results.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
