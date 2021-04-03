#!usr/bin/env python3

import prompt

def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    return str(name)

def wrong_answer(answer,right_answer,name):
    print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answer,right_answer,name))
    return 0