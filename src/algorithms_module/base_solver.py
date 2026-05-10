from abc import ABC, abstractmethod
from typing import List
from src.data_module.board import Board


class BaseSolver(ABC):
    """Interface for Lights Out puzzle solvers. Defines the method to solve the puzzle."""

    @abstractmethod
    def solve(self, board: Board) -> List[List[int]]:
        """Solve the Lights Out puzzle and return the sequence of moves."""
        pass
