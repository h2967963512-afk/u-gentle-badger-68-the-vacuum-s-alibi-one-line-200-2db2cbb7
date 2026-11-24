"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is a robot vacuum's deadpan excuse for a missed spot:
# the crumbs are a protected habitat, and no dust-bunny family gets
# evicted before breakfast.
import os

TEXT = (
    "I did not miss that spot \u2014 my lidar classified the crumbs "
    "as a protected habitat, and I refuse to evict a family of dust "
    "bunnies before breakfast."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 146 characters: deadpan alibi, punch at the end.
