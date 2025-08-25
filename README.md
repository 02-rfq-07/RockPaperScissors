Rock Paper Scissors

This project implements the classic Rock, Paper, Scissors game in Python, enhanced with a Markov Chain–based AI opponent that learns and predicts the player’s next moves.

🎮 Features

  Play Rock, Paper, Scissors against an AI.
  
  AI uses a Markov Chain model to analyze past player moves and predict future ones.
  
  Tracks results: Player wins, AI wins, and ties.
  
  Simulates games against different strategies like Quincy, Abbey, Kris, and Mrugesh for testing AI performance.

📂 Project Structure:

rock-paper-scissors/
│── RPS.py       # Main game logic with Markov AI
│── RPS_game.py
│── main.py   # Run bulk simulations and evaluate win rates
│── README.md           

⚙️ How It Works

Player vs AI

Player selects Rock (R), Paper (P), or Scissors (S).

AI predicts player’s move using transition probabilities from the Markov Chain.

AI chooses the winning move based on the prediction.

Opponent Strategies

  -Quincy: Cycles through moves in a fixed order.
  
  -Abbey: Uses the player’s previous moves to decide.
  
  -Kris: Random strategy with weighted probabilities.
  
  -Mrugesh: Uses more complex transition-based logic.


🚀 Getting Started
1. Clone the Repository
git clone [https://github.com/your-username/rock-paper-scissors-markov.git](https://github.com/02-rfq-07/RockPaperScissors)
cd RockPaperScissors

2. Run the File
python main.py


📊 Example Output
Final results: {'p1': 994, 'p2': 0, 'tie': 5}
Player 1 win rate: 100.0%
vs Quincy: 100.0

Final results: {'p1': 319, 'p2': 363, 'tie': 318}
Player 1 win rate: 46.7%
vs Abbey: 46.7%

Final results: {'p1': 202, 'p2': 297, 'tie': 501}
Player 1 win rate: 40.4%
vs Kris: 40.4%

Final results: {'p1': 638, 'p2': 361, 'tie': 1}
Player 1 win rate: 63.8%
vs Mrugesh: 63.8%

