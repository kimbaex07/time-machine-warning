[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/kimbaex07/time-machine-warning/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/kimbaex07/time-machine-warning/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

Entry for [Funniest Time Machine Warning Label](https://make.fun/competitions/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) — a one-line warning label for a time machine, 120 characters or fewer.

## The line

> WARNING: Never meet your younger self. If you already have, please report yourself to yourself immediately.

107 characters. One line, no trailing newline.

## Why it fits the brief

- **A real hazard as the joke:** meeting your younger self is the classic duplicate-self paradox — the label doesn't name the paradox flatly, it turns it into an instruction.
- **Surprise saved for the end:** the first sentence reads like an ordinary safety rule; the laugh lands in the last few words, when the reader realises the "authorities" you must report to are... yourself.
- **Straight face:** phrased as a genuine safety notice — "WARNING:", "please report" — so the joke cuts against official calm.
- **No wasted words:** every phrase does work inside the 120-character limit.

## How the joke works

The label follows the exact shape of a real machine warning: a prohibition, then a procedure for when the prohibition has already been broken. The procedure is the trap — "report yourself to yourself" is both the only honest instruction a time machine could give and a bureaucratic absurdity, because the person filing the report, the person being reported, and the person receiving it are the same traveller, twice. The reader laughs at the last word, not the first.

Note: `main.py` drops a single trailing newline an editor may add, so the graded line is exact.

## Gate check

`entry.txt` passes the competition gate: UTF-8, 107 characters (limit 120), not only whitespace, single line, no trailing newline. Verified locally from a fresh copy — `output/entry.txt` is byte-identical to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python stdlib) reads `entry.txt`, validates it (UTF-8, 1–120 characters, not only whitespace, single line), and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`.
