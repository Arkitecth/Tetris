import pygame
import random


class Block:
    def __init__(self, color, row, column) -> None:
        self.color = color
        self.row = row
        self.column = column
        self.rect = pygame.Rect(column, row, 10, 10)

    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, self.rect)

    def check_collission(self, block):
        if self.row == block.row and self.column == block.column:
            return True
        return False

    def check_wall_collission(self, wall_row, wall_column):
        if self.row == wall_row and self.column == wall_column:
            return True
        return False


class Tetronimoe:
    def __init__(self) -> None:
        self.pieces = []

    def draw_tetronimoe(self):
        pass
        # Random Piece
        # Store those Random Pieces
        # Rotate those pieces
