import random

def play_game():
    choices = ["rock", "scissors", "paper"]
    computer_count = 0
    user_count = 0

    while True:
        user_input = int(input('''Game Start...
1. Yes  = Game Start
2. No   = Game End
Choose an option: '''))
        
        if user_input == 1:
            for _ in range(1, 9):  # Play 8 rounds
                user_input = int(input('''
1. Rock
2. Scissors
3. Paper
Choose your move: '''))
                
                if user_input == 1:
                    user_choice = "rock"
                elif user_input == 2:
                    user_choice = "scissors"
                elif user_input == 3:
                    user_choice = "paper"
                else:
                    print("Invalid choice, please select 1, 2, or 3.")
                    continue
                
                computer_choice = random.choice(choices)

                print(f"Computer chose: {computer_choice}")
                print(f"You chose: {user_choice}")

                if computer_choice == user_choice:
                    print("Game Draw")
                elif (user_choice == "rock" and computer_choice == "scissors") or \
                     (user_choice == "scissors" and computer_choice == "paper") or \
                     (user_choice == "paper" and computer_choice == "rock"):
                    print("You Win!")
                    user_count += 1
                else:
                    print("Computer Wins!")
                    computer_count += 1

            print("Final Scores:-.............-:")
            print(f"You: {user_count}")
            print(f"Computer: {computer_count}")
            if user_count > computer_count:
                print("Final Result: You win the Game!")
            elif user_count < computer_count:
                print("Final Result: Computer wins the Game!")
            else:
                print("Final Result: Game Draw")
        
        elif user_input == 2:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1 to play or 2 to exit.")

# Start the game
if __name__ == "__main__":
    play_game()
