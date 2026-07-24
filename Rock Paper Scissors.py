import random 

choices = ['rock','paper','scissors']

player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    print('\nChoose one : ')
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    player_choice = input("Enter your choice: ").lower()

    if player_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")

    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f'\nScore: You {player_score} and Computer {computer_score}')

if player_score == 3:
    print("\nCongratulations! You won the game!")
else:
    print("\nComputer won the game! Better Luck next time!")