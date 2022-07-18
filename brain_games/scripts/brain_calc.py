#!/usr/bin/env python
"""Brain calculator game"""

from brain_games.games.calc import get_question, get_answer
from brain_games.engine import run_game


def main():
    return run_game(get_question, get_answer)


if __name__ == '__main__':
    main()
