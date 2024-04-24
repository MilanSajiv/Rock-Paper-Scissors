import random

def get_computer_choice():
    """Randomly pick an option between 'Rock', 'Paper', and 'Scissors'."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_user_choice():
    """Ask the user for an input and return it."""
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().capitalize()
    
    # Validate user input
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().capitalize()
    
    return user_choice

def get_winner(computer_choice, user_choice):
    """Determine the winner based on the classic Rock-Paper-Scissors rules."""
    if computer_choice == user_choice:
        return "It is a tie!"
    elif (computer_choice == "Rock" and user_choice == "Scissors") or \
         (computer_choice == "Paper" and user_choice == "Rock") or \
         (computer_choice == "Scissors" and user_choice == "Paper"):
        return "You lost!"
    else:
        return "You won!"

def play():
    """Play a game of Rock-Paper-Scissors."""
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")
    
    winner = get_winner(computer_choice, user_choice)
    print(winner)

if __name__ == "__main__":
    play()
