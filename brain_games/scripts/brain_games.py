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
        act = prompt.string("")
        if act == "brain-calc": calc(user) 
        elif act == "brain-even": even(user) 
        elif act == "brain-gcd": gcd(user) 
        elif act == "brain-prime": prime(user) 
        elif act == "brain-progression": progression(user) 
        else: break

def main():
  

    user = str(welcome_user())  
    print("Hello, {}".format(user)) 
     
    while (True):
        act = prompt.string()
        if act == "brain-calc": calc(user) 
        elif act == "brain-even": even(user) 
        elif act == "brain-gcd": gcd(user) 
        elif act == "brain-prime": prime(user) 
        elif act == "brain-progression": progression(user) 
        else: break
    return 0
    

    

if __name__ == "__main__":
    main()