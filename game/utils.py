def check_valid_move(board, row, col):
    return board[row][col] == " "

def display_message(screen, message, position, font, color=(255, 255, 255)):
    text = font.render(message, True, color)
    screen.blit(text, position)

def reset_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]


"""
    Check if a move is valid on the tic-tac-toe board.

    Args:
        board (list of list of str): The current state of the tic-tac-toe board.
        row (int): The row index of the move.
        col (int): The column index of the move.

    Returns:
        bool: True if the move is valid (i.e., the cell is empty), False otherwise.
"""
# This function checks if the specified cell on the tic-tac-toe board is empty.
# It returns True if the cell is empty (indicating a valid move), and False otherwise.