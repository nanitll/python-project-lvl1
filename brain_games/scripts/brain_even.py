#!usr/bin/env python3

import prompt
import random
        
def checking_answer(number):
    if number%2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return correct_answer

def pool(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    for i in range(3):
        i = random.randint(1,50)

        print("Question: {}".format(i))
        answer = prompt.string(prompt = "You answer: ")

        if checking_answer(i) == answer:
            print("Correct!")
        elif (checking_answer == "yes"):
            print("'{}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, Bill!".format(answer))
            return 0
        elif (checking_answer == "no"):
            print("'{}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, Bill!".format(answer))
            return 0
    print("Congratulations, {}!".format(name))