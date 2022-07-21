#!/usr/bin/env python
"""Brain even game"""

from brain_games.games.even import get_answer
from brain_games.engine import run_game


def main():
    return run_game(get_answer)


if __name__ == '__main__':
    main()
