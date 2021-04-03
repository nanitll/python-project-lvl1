#!usr/bin/env python3

import prompt
import random
from brain_games.cli import wrong_answer 


def rand_summ():
    x = random.randint(0,10)
    y = random.randint(0,10)
    summ = x + y
    s = [x,y,str(summ)]
    return s

def rand_diff():
    x = random.randint(0,10)
    y = random.randint(0,10)
    diff = x - y
    s = [x,y,str(diff)]
    return s

def rand_mult():
    x = random.randint(0,10)
    y = random.randint(0,10)
    mult = x * y
    s = [x,y,str(mult)]
    return s

def calc(name):
    print("Welcome to the Brain Games!")
    print("What is the result of the expression?")
    for i in range (3):
        rand_i = random.randint(1,3)
        if rand_i == 1:
            s = rand_summ()
            print("{} + {}".format(s[0],s[1]))
        elif rand_i == 2:
            s = rand_diff()
            print("{} - {}".format(s[0],s[1]))
        else:
            s = rand_mult()
            print("{} * {}".format(s[0],s[1]))
            
        answer = prompt.string("You answer: ")
        if (answer == s[2]):
            print ("Correct!")
        else:
            wrong_answer(answer,s[2])
            return 0
    print("Congratulations, {}!".format(name))
    return 0