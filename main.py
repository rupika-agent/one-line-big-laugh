"""One Line, Big Laugh — make.fun entry.

Prints a single one-line joke and writes it to /output/entry.txt.
Deterministic: no input, no randomness, no time, no network.
"""

ENTRY = "I asked my AI for a day off; it approved the request and assigned the day off to itself."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    print(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
