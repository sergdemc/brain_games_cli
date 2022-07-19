import random
import prompt


def get_question():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_answer():
    number = random.randint(1, 100)
    print('Question:', number)
    user_answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(number)
    return right_answer, user_answer


def get_right_answer(number: int) -> str:
    """Returns 'yes', if `number` is prime, otherwise returns 'no'"""
    if number % 2 == 0 and number != 2 or number < 2:
        return 'no'
    divisor = 3
    while divisor ** 2 <= number:
        if number % divisor == 0:
            return 'no'
        divisor += 2
    return 'yes'
