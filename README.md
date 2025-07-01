# Wordle Solver

This repository contains a Python-based solver for the Wordle game, designed to play the word-guessing puzzle interactively. The solver uses a knowledge base to track letter constraints and filters possible words from a dictionary, making informed guesses to solve the puzzle within six attempts. Built with a command-line interface and color-coded feedback using `termcolor`, the solver supports dynamic word filtering and is applicable to decision-making and optimization tasks in manufacturing data analysis.

## Table of Contents
- [Wordle Solver](#wordle-solver)
  - [Project Overview](#project-overview)
  - [Approach](#approach)
  - [Tools and Technologies](#tools-and-technologies)
  - [Results](#results)
  - [Skills Demonstrated](#skills-demonstrated)
  - [Setup and Usage](#setup-and-usage)
  - [References](#references)

## Project Overview
The Wordle Solver automates the Wordle game, where players guess a five-letter word within six attempts, receiving feedback on letter correctness (correct position, present in word, or absent). The solver maintains a knowledge base of possible letters per position and required letters, filtering a dictionary of valid words (`answer_words.txt`) to make optimal guesses. It prompts the user for guesses, validates them against a dictionary (`guess_words.txt`), and updates constraints based on feedback (green for correct letter and position, yellow for correct letter, white for absent). The solver’s iterative filtering and decision-making logic is applicable to manufacturing processes requiring pattern recognition and constraint-based optimization.

## Approach
The project is structured as a modular command-line application:
- **Wordle Class (`main.py`)**:
  - **Initialization**: Loads a list of possible answer words (`answer_words.txt`) and initializes a knowledge base tracking possible letters per position and required letters. Randomly selects an answer word for simulation.
  - **Game Loop**: Runs for up to six guesses or until the correct word is guessed. Displays previous guesses with color-coded feedback (green, yellow, white) using `termcolor`, prompts for user input, and validates guesses against `guess_words.txt`.
  - **Knowledge Base Update**: Updates constraints based on guess feedback:
    - Green (correct letter and position): Fixes the letter at that position.
    - Yellow (correct letter, wrong position): Removes the letter from that position’s possibilities and adds it to required letters.
    - White (absent letter): Removes the letter from all position possibilities.
  - **Word Filtering**: Uses regex to filter possible words based on position constraints and required letters, narrowing the candidate list after each guess.
- **User Interaction**: Prompts for five-letter guesses, validates them, and displays the updated knowledge base and number of possible words (full list if <50 words remain).
- **Feedback Visualization**: Prints guesses with color-coded letters (green, yellow, white) and announces win/loss with the answer word.

The solver iteratively refines its word list using feedback-driven constraints, mimicking human reasoning for optimal guessing.

## Tools and Technologies
- **Python**: Core language for game logic and word filtering.
- **termcolor**: Color-coded console output for guess feedback.
- **re (regex)**: Filtering possible words based on letter constraints.
- **random**: Selecting random answer words for simulation.
- **File I/O**: Reading word dictionaries (`answer_words.txt`, `guess_words.txt`).

## Results
- **Performance**: Successfully solved Wordle puzzles within six guesses by filtering possible words based on feedback-driven constraints.
- **Efficiency**: Reduced the candidate word list dynamically, displaying remaining possibilities (full list for <50 words) for informed guessing.
- **Usability**: Provided clear, color-coded feedback (green, yellow, white) and knowledge base updates, enhancing user interaction.
- **Robustness**: Handled invalid inputs and maintained accurate word filtering, ensuring reliable operation across puzzle instances.

## Skills Demonstrated
- **Algorithmic Problem-Solving**: Designed a constraint-based word filtering algorithm, applicable to manufacturing decision-making systems.
- **Data Filtering**: Implemented regex-based filtering to narrow word candidates, relevant to data analysis and optimization.
- **User Interface Design**: Built an interactive command-line interface with color-coded feedback for clear user communication.
- **Knowledge Representation**: Managed a dynamic knowledge base for letter constraints, suitable for pattern recognition tasks.
- **File Processing**: Handled dictionary files for word validation and answer selection.

## Setup and Usage
1. **Prerequisites**:
   - Clone the repository: `git clone <repository-url>` (replace with actual URL if available).
   - Install dependencies: `pip install termcolor`
   - Python 3.6+ required.
   - Provide `answer_words.txt` (comma-separated list of valid five-letter answer words) and `guess_words.txt` (newline-separated list of valid guess words) in the project directory.
2. **Running**:
- Run the solver: `python main.py`
- Enter five-letter guesses when prompted (validated against `guess_words.txt`).
- View color-coded guess feedback (green: correct letter and position, yellow: correct letter, white: absent letter).
- The game ends after six guesses or when the correct word is guessed, displaying win/loss and the answer word.
- Adjust `answer_words.txt` and `guess_words.txt` to modify the word pool.
3. **Notes**:
- Ensure `answer_words.txt` and `guess_words.txt` are present and correctly formatted.
- Invalid guesses (non-five-letter or not in `guess_words.txt`) are rejected with a prompt to retry.
- The solver simulates Wordle by randomly selecting an answer word from `answer_words.txt`.

## References
- [termcolor Documentation](https://pypi.org/project/termcolor/)
- [Python re Module](https://docs.python.org/3/library/re.html)
- [Python random Module](https://docs.python.org/3/library/random.html)
- [Wordle Game](https://www.nytimes.com/games/wordle/index.html)
