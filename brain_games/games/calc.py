import random


def get_answer():
    """Run brain-calc game:
            return game question and right answer."""
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(('+', '-', '*'))
    question = (
        'What is the result of the expression?',
        ('Question:', num1, operator, num2)
    )
    if operator == '+':
        right_answer = num1 + num2
    elif operator == '-':
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return question, right_answer
