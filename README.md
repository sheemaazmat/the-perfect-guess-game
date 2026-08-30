🎯 The Perfect Guess
A simple number guessing game built with Python where the computer generates a random number and the player tries to guess it.

📌 About the Project
In this game, the computer randomly generates a number between 1 and 100. The player keeps entering guesses until they find the correct number.
After each guess, the program provides a hint:

* If the guess is too high → "Lower number please"
* If the guess is too low → "Higher number please"
* If the guess is correct → "You guessed it!"

The program also keeps track of the number of attempts made by the player.

✨ Features

* 🎲 Generates a random number between 1 and 100
* ⌨️ Takes guesses from the user
* 💡 Provides higher/lower hints
* 🔢 Counts the number of guesses
* 🏆 Displays the result when the correct number is guessed
* 💻 Simple command-line interface

🛠️ Technologies Used

* Python 3
* random module

🧠 Python Concepts Practiced
This project helped practice:

* Variables
* User input using `input()`
* Type conversion using `int()`
* `while` loops
* `if-elif-else` statements
* Comparison operators
* Increment operators (`+=`)
* Python's `random` module
* `random.randint()`

🚀 How to Run
1. Clone the repository

```bash
git clone https://github.com/sheemaazmat/the-perfect-guess-game.git
```

2. Navigate to the project folder

```bash
cd the-perfect-guess-game
```

3. Run the program

```bash
python the_perfect_guess_game.py
```

💻 Example Output

```text
Guess the number: 50
Lower number please

Guess the number: 25
Higher number please

Guess the number: 37
You guessed it!
Number of guesses: 3
```

The randomly generated number will be different each time the program runs, so the output may vary.

🎯 Learning Objective
The main objective of this project was to strengthen Python fundamentals by building an interactive guessing game and practicing loops, conditional statements, user input, random number generation, and counting attempts.

🔮 Future Improvements
Possible improvements for future versions:

* Add difficulty levels
* Limit the number of attempts
* Add a score system
* Allow the player to play multiple rounds
* Add input validation for invalid entries

👤 Author
Sheema Azmat

⭐ If you found this project useful, consider giving the repository a star!
