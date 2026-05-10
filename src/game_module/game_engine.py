import copy
from typing import List
from src.data_module.board import Board


class GameEngine:
    """Lights Out Game Engine - game logic and evaluation of solutions."""

    def __init__(self, board: Board):
        self.board = board

    def flip(self, x: int, y: int) -> None:
        """Change the state of the cell at (x, y) and its neighbors."""
        directions = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.board.size and 0 <= ny < self.board.size:
                current_val = self.board.get_cell(nx, ny)
                self.board.set_cell(nx, ny, 1 - current_val)

    def get_lights_count(self) -> int:
        """Count the number of lights that are currently on."""
        return sum(sum(row) for row in self.board.matrix)

    def is_solved(self) -> bool:
        """Return True if the current board is solved (all lights are off)."""
        return self.get_lights_count() == 0

    def evaluate_solution(self, solution_matrix: List[List[int]]) -> int:
        """
        Evaluates a candidate solution for the Lights Out puzzle.
        Calculates objective function value based on the number of clicks and remaining lights.
        Score under 100 guarantees a solution, with lower being better.
        """

        clicks = sum(sum(row) for row in solution_matrix)

        temp_board = Board(copy.deepcopy(self.board.initial_state))
        temp_engine = GameEngine(temp_board)

        for y in range(temp_board.size):
            for x in range(temp_board.size):
                if solution_matrix[y][x] == 1:
                    temp_engine.flip(x, y)

        lights_left = temp_engine.get_lights_count()

        return (100 * lights_left) + clicks
