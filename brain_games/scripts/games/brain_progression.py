#!usr/bin/env python3
import random
import prompt
from brain_games.cli import wrong_answer

def generate_number_list() :
    number_list=[]
    y = random.randint(1,8)
    z = random.randint(2,6)
    
    for i in range(10) :
        number_list.append(y)
        y = y+z
        
    return number_list

def progression(name_user) :
    print("What number is missing in the progression?")
    for i in range (3) :
        n = random.randint(0,9)
        list_number = generate_number_list()
        right_answer = str(list_number[n])
        list_number[n] = ".."
        print("Question: {}".format(list_number))
        answer = prompt.string("Your answer: ")
        if answer == right_answer:
            print ("Correct!")
        else:
            wrong_answer(answer,right_answer,name_user)
            return 0
    print("Congratulations, {}".format(name_user))




