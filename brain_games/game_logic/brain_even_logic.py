import prompt
import random

name = ''


def greet_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!", '\n')


def start_brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        n = random.randint(0, 1000)
        print('Question: ', n)
        answer = prompt.string('Your answer: ').lower()
        right_answer = is_even(n)
        if answer == right_answer:
            count += 1
            print('Correct!')
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def is_even(n: int) -> str:
    """Return 'yes' if number even or return 'no' if number odd"""
    if n % 2 == 0:
        return 'yes'
    return 'no'
