Overview
This is a simple Rock, Paper, Scissors game implemented in Python.
The game allows a player to compete against the computer in a best-of-five rounds format.
The player can choose between "rock," "paper," or "scissors," and the computer randomly selects one of the three options. 
The game keeps track of scores and announces the winner at the end.

Features
Play against the computer.
Best of five rounds.
Score tracking for both player and computer.
Draws are possible, and scores are adjusted accordingly.

Requirements
Python 3.x
No external libraries required.

How to Run
Ensure you have Python installed on your machine.
Copy the code into a Python file (e.g., rock_paper_scissors.py).
Open your terminal or command prompt.
Navigate to the directory where your file is located.
Run the script using the command: python main.py

Gameplay Instructions
When prompted, type your choice: rock, paper, or scissor.
If you enter an invalid option, you will be prompted to choose again.
After each round, the scores will be displayed.
The game will conclude after five rounds, displaying the final scores and announcing the winner.

Code Explanation
Imports: The random module is used to allow the computer to make random choices.
Game Logic: A while loop runs for five rounds, allowing players to input their choice and comparing it against the computer's choice to determine the winner of each round.
Score Tracking: Scores are updated based on the outcomes of each round, with draws resulting in half points for both players.

Contributing
Feel free to fork this repository and make improvements! Pull requests are welcome.
