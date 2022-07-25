#!/usr/bin/env python
"""Brain calculator game"""

from brain_games.games import calc
from brain_games.engine import run_game


def main():
    return run_game(calc)


if __name__ == '__main__':
    main()
