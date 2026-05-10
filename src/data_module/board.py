import copy
from typing import List


class Board:
    """
    Class representing the board state.
    It is responsible only for storing the data (the matrix).
    """

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            raise ValueError("Matrix cannot be empty")

        self.size = len(matrix)

        for row in matrix:
            if len(row) != self.size:
                raise ValueError("Matrix must be square")

        self.initial_state = copy.deepcopy(matrix)
        self.matrix = copy.deepcopy(matrix)

    def get_cell(self, x: int, y: int) -> int:
        """Get the value of a cell. Note: y is the row, x is the column."""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.matrix[y][x]
        raise ValueError(f"Coordinates ({x}, {y}) are outside the board")

    def set_cell(self, x: int, y: int, val: int) -> None:
        """Set the value of a cell to 0 or 1."""
        if val not in (0, 1):
            raise ValueError("Cell value must be 0 or 1")
        if 0 <= x < self.size and 0 <= y < self.size:
            self.matrix[y][x] = val
        else:
            raise ValueError(f"Coordinates ({x}, {y}) are outside the board")

    def reset(self) -> None:
        """Reset the board to its initial state."""
        self.matrix = copy.deepcopy(self.initial_state)

    def __str__(self) -> str:
        """Pretty print the board in the console (useful for debugging)."""
        return "\n".join(str(row) for row in self.matrix)
