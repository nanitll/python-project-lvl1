#!usr/bin/env python3

import prompt
import random
import brain_games.cli


def rand_summ():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    summ = x + y
    s = [x, y, str(summ)]
    return s


def rand_diff():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    diff = x - y
    s = [x, y, str(diff)]
    return s


def rand_mult():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    mult = x * y
    s = [x, y, str(mult)]
    return s


def culc_rand():
    rand_i = random.randint(1,3)
    if rand_i == 1:
        s = rand_summ()
        print("Question: {} + {}".format(s[0], s[1]))
        return s[2]
    elif rand_i == 2:
        s = rand_diff()
        print("Question: {} - {}".format(s[0], s[1]))
        return s[2]
    else:
        s = rand_mult()
        print("Question: {} * {}".format(s[0], s[1]))
        return s[2]


def main():

    print("What is the result of the expression?")
    user_name = brain_games.cli.welcome_user()
    for __i in range(3):
        right_answer = culc_rand()        
        answer = prompt.string("You answer: ")
        if (answer == right_answer):
            print ("Correct!")
        else:
            brain_games.cli.wrong_answer(answer, right_answer, user_name)
            return 0
    print("Congratulations, {}!".format(user_name))
    return 0


if __name__ == "__main__":
    main()
