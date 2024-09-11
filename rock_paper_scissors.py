import random

emojis = {
    'r': '🪨',
    's': '✂️',
    'p': '📃',
}
choices = ('r', 'p', 's')

while True:
    user_choice = input("rock, paper, scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid selection!")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == "p") or
            (user_choice == 'p' and computer_choice == "r")):
        print("You Win!")
    else:
        print("You LOSER!")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        break

# Ask user to make a choice
# if not valid
#   print error
# Let the computer make a choice
# Print choices (emojis)
# Determine winner
# Ask if they want to play again
# if not
#   terminate
