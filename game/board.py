import pygame

class Board:
    def __init__(self, size, cell_size, space, cross_width, circle_radius, circle_width, cross_color, circle_color):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.cell_size = cell_size
        self.space = space
        self.cross_width = cross_width
        self.circle_radius = circle_radius
        self.circle_width = circle_width
        self.cross_color = cross_color
        self.circle_color = circle_color

    def draw(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == "X":
                    self.draw_x(screen, row, col)
                elif self.board[row][col] == "O":
                    self.draw_o(screen, row, col)

    def draw_x(self, screen, row, col):
        start_desc = (col * self.cell_size + self.space, row * self.cell_size + self.space)
        end_desc = (col * self.cell_size + self.cell_size - self.space, row * self.cell_size + self.cell_size - self.space)
        pygame.draw.line(screen, self.cross_color, start_desc, end_desc, self.cross_width)
        start_asc = (col * self.cell_size + self.space, row * self.cell_size + self.cell_size - self.space)
        end_asc = (col * self.cell_size + self.cell_size - self.space, row * self.cell_size + self.space)
        pygame.draw.line(screen, self.cross_color, start_asc, end_asc, self.cross_width)

    def draw_o(self, screen, row, col):
        center = (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2)
        pygame.draw.circle(screen, self.circle_color, center, self.circle_radius, self.circle_width)

    def mark_cell(self, row, col, player):
        self.board[row][col] = player

    def is_empty_cell(self, row, col):
        return self.board[row][col] == " "

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def check_winner(self, player):

        for row in self.board:
            if all([cell == player for cell in row]):
                return True

        for col in range(self.size):
            if all([self.board[row][col] == player for row in range(self.size)]):
                return True
            
        if all([self.board[i][i] == player for i in range(self.size)]):
            return True
        if all([self.board[i][self.size - i - 1] == player for i in range(self.size)]):
            return True
        return False
    
    
"""
This module defines the Board class for a Tic-Tac-Toe game using Pygame.
Classes:
    Board: Represents the game board and handles drawing and game logic.
Methods:
    __init__(self, size, cell_size, space, cross_width, circle_radius, circle_width, cross_color, circle_color):
        Initializes the board with the given parameters.
    draw(self, screen):
        Draws the current state of the board on the given Pygame screen.
    draw_x(self, screen, row, col):
        Draws an 'X' at the specified row and column on the given Pygame screen.
    draw_o(self, screen, row, col):
        Draws an 'O' at the specified row and column on the given Pygame screen.
    mark_cell(self, row, col, player):
        Marks the specified cell with the player's symbol ('X' or 'O').
    is_empty_cell(self, row, col):
        Checks if the specified cell is empty.
    is_full(self):
        Checks if the board is full (no empty cells).
    check_winner(self, player):
        Checks if the specified player has won the game.
"""
# This module defines the Board class for a Tic-Tac-Toe game using Pygame.
# It includes methods for drawing the board, marking cells, checking for empty cells,
# checking if the board is full, and checking for a winner.