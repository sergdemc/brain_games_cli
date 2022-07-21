import random


def get_answer():
    """Run brain-gcd game:
            return game question and right answer."""
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = (
        'Find the greatest common divisor of given numbers.',
        ('Question:', num1, num2)
    )
    right_answer = get_right_answer(num1, num2)
    return question, right_answer


def get_right_answer(num1: int, num2: int) -> int:
    """Return greatest common divisor"""
    if num2 == 0:
        return num1
    return get_right_answer(num2, num1 % num2)
