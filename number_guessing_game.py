import random

number_to_guess = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed the number")
        break
    elif guess > number_to_guess:
        print("Too High!")
    elif guess < number_to_guess:
        print("Too Low!")
    else:
        print("Please enter a valid number")
