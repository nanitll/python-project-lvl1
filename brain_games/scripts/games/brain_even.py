#!usr/bin/env python3

import prompt
import random
from brain_games.cli import wrong_answer
        
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
        right_answer = checking_answer(random_number)
        if (right_answer == answer):
            print("Correct!")
        else:
            wrong_answer(answer, right_answer, name)
            return 0
        
    print("Congratulations, {}!".format(name))