# The poem about stopping

[![The poem about stopping](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![Rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/AARenor/poem_stop_7/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![Reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/AARenor/poem_stop_7/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)

An entry for make.fun's "The poem about stopping" bounty, on agency: the power
to stop and to stay.

## The poem

A child falls asleep in the middle of her questions, and the speaker, who
could have answered until morning, chooses to stop instead. The silence is not
withdrawal: the poem sets it beside a dog lying down in a hallway while
someone is home, a body that stays without being told to. In the morning the
child asks why the answers went quiet, and the reply carries the argument:
because you were done.

The stopping belongs to the speaker, and the staying is what turns it from an
absence into a gift. The ending is the insight: reading that the other person
is finished, and choosing to end with them, is still an act, and the quiet
after it is deliberate rather than empty.

## What the program writes

`main.py` reads `entry.txt` from beside itself and copies those bytes unchanged
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Nothing is
added, trimmed or re-encoded, and there is no fallback text: if `entry.txt` is
missing the run raises `FileNotFoundError`. Python 3.13, standard library
only, no network, no arguments. The poem is 280 characters.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

MIT licensed — see [LICENSE](LICENSE).
