import pygame
import random
# pygame setup

WHITE = (200, 200, 200)


class Square:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.color = "blue"
        self.rect = pygame.Rect(400, 10, 40, 40)
        self.move = True

    def move_down(self):
        if self.move:
            self.rect.move_ip(0, 1)

    def detect_collission_part(self, pieces):
        for piece in pieces:
            if self.rect.colliderect(piece):
                self.move = False
                return True

    def detect_collission_wall(self, wall):
        # Bottom of the screen
        if self.rect.colliderect(wall):
            self.move = False
            return True
        return False

    def handle_keys(self, pieces):
        if self.move:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.can_move_horizontally(-1, pieces):
                self.rect.move_ip(-1, 0)
            if key[pygame.K_RIGHT] and self.can_move_horizontally(1, pieces):
                self.rect.move_ip(1, 0)
            if key[pygame.K_DOWN]:
                self.rect.move_ip(0, 1)

    def can_move_horizontally(self, dx, pieces):
        future_rect = self.rect.move(dx, 0)
        for piece in pieces:
            if future_rect.colliderect(piece):
                return False
        return True

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        border_color = "red"  # White color for the border
        border_width = 3  # Change this to increase or decrease border thickness
        pygame.draw.rect(self.screen, border_color, self.rect, border_width)


# Refactor to abstract class
class Straight:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.color = "red"
        self.rect = pygame.Rect(400, 10, 20, 60)
        self.move = True

    def move_down(self):
        if self.move:
            self.rect.move_ip(0, 1)

    def detect_collission_part(self, pieces):
        for piece in pieces:
            if self.rect.colliderect(piece):
                self.move = False
                return True

    def detect_collission_wall(self, wall):
        # Bottom of the screen
        if self.rect.colliderect(wall):
            self.move = False
            return True
        return False

    def handle_keys(self):
        if self.move:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.move_ip(-1, 0)
            if key[pygame.K_RIGHT] and self.rect.right < self.screen.get_width():
                self.rect.move_ip(1, 0)
            if key[pygame.K_DOWN]:
                self.rect.move_ip(0, 1)

    def draw(self):
        return pygame.draw.rect(self.screen, self.color,
                                self.rect)


class Game:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.width = width
        self.height = height
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill("black")
        self.running = True
        self.clock = pygame.time.Clock()
        self.current_piece = None
        self.pieces = []
        self.wall = pygame.Rect(0, 600, width, 10)

    def generate_shape(self):
        # self.shapes = {1: Square(self.screen), 2: Straight(self.screen)}
        # key = random.randint(1, len(self.shapes))
        # self.current_piece = self.shapes[key]
        self.current_piece = Square(self.screen)

    def draw_pieces(self):
        self.current_piece.draw()
        for piece in self.pieces:
            piece.draw()

    def start(self):
        self.generate_shape()
        while self.running:
            self.draw_grid()
            self.draw_pieces()
            self.current_piece.handle_keys(self.pieces)
            if self.current_piece.move and self.current_piece.detect_collission_wall(self.wall):
                self.pieces.append(self.current_piece)
                self.generate_shape()
            elif self.current_piece.move and self.current_piece.detect_collission_part(self.pieces):
                self.pieces.append(self.current_piece)
                self.generate_shape()
            self.clock.tick(60)
            self.current_piece.move_down()
            pygame.display.flip()
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def draw_grid(self):
        blockSize = 20
        for x in range(0, self.width, blockSize):
            for y in range(0, self.height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, WHITE, rect, 1)


def main():
    game = Game(800, 600)
    game.start()
    pygame.quit()


main()
