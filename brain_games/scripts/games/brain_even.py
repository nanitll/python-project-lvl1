#!usr/bin/env python3

import prompt
import random
        
def checking_answer(number):
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return correct_answer

def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = random.randint(1,50)
        print("Question: {}".format(random_number))
        answer = prompt.string("You answer: ")

        if (checking_answer(random_number) == answer):
            print("Correct!")
        elif (checking_answer(random_number) == "yes"):
            print("'{}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {}!".format(answer,name))
            return 0
        elif (checking_answer(random_number) == "no"):
            print("'{}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {}!".format(answer,name))
            return 0
    print("Congratulations, {}!".format(name))