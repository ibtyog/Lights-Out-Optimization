Feature: Game Engine Rules
  Optimization solver
  needs the game engine to enforce Lights Out rules and evaluate solutions
  So that It can find the optimal sequence of moves

  Scenario: Flipping a cell toggles it and its neighbors
    Given an empty board of size 5
    When the engine flips the cell at X: 2, Y: 2
    Then the cell at X: 2, Y: 2 becomes 1
    And the cell at X: 2, Y: 1 becomes 1
    And the cell at X: 2, Y: 3 becomes 1
    And the cell at X: 1, Y: 2 becomes 1
    And the cell at X: 3, Y: 2 becomes 1
    And the cell at X: 0, Y: 0 remains 0

  Scenario: Evaluating a complete solution 
    Given a board solvable by clicking X: 0, Y: 0
    When the engine evaluates a solution that clicks X: 0, Y: 0
    Then the objective function returns 1

  Scenario: Evaluating an incomplete solution 
    Given a board solvable by clicking X: 0, Y: 0
    When the engine evaluates an empty solution
    Then the objective function returns 300