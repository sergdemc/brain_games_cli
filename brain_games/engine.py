import prompt


def greet_user():
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f"Hello, {username}!")
    return username


def run_game(get_question, get_answer):
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
    if str(user_answer) == str(right_answer):
        return True
    else:
        return False
