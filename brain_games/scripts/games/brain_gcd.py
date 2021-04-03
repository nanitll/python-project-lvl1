#!usr/bin/env python3

import prompt
import random
from brain_games import cli

def calc_gcd(x,y):

    while x != 0 and y !=0:
        if x > y:
            x = x % y
        else:
            y = y % x

    return x+y

def gcd(name):
    
    print("Find the greatest common divisor of given numbers.")
    for i in range(3):
        random_number_one = random.randint(1,50)
        random_number_two = random.randint(1,50)
        print("Question: {} {}".format(random_number_one, random_number_two))
        answer = prompt.string("Your answer: ")
        right_answer = calc_gcd(random_number_one, random_number_two)
        if answer == str(right_answer):
            print("Correct!")
        else:
            cli.wrong_answer(answer, right_answer, name)
            return 0
    print("Congratulations, {}".format(name))