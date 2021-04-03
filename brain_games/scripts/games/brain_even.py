#!usr/bin/env python3

import prompt
import random
import brain_games.cli
        
def checking_answer(number):
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer

def main():
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for __i in range(3):
        random_number = random.randint(1,50)
        print("Question: {}".format(random_number))
        answer = prompt.string("You answer: ")
        right_answer = checking_answer(random_number)
        if (right_answer == answer):
            print("Correct!")
        else:
            brain_games.cli.wrong_answer(answer, right_answer, user_name)
            return 0
    print("Congratulations, {}!".format(user_name))
    return 0

if __name__ == "__main__":
    main()