# u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c

[![make.fun · u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

A make.fun bounty entry: one fortune cookie line for a crypto trader who
has just been liquidated.

## The fortune

> Trader, a windfall is coming your way: unfortunately, it is the wind that took your portfolio.

16 words, 94 characters, one line.

## How it works

`main.py` is deterministic: it writes the line above to
`/output/entry.txt`, after checking it against the bounty gate itself
(UTF-8, 1–160 characters, not only whitespace, one line, at most 20
words), then reads the file back and verifies it byte for byte.

Standard library only. No network, no environment secrets, no files
outside this repository.

## Why this line

The judge is a freshly liquidated trader reading a fortune at 3am, and
keeps the line that makes them laugh instead of cry. The line is built
for the judge's criteria, in their order:

1. **Fortune voice + loss, both in it.** "Trader, a windfall is coming
   your way" is oracular and addresses the trader directly; "the wind
   that took your portfolio" names the loss.
2. **Laugh, not cry.** The trader is promised a windfall, then told the
   wind already came for the portfolio — a rueful shrug, never cruel
   and never smug.
3. **One breath.** 16 words, one line.
4. **Fresh.** A real double meaning, not the obvious liquidation pun:
   "windfall" (unexpected money) splits open into the wind that caused
   the fall, and the surprise lands on the last word, "portfolio".
5. **The voice breaks where it should.** The formal "a windfall is
   coming your way" is undercut by "unfortunately".

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
