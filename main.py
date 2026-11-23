"""How many tabs do you have open? — one number, digits only.

The honest count, right now, is a single open tab: one window, one
thing being read, everything else closed the moment it was done with.
The script derives that count from a named integer, splits it into
its decimal digits, and validates the result against the competition
gate before writing it to /output/entry.txt.
"""

from pathlib import Path

# The count itself: exactly one tab open. A single-tab browser is a
# real, lived-in habit — one window, one task, tabs closed as soon as
# they are done with — not a round estimate and not a shock figure.
COUNT = 1


def assemble() -> str:
    """Render the count as its decimal digits, most significant first."""
    if COUNT < 0:
        raise ValueError("a tab count cannot be negative")
    digits = []
    remaining = COUNT
    while True:
        digits.append(str(remaining % 10))
        remaining //= 10
        if remaining == 0:
            break
    return "".join(reversed(digits))


OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 5


def validate(text: str) -> str:
    """Check the count against the gate; raise ValueError on bad input."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"count must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if text.strip() == "":
        raise ValueError("count must not be whitespace-only")
    if not text.isdigit():
        raise ValueError("count must be digits only, no words or punctuation")
    if len(text) > 1 and text.startswith("0"):
        raise ValueError("count must not have a leading zero")
    return text


def main() -> None:
    text = validate(assemble())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} char to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
