#!/usr/bin/env python
"""Brain greatest-common-divisor game"""

from brain_games.games import gcd
from brain_games.engine import run_game


def main():
    return run_game(gcd)


if __name__ == '__main__':
    main()
