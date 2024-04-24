import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissorsGame:
    def __init__(self, model_path='keras_model.h5'):
        self.model = load_model(model_path)
        self.cap = cv2.VideoCapture(0)
        self.computer_wins = 0
        self.user_wins = 0

    def get_model_prediction(self, frame):
        """Get prediction from the computer vision model."""
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        normalized_image = (resized_frame.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image
        prediction = self.model.predict(data)
        probabilities = prediction[0].tolist()
        return probabilities

    def get_computer_choice_from_prediction(self, probabilities):
        """Convert model prediction probabilities to a choice."""
        classes = ["Rock", "Paper", "Scissors", "Nothing"]
        index = probabilities.index(max(probabilities))
        return classes[index]

    def get_user_choice(self):
        """Ask the user for an input and return it."""
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().capitalize()
        while user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")
            user_choice = input("Enter your choice (Rock, Paper, Scissors): ").strip().capitalize()
        return user_choice

    def get_winner(self, computer_choice, user_choice):
        """Determine the winner based on the classic Rock-Paper-Scissors rules."""
        if computer_choice == user_choice:
            return "It is a tie!"
        elif (computer_choice == "Rock" and user_choice == "Scissors") or \
             (computer_choice == "Paper" and user_choice == "Rock") or \
             (computer_choice == "Scissors" and user_choice == "Paper"):
            self.computer_wins += 1
            return "Computer wins!"
        else:
            self.user_wins += 1
            return "You win!"

    def display_countdown(self):
        """Display countdown on the webcam feed."""
        start_time = time.time()
        countdown_time = 3
        elapsed_time = 0
        while True:
            ret, frame = self.cap.read()
            elapsed_time = time.time() - start_time
            remaining_time = countdown_time - int(elapsed_time)
            
            cv2.putText(frame, str(remaining_time), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            cv2.imshow('Rock-Paper-Scissors', frame)
            
            if remaining_time <= 0:
                break
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def play(self):
        """Play a game of Rock-Paper-Scissors."""
        while self.computer_wins < 3 and self.user_wins < 3:
            print(f"\nComputer wins: {self.computer_wins}, User wins: {self.user_wins}")
            print("Get ready to show your hand!")
            
            self.display_countdown()
            
            probabilities = self.get_model_prediction(frame)
            computer_choice = self.get_computer_choice_from_prediction(probabilities)
            
            user_choice = self.get_user_choice()
            
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            
            winner = self.get_winner(computer_choice, user_choice)
            print(winner)
            
            input("Press Enter to continue to the next round...")

        print("\nGame Over!")
        if self.computer_wins > self.user_wins:
            print("Computer wins the game!")
        else:
            print("You win the game!")
        
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
