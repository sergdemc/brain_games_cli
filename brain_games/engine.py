import prompt


def run_game(get_answer):
    """
    Run common logic of games:
    greet user, check user_answer, print messages to user.
    """
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f"Hello, {username}!")
    COUNT_OF_ROUNDS = 3
    for game_round in range(COUNT_OF_ROUNDS):
        question, right_answer = get_answer()
        if game_round == 0:
            print(question[0])
        print(*question[1])
        user_answer = prompt.string('Your answer: ').lower()
        if str(right_answer) == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
