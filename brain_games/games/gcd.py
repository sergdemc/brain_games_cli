import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    """Run brain-gcd game:
            return game question and right answer."""
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = ('Question:', num1, num2)
    right_answer = gcd(num1, num2)
    return question, right_answer


def gcd(num1: int, num2: int) -> int:
    """Return greatest common divisor"""
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)
