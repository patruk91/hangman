import hmfunc
import os


def main():
    os.system("clear")
    hmfunc.show_title()
    name = input("Enter your name: ")

    os.system("clear")
    again = True
    while again:
        # Set default values.
        defaults = hmfunc.set_defaults()
        lives = defaults[0]
        win_condition = defaults[1]
        attempt_count = defaults[2]
        start = defaults[3]
        list_wrong_letters = defaults[4]

        # Get random capital, split to list of [capital's letters, dash
        # letters]
        capital = hmfunc.get_random_capital_name()
        list_of_chars = hmfunc.show_char_of_capital(capital[1])
        dash_letters = list_of_chars[1]

        # Set program to demo mode.
        hmfunc.demo_mode(capital)

        while lives > 0 and win_condition:
            attempt_count += 1

            # Check if user input is correct
            message = hmfunc.handle_user_input()
            check_message = hmfunc.check_if_input_correct(
                message, list_of_chars)
            if check_message[0]:
                dash_letters = hmfunc.write_dash_letters(
                    message, list_of_chars[1], check_message[1])
            else:
                lives = hmfunc.decrease_life(lives, check_message[2])
                list_wrong_letters = hmfunc.wrong_letters_append(
                    message, list_wrong_letters)
            # Check if user guessed capital correct.
            hmfunc.show_hangman(lives)
            if hmfunc.check_success(dash_letters, list_of_chars[0]):
                win = hmfunc.set_win_conditions(start)
                win_condition = win[0]

                # Show user results, add score to file, show top 10 high score.
                os.system("clear")
                hmfunc.show_user_result(capital[1], attempt_count, win[1])
                hmfunc.add_high_score(name, win[1], capital[1])
                hmfunc.show_high_score()
            else:
                hmfunc.show_all(
                    dash_letters,
                    list_wrong_letters,
                    lives,
                    capital[0])

        hmfunc.looser_screen(capital, lives, win_condition)
        again = hmfunc.restart()


if __name__ == '__main__':
    main()
