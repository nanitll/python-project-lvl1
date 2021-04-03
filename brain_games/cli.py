import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}".format(name))
    return str(name)

    
def wrong_answer(answer, right_answer, name = ''):
    if name == '':
        print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answer, right_answer))
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answer, right_answer, name))
    return 0
