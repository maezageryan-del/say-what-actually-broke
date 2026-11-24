"""Say What Actually Broke — one line of honest error copy.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)
and prints exactly the same line to stdout.
"""

import os

LINE = "The server is up. The database is up. The connection between them left for a better job in 2019. Try again in five minutes."


def main():
    # The harness (program/v1) grades /output/entry.txt; honour the
    # output-dir override when the sandbox sets one, else use /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
