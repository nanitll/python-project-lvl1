#!usr/bin/env python3

import random
import prompt
import math
from brain_games.cli import wrong_answer

def prime_check(number):
    
    if number < 2:
        answer = 'no'
        return answer
    elif number == 2:
        answer = 'yes'
        return answer

    i=2

    limit = int(math.sqrt(number))     
    while i <= limit:
        if number % i == 0:
            answer = "no"
            return answer
        i+=1
    answer = 'yes'    
    return answer

def prime(user_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range (3):
        random_number = random.randint(0,50)
        right_answer = prime_check(random_number)         
        print("Question: {}".format(random_number))
        answer = prompt.string("Your answer: ")
        if answer == right_answer:
            print ("Correct!")
        else:
            wrong_answer(answer,right_answer,user_name)
            return 0
    return 0