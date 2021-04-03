#!usr/bin/env python3

import random
import prompt
import math
import brain_games.cli


def prime_check(number):
    if number < 2:
        answer = "no"
        return answer
    elif number == 2:
        answer = "yes"
        return answer

    i = 2

    limit = int(math.sqrt(number))
    while i <= limit:
        if number % i == 0:
            answer = "no"
            return answer
        i += 1
    answer = "yes"
    return answer


def main():
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for __i in range(3):
        random_number = random.randint(0, 50)
        right_answer = prime_check(random_number)
        print("Question: {}".format(random_number))
        answer = prompt.string("Your answer: ")
        if answer == right_answer:
            print("Correct!")
        else:
            brain_games.cli.wrong_answer(answer, right_answer, user_name)
            return 0

    print("Congratulations, {}!".format(user_name))
    return 0


if __name__ == "__main__":
    main()
