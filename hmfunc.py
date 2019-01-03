import os
import time
import sys
from random import randint


def demo_mode(capital):
    """
    Enter program in demo mode. Show randomly chosen capital.
    :param capital: chosen capital
    """
    try:
        if sys.argv[1] == "--demo":
            print(capital[1])
    except IndexError:
        pass


def decrease_life(live_to_decrease, amount):
    """
    Decrease life depending on the provided amount.
    :param live_to_decrease: live which player have
    :param amount: amount do decrease, depending on user input
    :return: new amount of life
    """
    live_to_decrease -= amount
    return live_to_decrease


def set_defaults():
    """
    Set default values in game options.
    :return: parameters to main function
    """
    lives = 5
    win_condition = True
    attempt_count = 0
    start = time.time()
    list_wrong_letters = []
    return lives, win_condition, attempt_count, start, list_wrong_letters


def get_random_capital_name():
    """
    Take a random capital name form the file (capitals.txt).
    :return: randomly chosen capital
    """
    filename = "capitals.txt"
    with open(filename) as file_object:
        lines = file_object.readlines()
        line_number = randint(0, len(lines))
        capital = lines[line_number].rstrip().split(" | ")
        return capital


def show_char_of_capital(capital):
    """
    Transform the capital name into two list [letters, letters as dashes]
    :param capital: capital name in string
    :return: list of characters or underscores "_"
    """
    char_of_capital = list(capital.lower())
    dash_of_capital = ["_" if index != " " else
                       " " for index in char_of_capital]
    return char_of_capital, dash_of_capital


def handle_user_input():
    """
    Ask user to put character or whole word.
    :return: lower cased user input
    """
    message = input("\nEnter letter or a whole word: ")
    os.system("clear")
    return message.lower()


def check_if_input_correct(message, list_of_chars):
    """
    Check if this is a word or char. Then go to appropriate function.
    :param message: user input
    :param list_of_chars: list of characters with letters
    :return: in case of letter: correctness [True/False], list of index,
             where letter is, amount of lives to decrease;
             in case of word: correctness [True/False], empty list of index,
             amount of lives to decrease
    """
    if len(message) == 1:
        letters = handle_letter(message, list_of_chars[0])
        amount = 1
        return letters[0], letters[1], amount
    else:
        word = handle_word(message, list_of_chars[0])
        amount = 2
        return word, [], amount


def handle_letter(letter, list_of_chars):
    """
    Check if letter is in list of characters from capital.
    :param letter: user input
    :param list_of_chars: list of characters
    :return: correctness [True/False], list of index where letter is,
    """
    list_index = []
    correct = False
    if letter in list_of_chars:
        for index in range(len(list_of_chars)):
            if letter == list_of_chars[index]:
                list_index.append(index)
        correct = True
    return correct, list_index


def handle_word(message, list_of_chars):
    """
    Check if list from user input is the same
    as list of characters from capital.
    :param message: user input
    :param list_of_chars: list of characters
    :return: correctness [True/False]
    """
    correct = False
    if list(message) == list_of_chars:
        correct = True
    return correct


def write_dash_letters(letter, dash_of_capital, index_letters=[]):
    """
    In case of letter: replace underscore "_" with appropriate letters
    In case of word: replaces underscores "_" with all letters
    :param letter: list from user input
    :param dash_of_capital: list of underscore "_" from capital list
    :param index_letters: indexes of letter in capital in list of characters
    :return: switched underscores with appropriate letter or whole word
    """
    if len(index_letters) != 0:
        for index in index_letters:
            dash_of_capital[index] = letter
        return dash_of_capital
    else:
        dash_of_capital = list(letter)
        return "".join(dash_of_capital)


def check_success(dash_of_capital, char_of_capital):
    """
    Checking if list of characters are the same with list
    of changed underscores.
    :param dash_of_capital: list of underscores
    :param char_of_capital:  list of characters
    :return: True/False
    """
    dash_of_capital = list(dash_of_capital)
    if dash_of_capital == char_of_capital:
        return True
    else:
        return False


def restart():
    """
    Ask user if he want play agin. If yes restart program.
    :return: True/False
    """
    answer = input("\nAgain? [y/n]: ")
    os.system("clear")
    if answer.lower() == "y":
        return True
    else:
        return False


def wrong_letters_append(message, list_wrong_letters):
    """
    Makes a list of wrong answers.
    :param message: wrong answers from user input
    :param list_wrong_letters: actual wrong list
    :return: wrong letters in list
    """
    list_wrong_letters.append(message)
    return list_wrong_letters


def show_all(dash_letters, wrong_letters, lives, country):
    """
    Print on the screen informations about: hint, wrong answers, attempts.
    :param dash_letters: actual state of guessing
    :param wrong_letters: actual state of wrong answers
    :param lives: actual amount of tries
    :param country: Country for hint.
    """
    if lives <= 2:
        print("\nHint: ", end="")
        print("What is capital of " + country.title() + "?\n")
    print(" ".join(dash_letters))
    print('\nWrong answers: ', end="")
    print(', '.join(wrong_letters))
    print("Attempts left: ", lives)


def add_high_score(name, win_time, capital):
    """
    Append user result to file.
    :param name: name of user
    :param win_time: time to finished game
    :param capital: capital
    """
    with open("high_score.txt", "a") as file_object:
        file_object.write(
            "{}|{}|{}|{}\n".format(
                name.title(),
                time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.gmtime()),
                round(
                    win_time /
                    len(capital)),
                capital))


def show_high_score():
    """
    Prints out top ten of high scores from file.
    """
    result = []
    with open("high_score.txt") as file_object:
        for line in file_object:
            line = line.rstrip().split("|")
            line[2] = int(line[2])
            result.append(line)
    handle_high_score_formatting(result)


def calculate_max_sizes(result):
    """
    Calcualte sizes of length of columns for high score table.
    :param result: list of high scores
    :return: lenght of name, date, capital, <-- max len from this,
    sorted results
    """
    size_of_name = 0
    size_of_date = 0
    size_of_capital = 0
    for i in result:
        if size_of_name < len(i[0]):
            size_of_name = len(i[0])
        if size_of_date < len(i[1]):
            size_of_date = len(i[1])
        if size_of_capital < len(i[3]):
            size_of_capital = len(i[3])
    result_sorted = sorted(result, key=lambda x: x[2])

    if len(result_sorted) < 10:
        max_len = len(result_sorted)
    else:
        max_len = 10
    return size_of_name, size_of_date, size_of_capital, max_len, result_sorted


def handle_high_score_formatting(result):
    """
    Dynamically print out high scores tables.
    :param result: list of high scores
    """
    calculated_sizes = calculate_max_sizes(result)
    size_of_name = calculated_sizes[0]
    size_of_date = calculated_sizes[1]
    size_of_capital = calculated_sizes[2]
    max_len = calculated_sizes[3]
    result_sorted = calculated_sizes[4]

    print("TOP 10 HIGH SCORE: ")
    print(
        "{:<3}|{:^{s_o_n}}|{:^{s_o_d}}|{:^{x}}|{:^{s_o_c}}|" .format(
            "LP",
            "NAME",
            "DATE",
            "SCORE",
            "CAPITAL",
            s_o_n=size_of_name + 3,
            s_o_d=size_of_date + 3,
            x=10,
            s_o_c=size_of_capital + 3))
    print("-" * (size_of_name + size_of_date + size_of_capital + 27))

    i = 1
    for line in result_sorted[:max_len]:
        print(
            "{:<3}|{:^{s_o_n}}|{:^{s_o_d}}|{:^{x}}|{:^{s_o_c}}|" .format(
                i,
                line[0],
                line[1],
                line[2],
                line[3],
                s_o_n=size_of_name + 3,
                s_o_d=size_of_date + 3,
                x=10,
                s_o_c=size_of_capital + 3))
        i += 1


def show_user_result(capital, attempt_count, win_time):
    """
    Shows user result in case of victory.
    :param capital: selected capital from file
    :param attempt_count: amount of tries
    :param win_time: time in which user guess capital
    """
    print("\nVICTORY!")
    print("You guess " +
          capital +
          " in " +
          str(attempt_count) +
          " guesses. "
          "It took you, " +
          str(round(win_time)) +
          " seconds.\n\n")


def set_win_conditions(start_time):
    """
    Calculate win time and sets parameter win condition to break game
    :param start_time: time when user start game
    :return: True/False, time
    """
    win_condition = False
    win_time = time.time() - start_time
    return win_condition, win_time


def looser_screen(capital, lives, win_condition):
    """
    Display a hangman ASCII art, when user loose game, what was the answer.
    :param capital: chosen capital
    :param lives: actual amount of lives,
    :param win_condition: True/False
    """
    if lives == 0 or lives == -1 and win_condition:
        os.system("clear")
        with open("hangman.txt") as my_file:
            lines = my_file.readlines()[51:60]
            for i in lines:
                print(i.rstrip())
        print("\nThe answer was: " + capital[1])
        print("Better luck next time!")


def print_hangman(begin_line, end_line):
    """
    Display a hangman ASCII art.
    :param begin_line: read line from the file
    :param end_line: read line from the file
    """
    with open("hangman.txt") as my_file:
        lines = my_file.readlines()[begin_line:end_line]
        for i in lines:
            print(i.rstrip())


def show_hangman(lives):
    """
    Read actual lines, depending on amount of life.
    :param lives: actual amount of life
    :return: print_hangman()
    """
    if lives == 5:
        print_hangman(1, 10)
    elif lives == 4:
        print_hangman(11, 20)
    elif lives == 3:
        print_hangman(21, 30)
    elif lives == 2:
        print_hangman(31, 40)
    elif lives == 1:
        print_hangman(41, 50)


def show_title():
    """
    Show a title of game.
    """
    with open("title.txt") as file_object:
        for line in file_object:
            print(line.rstrip())
        print()


if __name__ == '__main__':
    main()
