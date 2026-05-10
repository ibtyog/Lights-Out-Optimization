import json
import os
import time
from typing import List
from .board import Board


class FileManager:
    def __init__(self, filepath: str = "data/boards.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def _load_all(self) -> dict:
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def save_board(self, board: Board) -> str:
        data = self._load_all()

        if data:
            next_id = max(int(k) for k in data.keys()) + 1
        else:
            next_id = 1

        data[str(next_id)] = {"size": board.size, "initial_state": board.initial_state}

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return str(next_id)

    def load_board(self, board_id: str) -> List[List[int]]:
        data = self._load_all()
        if board_id not in data:
            raise KeyError(f"Board with ID {board_id} not found")
        return data[board_id]["initial_state"]
