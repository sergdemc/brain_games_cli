#!/usr/bin/env python
"""Brain progression game"""

from brain_games.games import progression
from brain_games.engine import run_game


def main():
    return run_game(progression)


if __name__ == '__main__':
    main()
