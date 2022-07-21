import random


def get_answer():
    """Run brain-progression game:
            return game question and right answer."""
    start_progression = random.randint(0, 20)
    step_progression = random.randint(2, 20)
    len_progression = random.randint(8, 12)
    progression = [start_progression]
    for i in range(len_progression - 1):
        progression.append(progression[-1] + step_progression)
    missing_index = random.randint(0, len(progression) - 1)
    right_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = (
        'What number is missing in the progression?',
        ('Question:', *progression)
    )
    return question, right_answer
