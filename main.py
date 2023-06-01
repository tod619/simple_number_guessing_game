# Simply Number Guessing Game
# 01/06/2023
import random


def check_answer(guess, answer):
    """Check the user guess against the answer and return the results"""
    if guess > answer:
        return "Too high!"
    elif guess < answer:
        return "Too Low"
    else:
        return "Correct!"


answer = random.randint(1, 100)

print("Welcome to the number guessing game!!!")
print("The computer is thinking of a number between 1 - 100")
print(answer)
guess = int(input("Make a guess: "))

print(guess)

result = check_answer(guess, answer)
print(result)

# print(answer)
