import prompt
import random


def get_question():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_answer():
    n = random.randint(0, 1000)
    print('Question: ', n)
    user_answer = prompt.string('Your answer: ').lower()
    right_answer = is_even(n)
    return right_answer, user_answer


def is_even(n: int) -> str:
    """Return 'yes' if number even or return 'no' if number odd"""
    if n % 2 == 0:
        return 'yes'
    return 'no'
