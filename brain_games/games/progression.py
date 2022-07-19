import random
import prompt


def get_question():
    print('What number is missing in the progression?')


def get_answer():
    progression = generate_progression()
    missing_index = random.randint(0, len(progression) - 1)
    missing_num = progression[missing_index]
    progression[missing_index] = '..'
    print('Question:', *progression)
    user_answer = prompt.string('Your answer: ')
    right_answer = missing_num
    return right_answer, user_answer


def generate_progression() -> list:
    """Generate arithmetic progression and return it in list"""
    start_progression = random.randint(0, 20)
    step_progression = random.randint(2, 20)
    len_progression = random.randint(8, 12)
    progression = [start_progression]
    count = 1
    while count <= len_progression:
        progression.append(progression[-1] + step_progression)
        count += 1
    return progression
