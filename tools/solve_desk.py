"""Reproduce the desk puzzle's scientific-name extraction and XOR link."""

import re
import string
from pathlib import Path

from lxml import html


ROOT = Path(__file__).resolve().parents[1]
PAIRS = {
    29: 3, 39: 6, 42: 5, 61: 2, 74: 9, 76: 4, 81: 14, 83: 11,
    101: 2, 102: 3, 112: 9, 162: 5, 184: 5, 216: 1, 225: 6,
    235: 7, 245: 8, 246: 8, 253: 14, 275: 3, 329: 10,
    337: 6, 358: 9, 424: 16,
}


def letters(value):
    return re.sub("[^A-Z]", "", value.upper())


def plate_rows():
    doc = html.parse(str(ROOT / "work/audubon/plate_concordance.html"))
    rows = {}
    for row in doc.xpath("//table//tr"):
        cells = [" ".join(c.text_content().split()) for c in row.xpath("./td|./th")]
        if not cells or not cells[0].isdigit() or int(cells[0]) not in PAIRS:
            continue
        number = int(cells[0])
        caption = cells[5]
        scientific = re.search(r"\(([^()]+)\)", caption)
        old = scientific.group(1) if scientific else caption
        # Plate 424 figure 6 is the final row for this plate in the concordance.
        rows[number] = {
            "number": number, "index": PAIRS[number], "old": old,
            "modern": cells[3], "common": caption.split("(")[0].strip(),
        }
    return rows


def main():
    key = b"%H6U=)Z7</#bq"
    token = b"SuperB-owLs14"
    result = bytes(a ^ b for a, b in zip(token, key)).decode("ascii")
    print("XOR:", token.decode(), "->", "https://www.youtube.com/watch?" + result)
    rows = plate_rows()
    # The concordance misspells HALIAETUS and indexes figure 6 under its own name.
    # Use the original plate 81 spelling and plate 424's first caption instead.
    rows[81]["old"] = "Falco haliaetus"
    rows[424]["common"] = "Lazuli Finch"
    alphabet = {"Q": "T", "X": "H"}
    for row in sorted(rows.values(), key=lambda r: r["common"]):
        slot = row["common"][0].upper()
        assert slot not in alphabet, (slot, row)
        alphabet[slot] = letters(row["old"])[row["index"] - 1]
    assert set(alphabet) == set(string.ascii_uppercase)
    red = "".join(alphabet[c] for c in string.ascii_uppercase)
    assert red == "MRBEASTSANDWHERETOFINDTHEM", red
    print("Red A-Z with QX=TH:", red)
    print("Red wordplay: replace MR with FANTASTIC (9 letters)")

    # The blue sticky is a two-row alternating-ends transposition, not a
    # conventional three-rail cipher. Its displayed line breaks are cosmetic.
    sticky = "LSWRTENNHTINHDOTA"
    blue_instruction = "".join(
        sticky[i // 2] if i % 2 == 0 else sticky[-1 - i // 2]
        for i in range(len(sticky))
    )
    assert blue_instruction == "LASTWORDTHENNINTH"
    print("Blue sticky:", blue_instruction)
    captions = (ROOT / "work/yt/owl14_gateway.en.vtt").read_text()
    spoken = []
    for block in captions.split("\n\n"):
        lines = block.splitlines()
        for i, line in enumerate(lines):
            if " --> " in line:
                spoken.extend(lines[i + 1:])
                break
    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", " ".join(spoken))
    gateway = (words[-1].upper(), words[8].upper())
    assert gateway == ("FOURTH", "UPLOAD"), gateway
    print("Gateway captions: last word", gateway[0], "; ninth word", gateway[1])
    print("Blue terminal: NOT independently solved; 251634 remains unused")
    print("\nDiagnostic extraction variants:")
    for source in ("old", "modern", "common"):
        for order in ("number", "old", "modern", "common"):
            ordered = sorted(rows.values(), key=lambda r: r[order])
            extracted = "".join(
                letters(r[source])[r["index"] - 1:r["index"]] or "?" for r in ordered
            )
            chunks = (extracted[:8], extracted[8:11], extracted[11:16], extracted[16:20], extracted[20:])
            print(source, "sorted by", order, ":", " ".join(chunks))
    print("\nHistorical scientific names, alphabetical:")
    for row in sorted(rows.values(), key=lambda r: r["old"]):
        value = letters(row["old"])
        print(row["number"], row["index"], row["old"], value[row["index"] - 1:row["index"]])


if __name__ == "__main__":
    main()
