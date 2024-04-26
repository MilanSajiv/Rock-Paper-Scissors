# Computer Vision RPS
This project implements a Rock-Paper-Scissors game that uses a webcam to capture the user's hand gesture and a pre-trained machine learning model to predict the computer's choice. The aim of the project is to provide an interactive and engaging experience for users to play the classic Rock-Paper-Scissors game against the computer.

## What it does
- Captures the user's hand gesture using a webcam.
- Uses a pre-trained machine learning model to predict the computer's choice.
- Implements a countdown timer displayed on the webcam feed.
- Continues the game until either the computer or the user wins three rounds.
- Displays the winner of the game.
    
## Aim of the Project
The main goal of this project is to create a fun and interactive Rock-Paper-Scissors game that showcases the integration of computer vision and machine learning in a real-world application. It aims to provide an enjoyable user experience while demonstrating the capabilities of using a webcam and a machine learning model together in a Python application.

## What I Learned
- Integrating a webcam feed into a Python application using OpenCV.
- Using a pre-trained machine learning model in a Python application.
- Implementing interactive features such as countdown timers in a GUI application.
- Organizing code using object-oriented programming and classes in Python.

## Milestone 1 - Create the computer vision system
Objective: Develop a computer vision system to recognize and classify hand gestures (Rock, Paper, Scissors) from webcam input.

Technologies Used: OpenCV, Keras

Achievements:
- Created a pre-trained machine learning model to classify hand gestures.
- Integrated webcam feed to capture real-time hand gestures.
- Successfully predicted hand gestures with high accuracy.

## Milestone 2 - Create the rock. paper, scissors game
Objective: Implement the classic Rock-Paper-Scissors game logic in Python.

Technologies Used: Python

Achievements:
- Developed a Python script that simulates the Rock-Paper-Scissors game.
- Implemented a user input system to receive Rock, Paper, or Scissors choices.
- Created logic to compare user input with computer choice and determine the winner. 

## Milestone 3 - Use the camera to play rock, paper, scissors game
Objective: Combine the computer vision system and the game logic to create an interactive webcam-enabled Rock-Paper-Scissors game.

Technologies Used: OpenCV, Keras, Python

Achievements:
- Integrated the computer vision system with the Rock-Paper-Scissors game.
- Implemented an interactive countdown timer displayed on the webcam feed.
- Created a round-based scoring system to track computer and user wins.
- Combined all components to offer an engaging and interactive gameplay experience.

## Installation 
- Clone the repository:
```python
git clone https://github.com/MilanSajiv/Rock-Paper-Scissors
```

- Install the required Python packages:
```python
pip install -r requirements.txt
```

- Run the camera_rps.py script to start the game:
```python
python camera_rps.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
