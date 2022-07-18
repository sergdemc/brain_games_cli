import prompt


def greet_user() -> str:
    """Print invite to Brain Games, ask username, return username"""
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f"Hello, {username}!")
    return username


def run_game(get_question, get_answer):
    """Run common logic of games;
    Run greeting func;
    Run check func for user_answer;
    Print messages to user.
    """
    username = greet_user()
    count = 0
    while count != 3:
        if count == 0:
            get_question()
        right_answer, user_answer = get_answer()
        if check_answer(right_answer, user_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")


def check_answer(right_answer, user_answer) -> bool:
    """Return True if right_answer == user_answer, otherwise return False"""
    if str(user_answer) == str(right_answer):
        return True
    else:
        return False
