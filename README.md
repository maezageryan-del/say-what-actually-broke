# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the make.fun bounty [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5): one line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong and makes them laugh on the way.

## The line (123 characters)

> The server is up. The database is up. The connection between them left for a better job in 2019. Try again in five minutes.

## Why this line

Every dashboard is green and nothing works — the most relatable outage there is. The line names the real failure in plain words (the connection between two healthy systems is dead), gives the user something to do (try again in five minutes), and lands the joke in a single repeatable image: the connection quit its job in 2019. No vague apology, no blaming the user, and short enough to survive being pasted into a real product's error dialog.

## Run it

```sh
python3 main.py
```

It prints the line and writes the same line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
