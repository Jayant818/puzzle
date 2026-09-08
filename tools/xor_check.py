#!/usr/bin/env python3
"""Test candidate strings against Colin's CyberChef recipe (XOR, UTF8 key '%H6U=)Z7</#bq').

usage: python3 tools/xor_check.py CANDIDATE [CANDIDATE ...]
       python3 tools/xor_check.py -f candidates.txt

Prints the XOR output, whether it is printable ASCII, and whether it looks like words.
The recipe is symmetric: it also shows what ciphertext a hoped-for ANSWER would need.
"""
import sys

KEY = b"%H6U=)Z7</#bq"


def xor(s: str) -> bytes:
    b = s.encode("utf-8")
    return bytes(x ^ KEY[i % len(KEY)] for i, x in enumerate(b))


def report(cand: str) -> None:
    out = xor(cand)
    printable = all(0x20 <= c < 0x7F for c in out)
    wordy = printable and sum(chr(c).isalpha() or c == 0x20 for c in out) >= 0.8 * len(out)
    flag = "WORDY" if wordy else ("printable" if printable else "junk")
    print(f"{cand!r:20} len={len(cand):2} -> {out.decode('latin1')!r:20} [{flag}]")


def main(argv):
    if len(argv) >= 2 and argv[0] == "-f":
        cands = [l.strip() for l in open(argv[1]) if l.strip()]
    else:
        cands = argv
    if not cands:
        print(__doc__)
        return
    for c in cands:
        report(c)


if __name__ == "__main__":
    # self-check: placeholder from the shared URL
    assert xor("AaaaaA-aaAa##") == b"d)W4\\hwV]nBAR"
    main(sys.argv[1:])
