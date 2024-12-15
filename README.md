# Sudoku Solver

This project is a Sudoku solver implemented in Python. It reads Sudoku puzzles from text files, solves them using constraint propagation, and prints the solutions. The project demonstrates the use of list comprehensions to create lists and sets.

## Files

- `main.py`: Contains the `Sudoku` class and the main script to solve Sudoku puzzles.
- `subor1.txt`, `subor2.txt`, ..., `subor9.txt`: Text files containing Sudoku puzzles.

## Usage

1. Place your Sudoku puzzle files (`subor1.txt`, `subor2.txt`, ..., `subor9.txt`) in the same directory as `main.py`.
2. Run the `main.py` script to solve the puzzles.

```bash
python main.py
```

## Sudoku Class

The `Sudoku` class provides methods to read, solve, and print Sudoku puzzles.

### Methods

- `__init__(self, file_name)`: Initializes the Sudoku grid from a file.
- `__str__(self)`: Returns a string representation of the Sudoku grid.
- `make_sets(self)`: Identifies possible values for empty cells using constraint propagation.
- `replace(self)`: Replaces single-value sets with their corresponding values.
- `solve(self)`: Solves the Sudoku puzzle.
- `count_empty_squares(self)`: Counts the number of empty squares in the grid.

## Example

```python
if __name__ == "__main__":
    for i in range(1, 10):
        s = Sudoku(f'subor{i}.txt')
        print(s.solve())
```

##

