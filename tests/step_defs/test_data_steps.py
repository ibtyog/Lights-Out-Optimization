import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.data_module.scraper import Scraper
from src.data_module.file_manager import FileManager

scenarios("../features/data_processing.feature")


@pytest.fixture
def context():
    """Dict to pass data between steps."""
    return {}


@given(parsers.parse('has access to "{url}"'))
def target_url(context, url):
    context["url"] = url
    context["file_path"] = "data/test_boards.json"

    if os.path.exists(context["file_path"]):
        os.remove(context["file_path"])


@when("system fetches HTML and extracts matrix")
def scrape_board(context):
    scraper = Scraper(context["url"])
    context["board"] = scraper.get_new_board()


@then("system creates valid board with size 5")
def check_board_size(context):
    board = context["board"]
    assert board.size == 5
    assert isinstance(board.matrix, list)


@then(parsers.parse('file manager stores board to "{filename}"'))
def check_file_save(context, filename):
    fm = FileManager(filepath=f"data/{filename}")
    board_id = fm.save_board(context["board"])

    assert os.path.exists(fm.filepath)

    loaded_matrix = fm.load_board(board_id)
    assert loaded_matrix == context["board"].initial_state
