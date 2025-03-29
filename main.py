# Python Number Guessing Game
import random
Answer = random.randint(1,100)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f" Select a number between {1} and {100} ")

while is_running:
    guess = input(" Enter your guess : ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > 100 or guess < 1 :
            print ("the number is out of the range ")
            print(f" Select a number between {1} and {100} ")
        elif guess < Answer:
            print ("Too low! Try again")
        elif guess > Answer:
            print("Too High! Try again")
        else:
            print(f" CORRECT! The answer was {Answer} ")
            print(f" number of gusses : {guesses} ")
    else:
        print("invalid")
        print(f" Select a number between {1} and {100} ")
