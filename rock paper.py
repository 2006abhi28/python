import random
choices = [
    '''
    Rock
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
    ''',
    '''
    Paper
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
    ''',
    '''
    Scissors
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
    '''
]
# Get user input
user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
# Validate input
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please try again.")
else:
    print(f"You chose:\n{choices[user_choice]}")

    # Computer makes a random choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
