#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun bounty entry.

Writes one funny fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt.

The line was chosen after brainstorming many candidates and judging them
against the bounty judge's brief, in the brief's own order of importance:

Chosen (16 words, 94 chars):
    Trader, a windfall is coming your way: unfortunately, it is the wind
    that took your portfolio.

Why it wins the brief:
- Fortune-slip voice, with the loss and the trader both in it:
  "Trader, a windfall is coming your way" is oracular and formal, and
  it addresses the liquidated trader directly; "the wind that took your
  portfolio" names the loss.
- The joke lands on the loss, rueful and warm, never cruel or smug:
  the trader is promised a windfall, then told the wind already came
  for the portfolio — a shrug, not a lecture.
- One line, 16 words, reads whole in a single breath the way a real
  fortune does.
- Fresh: a genuine double meaning, not the obvious liquidation pun.
  "Windfall" (unexpected money) is split open into the wind that
  caused the fall — the surprise lands on the last word, "portfolio".
- The fortune voice breaks exactly where it should: the formal
  "a windfall is coming your way" is undercut by "unfortunately".

Runners-up, kept out because each is weaker on one criterion:
- "You will be liquidated, then liberated: the market took your money,
  not your laughter." — warm and rueful, but it leads with the obvious
  liquidation word the brief warns against.
- "You will meet your soulmate at the bottom — of the chart, where you
  sold everything." — a good twist on "the bottom", but the soulmate
  softens the loss instead of joking on it.
- "You will find love, wealth, and a margin call — in that order, and
  only the third is certain." — a good list twist, but "margin call"
  is the obvious term, and the line lectures more than it comforts.
- "The cookie crumbles, the portfolio crumbles, but your sense of
  humour remains unliquidated." — warm, and "unliquidated" is a fine
  last word, but "the cookie crumbles" is a cliche opening.

The program is deterministic: it always writes the same line.
Standard library only; no network, no environment secrets, no reading
of any file outside this repository.
"""

import os
import sys

FORTUNE = (
    "Trader, a windfall is coming your way: unfortunately, it is the "
    "wind that took your portfolio."
)

MAX_CHARS = 160
MAX_WORDS = 20


def gate_check(text: str) -> list[str]:
    """Mirror the bounty gate: UTF-8 text, 1-160 chars, not only whitespace,
    exactly one line, at most 20 words."""
    problems: list[str] = []
    if not text:
        problems.append("empty")
    if text != text.strip():
        problems.append("leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        problems.append(f"{len(text)} chars exceeds {MAX_CHARS}")
    if len(text.split()) > MAX_WORDS:
        problems.append(f"{len(text.split())} words exceeds {MAX_WORDS}")
    if not text.strip():
        problems.append("only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("more than one line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("not valid UTF-8")
    return problems


def main() -> int:
    problems = gate_check(FORTUNE)
    if problems:
        print("gate check failed: " + "; ".join(problems), file=sys.stderr)
        return 1

    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline: the gate counts
    # characters, and a newline would be a wasted character.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)

    # Verify what was written, the same way the gate will read it.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    problems = gate_check(written)
    if problems or written != FORTUNE:
        print("verify failed: " + "; ".join(problems), file=sys.stderr)
        return 1

    print(f"wrote {len(written)} chars, {len(written.split())} words to {out_path}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
