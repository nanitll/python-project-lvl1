#!usr/bin/env python3

import random
import prompt
import brain_games.cli


def generate_number_list():
    number_list = []
    y = random.randint(1, 8)
    z = random.randint(2, 6)

    for __i in range(10):
        number_list.append(str(y))
        y = y + z

    return number_list


def main():
    name_user = brain_games.cli.welcome_user()
    print("What number is missing in the progression?")
    for __i in range(3):
        n = random.randint(0, 9)
        list_number = generate_number_list()
        right_answer = list_number[n]
        list_number[n] = ".."
        print("Question: {}".format(' '.join(list_number)))
        answer = prompt.string("Your answer: ")
        if answer == right_answer:
            print("Correct!")
        else:
            brain_games.cli.wrong_answer(answer, right_answer, name_user)
            return 0
    print("Congratulations, {}!".format(name_user))
    return 0


if __name__ == "__main__":
    main()
