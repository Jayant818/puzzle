"""Compare a candidate with a public solver's hash, not the contest answer."""

import hashlib
import sys


SOURCE = (
    "https://www.reddit.com/r/MrBeast/comments/1w7qx8b/"
    "6_and_9_letter_words_solved_for/"
)
EXPECTED = "b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22"


def main():
    candidate = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "FANTASTIC HEDWIG"
    digest = hashlib.sha256(candidate.encode("utf-8")).hexdigest()
    print("Candidate:", repr(candidate))
    print("SHA-256:", digest)
    print("Matches CiviledXI's public claim:", digest == EXPECTED)
    print("Source:", SOURCE)
    print("A match is not official contest confirmation or a blue-path derivation.")
    return 0 if digest == EXPECTED else 1


if __name__ == "__main__":
    sys.exit(main())
