#!usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.games.brain_even import even 
from brain_games.scripts.games.brain_calc import calc
from brain_games.scripts.games.brain_gcd import gcd
from brain_games.scripts.games.brain_progression import progression
from brain_games.scripts.games.brain_prime import prime

def menu(user,act):
    while (True):
        if act == "brain-calc": 
            calc(user) 
            act = prompt.string("")
        elif act == "brain-even": 
            even(user) 
            act = prompt.string("")
        elif act == "brain-gcd": 
            gcd(user) 
            act = prompt.string("")
        elif act == "brain-prime": 
            prime(user) 
            act = prompt.string("")
        elif act == "brain-progression": 
            progression(user) 
            act = prompt.string("")
        elif act == "logout" or act == "to be_stopped": break
        else: act = prompt.string("")

def main():
    user = str(welcome_user()) 

    while(True):
        act = prompt.string("") 
        if act == "brain-games": 
            menu(user,act) 
            break 
        if act == "logout" or act == "to be_stopped": break
    return 0
    

    

if __name__ == "__main__":
    main()