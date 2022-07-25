#!/usr/bin/env python
"""Brain even game"""

from brain_games.games import even
from brain_games.engine import run_game


def main():
    return run_game(even)


if __name__ == '__main__':
    main()
