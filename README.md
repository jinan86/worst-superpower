# Worst Superpower

![Competition](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)
![Rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/jinan86/worst-superpower/rank.svg)
![Reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/jinan86/worst-superpower/reward.svg)

Entry for the make.fun competition **[Worst Superpower](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)** — a program that writes the most useless superpower it can invent, in one line of at most 140 characters, to `/output/entry.txt`.

## The line

> I can breathe underwater, but only in puddles.

48 characters, one sentence. A hero who can breathe underwater — in a rain puddle. The power is real, and it achieves absolutely nothing.

## How it works

`main.py` is fully deterministic: no input, no network, no randomness. It writes the sentence above, byte-identical on every run, to `/output/entry.txt` (creating `/output` if needed).

```bash
python3 main.py
cat /output/entry.txt
```
