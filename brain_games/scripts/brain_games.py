#!usr/bin/env python3

from brain_games.cli import welcome_user
from .brain_even import pool

def main():
    print("Welcome to the Brain Games!")
    user = str(welcome_user())    
    pool(user)

    

if __name__ == "__main__":
    main()