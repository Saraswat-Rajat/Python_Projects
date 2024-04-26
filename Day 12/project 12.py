# NUMBER GUSSER GAME
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high. ")
        return turns - 1
    elif (guess < answer):
        print("too low")
        return turns - 1
    else:
        print(f"You got it! the answer was {answer}.")


def set_difficulty():
    level = input("choose your difficulty , type 'easy' or 'hard' : ")

    if level == 'easy':

        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guesser ")
    print("I'm thinking of a number between 1 and 100 ")

    answer = randint(1, 100)
    print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while (guess != answer):

        print(f"you have {turns} attempts remaining to guess the number ")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("you've ran out of guesses, you loose")
            return


game()
