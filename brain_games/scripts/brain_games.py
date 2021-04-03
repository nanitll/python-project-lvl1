#!usr/bin/env python3
# in /home/nanit/python-project-lvl1

from brain_games.cli import welcome_user
from brain_even import even
from brain_calc import calc

def main():
    print("Welcome to the Brain Games!")
    user = str(welcome_user())    
    #even(user)
    calc(user)


    

if __name__ == "__main__":
    main()