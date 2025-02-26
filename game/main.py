import pygame
import sys
import time
from board import Board
from player import Player
from utils import display_message

# Initialize Pygame
pygame.init()

# Constants
SCREEN_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
LINE_WIDTH = 15
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = CELL_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

# Screen setup
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Fonts
font = pygame.font.Font(None, 74)

# Game variables
board = Board(GRID_SIZE, CELL_SIZE, SPACE, CROSS_WIDTH, CIRCLE_RADIUS, CIRCLE_WIDTH, CROSS_COLOR, CIRCLE_COLOR)
player1 = Player("X")
player2 = Player("O")
current_player = player1

def draw_grid():
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, x * CELL_SIZE), (SCREEN_SIZE, x * CELL_SIZE), LINE_WIDTH)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] // CELL_SIZE
            mouseY = event.pos[1] // CELL_SIZE

            if board.is_empty_cell(mouseY, mouseX):  # Swap mouseX and mouseY
                board.mark_cell(mouseY, mouseX, current_player.symbol)  # Swap mouseX and mouseY
                if board.check_winner(current_player.symbol):
                    display_message(screen, f"{current_player.symbol} wins!", (50, 50), font)
                    pygame.display.update()
                    time.sleep(5)  # Display the winning message for 5 seconds
                    running = False
                elif board.is_full():
                    display_message(screen, "Draw!", (50, 50), font)
                    pygame.display.update()
                    time.sleep(5)  # Display the draw message for 5 seconds
                    running = False
                current_player = player2 if current_player == player1 else player1

    screen.fill(BG_COLOR)
    draw_grid()
    board.draw(screen)
    pygame.display.update()


"""
This module initializes and runs a Tic Tac Toe game using Pygame.

Classes:
    Board: Represents the game board.
    Player: Represents a player in the game.

Functions:
    draw_grid(): Draws the grid lines on the game screen.

Constants:
    SCREEN_SIZE (int): The size of the game screen.
    GRID_SIZE (int): The number of cells in the grid.
    CELL_SIZE (int): The size of each cell in the grid.
    LINE_WIDTH (int): The width of the grid lines.
    CIRCLE_RADIUS (int): The radius of the circle (O) symbol.
    CIRCLE_WIDTH (int): The width of the circle (O) symbol.
    CROSS_WIDTH (int): The width of the cross (X) symbol.
    SPACE (int): The space between the symbol and the cell border.
    BG_COLOR (tuple): The background color of the game screen.
    LINE_COLOR (tuple): The color of the grid lines.
    CIRCLE_COLOR (tuple): The color of the circle (O) symbol.
    CROSS_COLOR (tuple): The color of the cross (X) symbol.

Variables:
    screen: The Pygame display surface.
    font: The font used for displaying messages.
    board: The game board instance.
    player1: The first player instance.
    player2: The second player instance.
    current_player: The player whose turn it is.
    running: A boolean indicating whether the game loop is running.

Main Game Loop:
    Handles Pygame events, updates the game state, and redraws the screen.
"""
# This page initializes the Pygame library, sets up the game screen, defines game constants and colors, 
# creates instances of the Board and Player classes, and runs the main game loop.
