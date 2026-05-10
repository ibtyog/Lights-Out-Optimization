from typing import List
from .board import Board


class InputParser:
    """Klasa odpowiedzialna za parsowanie i walidację ręcznego wejścia od użytkownika."""

    @staticmethod
    def parse_string(input_str: str) -> Board:
        # 1. Usunięcie ewentualnych białych znaków (np. spacji na końcu)
        clean_str = input_str.strip()

        # 2. Walidacja długości
        if len(clean_str) != 25:
            raise ValueError(
                f"Plansza musi mieć dokładnie 25 znaków. Podano: {len(clean_str)}."
            )

        # 3. Walidacja znaków (tylko 0 i 1)
        if not all(char in "01" for char in clean_str):
            raise ValueError("Ciąg może zawierać wyłącznie znaki '0' oraz '1'.")

        # 4. Konwersja do macierzy 5x5
        flat_list = [int(char) for char in clean_str]
        matrix = [flat_list[i : i + 5] for i in range(0, 25, 5)]

        return Board(matrix)
