import random
from random import randint

while True:
    roll_question = input("Roll the dice? (y/n): ").lower()
    if roll_question == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"{dice1}, {dice2}")
    elif roll_question == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid answer.")
