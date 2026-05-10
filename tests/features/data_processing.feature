Feature: Collecting and storing data
  Optimization algorithm needs access to valid input data to solve

  Scenario: Fetching and storing data into the Json file
    Given has access to "https://logicgamesonline.com/lightsout/"
    When system fetches HTML and extracts matrix
    Then system creates valid board with size 5
    And file manager stores board to "test_boards.json"

Scenario: Creating a board from manual keyboard input
    Given user provides a string "1110011100111001110011100"
    When system parses the string into a matrix
    Then system creates valid board with size 5
    And file manager stores manual board to "manual_boards.json"