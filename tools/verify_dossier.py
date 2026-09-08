"""Re-verify every table and calculation printed in LLM_REVIEW_PACKET.md.

Parses the dossier's own markdown tables and checks them against the cached
source data, so the document cannot drift from the evidence. Exit code is the
number of failures.
"""

import base64
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from solve_desk import letters, plate_rows

ROOT = Path(__file__).resolve().parents[1]
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XIV": 14, "XVI": 16}
FAILURES = []


def check(ok, message):
    print(("OK   " if ok else "FAIL ") + message)
    if not ok:
        FAILURES.append(message)


def plain(value):
    return value.replace("**", "").replace("\\*", "").replace("*", "").strip()


def cells(row):
    return [c.strip() for c in row.strip("|").split("|")]


def table(text, header):
    block = re.search(re.escape(header) + r".*?\n\n", text, re.S)
    return block.group(0).split("\n") if block else []


def check_owls(text):
    rows = [r for r in table(text, "| # | Picture | Owl |") if re.match(r"\| \d+ \|", r)]
    check(len(rows) == 14, f"owl table has 14 rows (got {len(rows)})")
    red = blue = ""
    for row in rows:
        c = cells(row)
        name = re.sub("[^A-Z]", "", c[3].upper())
        for numeral, letter, colour in ((c[4], c[5], "red"), (c[6], c[7], "blue")):
            numeral, letter = plain(numeral), plain(letter).replace("(none)", "")
            if numeral == "—":
                continue
            check(name[ROMAN[numeral] - 1] == letter,
                  f"{c[2]} {colour} {numeral} -> {letter}")
        red += plain(c[5])
        blue += plain(c[7]).replace("(none)", "")
    check(red == "BIRDSOFAMERICA", f"red numerals spell BIRDSOFAMERICA (got {red})")
    check(blue == "XORSUPERBOWLS", f"blue numerals spell XORSUPERBOWLS (got {blue})")


def check_audubon(text):
    rows = [r for r in table(text, "| Slot | Plate | Numeral |")
            if re.match(r"\| \*?\*?[A-Z]\*?\*? \|", r)]
    check(len(rows) == 26, f"Audubon table has 26 rows (got {len(rows)})")
    check("".join(plain(cells(r)[5]) for r in rows) == "MRBEASTSANDWHERETOFINDTHEM",
          "A-Z slots spell MRBEASTSANDWHERETOFINDTHEM")
    source = plate_rows()
    # The two source corrections the red chain depends on; see dossier section 5.2.
    source[81]["old"] = "Falco haliaetus"
    source[424]["common"] = "Lazuli Finch"
    for row in rows:
        c = cells(row)
        if plain(c[0]) in ("Q", "X"):
            continue
        number, index = int(plain(c[1]).split()[0]), ROMAN[plain(c[2])]
        check(source[number]["index"] == index,
              f"plate {number} numeral {plain(c[2])} matches the pink note")
        check(letters(source[number]["old"])[index - 1] == plain(c[5]),
              f"plate {number} yields {plain(c[5])}")


def check_derivations():
    for numbers, total, label in ((( 5, 2, 7), 14, "red source"),
                                  (( 3, 6, 4), 13, "blue source"),
                                  (( 4, 4, 4, 5), 17, "blue instruction"),
                                  (( 8, 3, 5, 2, 4, 4), 26, "red instruction")):
        check(sum(numbers) == total, f"{label} enumeration {numbers} = {total}")

    sticky, decoded = "LSWRTENNHTINHDOTA", "LASTWORDTHENNINTH"
    check("".join(sticky[i // 2] if i % 2 == 0 else sticky[-1 - i // 2]
                  for i in range(len(sticky))) == decoded, "alternating-ends decode")
    check(decoded[::2] + decoded[1::2][::-1] == sticky,
          "two-row transposition with the lower row reversed")

    encoded = "QWFhYWFBLWFhQWEjIw"
    placeholder = base64.b64decode(encoded + "=" * (-len(encoded) % 4)).decode()
    key = b"%H6U=)Z7</#bq"
    check(placeholder == "AaaaaA-aaAa##", "CyberChef placeholder decodes")
    check(" ".join(f"{b:02X}" for b in key) ==
          "25 48 36 55 3D 29 5A 37 3C 2F 23 62 71", "XOR key bytes")
    check(all(t.isupper() if p == "A" else t.islower() if p == "a"
              else t.isdigit() if p == "#" else p == t
              for p, t in zip(placeholder, "SuperB-owLs14")), "input matches the mask")
    check(bytes(a ^ b for a, b in zip(b"SuperB-owLs14", key)).decode() == "v=F0OkwXKcPSE",
          "XOR gives the YouTube suffix")

    check(hashlib.sha256(b"FANTASTIC HEDWIG").hexdigest() ==
          "b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22",
          "spaced phrase matches the public commitment")
    check(len("FANTASTICHEDWIG") == 15 and len("FANTASTIC HEDWIG") == 16,
          "15 unspaced / 16 spaced characters")


def check_test_counts():
    work = ROOT / "work"
    total = sum(x["tests"] for x in
                json.loads((work / "yt/blue_key_text_tests.json").read_text()))
    check(total == 81781, f"caption tests total 81,781 (got {total:,})")
    audit = json.loads((work / "yt/blue_251634_audit/results.json").read_text())
    check(len(audit["item_tests"]) == 120 and len(audit["single_source_tests"]) == 28,
          "251634 audit ran 120 + 28 = 148 models")
    check(audit["dictionary_matches"] == [], "251634 audit found no dictionary word")
    fence = json.loads((work / "yt/blue_alternative_results.json").read_text())["rail_fence"]
    check(fence["models_tested"] == 2408 and fence["matches"] == [],
          "2,408 rail-fence configurations, none matched")
    mask = json.loads((work / "video_audit/mask_counts.json").read_text())
    check(all(v == 15 for f in mask["frames"] for v in f["counts_by_threshold"].values()),
          "every sampled frame shows 15 asterisks")
    check(max(mask["native_sequence_counts"]) == 15, "native frames peak at 15 asterisks")


def check_references(text):
    images = sorted((ROOT / "dossier_images").iterdir())
    check(len(images) == 12, f"12 clue images present (got {len(images)})")
    for image in images:
        check(image.name in text, f"{image.name} is referenced in the dossier")


def main():
    text = (ROOT / "LLM_REVIEW_PACKET.md").read_text()
    check_owls(text)
    check_audubon(text)
    check_derivations()
    check_test_counts()
    check_references(text)
    print(f"\n{len(FAILURES)} failure(s)")
    for failure in FAILURES:
        print(" -", failure)
    return len(FAILURES)


if __name__ == "__main__":
    sys.exit(main())
