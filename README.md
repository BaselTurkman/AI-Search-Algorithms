# AI Assignment: Rearranging Letters on a Chessboard

## Overview
This assignment involves rearranging letters on a chessboard to reach a specific configuration using **breadth-first search (BFS)** and **A\* algorithms**. The main objective is to explore all possible moves to reach a goal state by manipulating the letters on the chessboard.

## Classes

### `Grid`
Represents a state of the chessboard. It holds information about the current configuration of letters on the chessboard.

### `ChessBoard`
Represents the environment or the chessboard itself, handling the grid and the operations that can be performed on it.

## Helper Functions
These functions assist in both the BFS and A\* algorithms.

### `printChessboard(self, grid)`
Prints the chessboard represented by the given grid (state).

### `findFirstLetter(self, state)`
Performs a linear search to find the first letter in the given state.

### `isValidMove(self, x, y)`
Checks if the given position (x, y) is valid on the chessboard.

### `knightMoves(self, grid)`
Performs breadth-first search (BFS) to find all possible moves for a knight on the chessboard starting from the first letter and returns the number of letters seen. This function is also used as a heuristic function in the A\* solution.

## BFS Functions
These functions implement the BFS algorithm to solve the problem.

### `rearrangeLettersUsingBFS(self, state)`
The main function in the BFS solution. It rearranges the letters on the chessboard using BFS until a solution is found.

### `generateChessboard(self, board)`
Generates a new chessboard by moving letters in all possible directions (up, down, left, right) from the current state. Called by `rearrangeLettersUsingBFS`.

### `printBFSSolution(self, state)`
Prints the solution path by tracing back from the initial state to the final state.

## A\* Functions
These functions implement the A* algorithm to solve the problem.

### `rearrangeLettersUsingAStar(self, state)`
The main function in the A* solution. It rearranges the letters on the chessboard using the A* algorithm until a solution is found.

### `generateChessboardWithKnightMoves(self, board)`
Generates new chessboards by moving letters in all possible directions from the current state (up, down, left, right) and calls `knightMoves` to calculate how many letters have been seen in the new state. It subtracts this value by 6 to determine how many letters remain to reach the goal state.

### `printSolutionAStar(self, state)`
Prints the solution path found using the A* algorithm.

## Summary
This problem is solved using Python programming. The key functions triggering the search for solutions are:

- `rearrangeLettersUsingBFS` (for BFS)
- `rearrangeLettersUsingAStar` (for A*).

Both algorithms explore the state space of possible chessboard configurations, attempting to rearrange the letters to the goal configuration.

- The `generateChessboard` and `generateChessboardWithKnightMoves` functions are responsible for generating new states (chessboards) by moving letters in different directions.
- The solution paths are printed using `printBFSSolution` and `printSolutionAStar`.

## Requirements
- Python 3.x

## Usage
1. Clone or download this repository.
2. Ensure that Python 3.x is installed.
3. Run the provided Python script to see the BFS and A* solutions.

