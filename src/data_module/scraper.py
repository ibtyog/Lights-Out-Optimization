import requests
from bs4 import BeautifulSoup
from typing import List
from .board import Board


class Scraper:
    def __init__(self, url: str = "https://logicgamesonline.com/lightsout/"):
        self.url = url

    def fetch_html(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def extract_puzzle(self, script_text: str) -> str:
        """Extract the puzzle string"""
        marker = "var puzzle = "
        if marker not in script_text:
            raise ValueError("Variable 'puzzle' not found")
        return script_text.split(marker, 1)[1].split(";", 1)[0].strip().strip("\"'")

    def parse_matrix(self, html_data: str) -> List[List[int]]:
        soup = BeautifulSoup(html_data, "html.parser")

        script_text = ""
        for script in soup.find_all("script"):
            if script.string and "var puzzle =" in script.string:
                script_text = script.string
                break

        if not script_text:
            raise ValueError("Variable 'puzzle' not found in the HTML.")

        puzzle_string = self.extract_puzzle(script_text)

        if len(puzzle_string) != 25:
            raise ValueError(
                f"Expected 25 characters (5x5 board), found {len(puzzle_string)}"
            )

        flat_list = [1 if char == "#" else 0 for char in puzzle_string]

        matrix = [flat_list[i : i + 5] for i in range(0, 25, 5)]
        return matrix

    def get_new_board(self) -> Board:
        html = self.fetch_html()
        matrix = self.parse_matrix(html)
        return Board(matrix)
