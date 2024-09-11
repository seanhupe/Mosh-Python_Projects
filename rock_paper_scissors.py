import random

emojis = {
    'r': '🪨',
    's': '✂️',
    'p': '📃',
}

choices = ('r', 'p', 's')
user_choice = input("rock, paper, scissors? (r/p/s): ").lower()

if user_choice not in choices:
    print("Invalid selection!")

computer_choice = random.choice(choices)

print(f"You chose {emojis[user_choice]}")
print(f"Computer chose {emojis[computer_choice]}")



# Ask user to make a choice
# if not valid
#   print error
# Let the computer make a choice
# Print choices (emojis)
# Determine winner
# Ask if they want to play again
# if not
#   terminate
