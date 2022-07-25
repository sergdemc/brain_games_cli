import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game():
    """Run brain-prime game:
        return game question and right answer."""
    number = random.randint(1, 100)
    question = ('Question:', number)
    right_answer = is_prime(number)
    return question, right_answer


def is_prime(number: int) -> str:
    if number % 2 == 0 and number != 2 or number < 2:
        return 'no'
    divisor = 3
    while divisor ** 2 <= number:
        if number % divisor == 0:
            return 'no'
        divisor += 2
    return 'yes'
