# Simply Number Guessing Game
# 01/06/2023
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    """Check the user guess against the answer and return the results"""
    if guess > answer:
        return "Too high!"
    elif guess < answer:
        return "Too Low"
    else:
        return f"Well done you got it right! the answer was {answer}"


def set_difficulty():
    """Create a Function to set the dificulty of the game"""
    level = input("Choose a difficulty easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def game():
    answer = random.randint(1, 100)

    print("Welcome to the number guessing game!!!")
    print("The computer is thinking of a number between 1 - 100")
    # print(answer)
    turns = set_difficulty()
    guess = 0
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = check_answer(guess, answer)
        print(result)
        turns -= 1
    if turns == 0:
        print("You ran out of lives. GAME OVER!!!")


game()

input("\nPress Enter to exit the program")

# print(answer)
