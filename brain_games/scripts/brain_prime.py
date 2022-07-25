#!/usr/bin/env python
"""Brain prime game"""

from brain_games.games import prime
from brain_games.engine import run_game


def main():
    return run_game(prime)


if __name__ == '__main__':
    main()
