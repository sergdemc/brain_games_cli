import random


def get_answer():
    """Run brain-prime game:
        return game question and right answer."""
    number = random.randint(1, 100)
    question = (
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        ('Question:', number)
    )
    if number % 2 == 0 and number != 2 or number < 2:
        right_answer = 'no'
        return question, right_answer
    divisor = 3
    while divisor ** 2 <= number:
        if number % divisor == 0:
            right_answer = 'no'
            return question, right_answer
        divisor += 2
    right_answer = 'yes'
    return question, right_answer
