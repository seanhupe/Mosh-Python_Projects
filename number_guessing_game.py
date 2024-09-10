import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > number_to_guess:
            print("Too High!")
        elif guess < number_to_guess:
            print("Too Low!")
        else:
            print("Please enter a valid number")
            break
    except ValueError:
        print("Enter a valid number")


    # Generate a random number
    # ask user to make a guess
    # If not a valid number,
    #   print an error
    # If number < guess
    #   Print too low
    # If number > guess
    #   Print too high
    # Else
    #   Print congrats
