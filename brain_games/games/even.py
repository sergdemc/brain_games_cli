import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    """Run brain-even game:
            return game question and right answer."""
    n = random.randint(0, 1000)
    question = ('Question:', n)
    if n % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
