#!usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_even import even 
from brain_games.scripts.games.brain_calc import calc
from brain_games.scripts.games.brain_gcd import gcd
from brain_games.scripts.games.brain_progression import progression

def main():
    print("Welcome to the Brain Games!")
    user = str(welcome_user())    
    #even(user)
    #calc(user)
    #gcd(user)
    progression(user)
    
    return 0

    

if __name__ == "__main__":
    main()