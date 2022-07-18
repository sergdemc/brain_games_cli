import random
import prompt


def get_question():
    print('What is the result of the expression?')


def get_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(('+', '-', '*'))
    print('Question: ', num1, operator, num2)
    user_answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(num1, num2, operator)
    return right_answer, user_answer


def get_right_answer(num1: int, num2: int, operator) -> int:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
