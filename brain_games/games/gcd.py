import random
import prompt


def get_question():
    print('Find the greatest common divisor of given numbers.')


def get_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    print('Question: ', num1, num2)
    user_answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(num1, num2)
    return right_answer, user_answer


def get_right_answer(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    return get_right_answer(num2, num1 % num2)
