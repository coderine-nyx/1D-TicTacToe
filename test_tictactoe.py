import pytest

# The functions to be tested
def evaluate(board):
    if 'xxx' in board:
        return 'x'
    elif 'ooo' in board:
        return 'o'
    elif '-' not in board:
        return '!'
    else:
        return '-'

def move(board, mark, position):
    if board[position] == '-':
        return board[:position] + mark + board[position+1:]
    return board

# Tests for evaluate function
def test_evaluate_x_wins():
    assert evaluate('-------xxx--------') == 'x'
    assert evaluate('xxx----------------') == 'x'
    assert evaluate('----------------xxx') == 'x'

def test_evaluate_o_wins():
    assert evaluate('-------ooo--------') == 'o'
    assert evaluate('ooo----------------') == 'o'
    assert evaluate('----------------ooo') == 'o'

def test_evaluate_draw():
    assert evaluate('xoxoxoxoxoxoxoxoxoxo') == '!'
    assert evaluate('oxoxoxoxoxoxoxoxoxox') == '!'

def test_evaluate_game_not_finished():
    assert evaluate('-------x-----------') == '-'
    assert evaluate('-------x---o-------') == '-'
    assert evaluate('-------------------') == '-'

# Tests for move function
def test_move_valid():
    assert move('--------------------', 'x', 5) == '-----x-------------'
    assert move('-----x-------------', 'o', 6) == '-----xo------------'

def test_move_invalid():
    assert move('-----x-------------', 'o', 5) == '-----x-------------'  # Position already occupied
    assert move('-----x-------------', 'x', 5) == '-----x-------------'  # Position already occupied

if __name__ == '__main__':
    pytest.main()

# What is a Python module and how does it differ from a Python package?
# A Python module is a single file containing Python code, which can define functions, classes, and variables.
# A Python package is a collection of modules organized in directories, and it contains an __init__.py file
# to be recognized as a package. Packages allow for a hierarchical structuring of the module namespace.

# What are side effects and give some examples.
# Side effects are changes or effects caused by executing a piece of code that go beyond returning a value.
# Examples include modifying a global variable, changing the state of an object, printing to the console,
# or writing to a file.

# What are Exceptions and what to do if third-party code that we use throws them?
# Exceptions are errors that occur during the execution of a program, disrupting its normal flow.
# If third-party code throws exceptions, we should handle them using try-except blocks, potentially
# logging the error or taking corrective actions to maintain the program's stability.

# Using which keywords can you create, throw and catch your new custom Exception?
# To create a custom exception, we define a new class inheriting from Exception or a subclass.
# To throw (raise) an exception, we use the raise keyword.
# To catch an exception, we use the try and except keywords.

# Benefits of testing include:
# - Ensuring code correctness and functionality.
# - Catching bugs early, which reduces the cost of fixing them.
# - Providing documentation of how the code is supposed to work.
# - Facilitating code maintenance and refactoring.
# - Improving code reliability and quality.
