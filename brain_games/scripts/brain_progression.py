#!/usr/bin/env python
"""Brain progression game"""

from brain_games.games.progression import get_answer
from brain_games.engine import run_game


def main():
    return run_game(get_answer)


if __name__ == '__main__':
    main()
