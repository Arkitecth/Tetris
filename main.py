import pygame

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

    def handle_keys(self):
        if self.move:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.rect.move_ip(-1, 0)
            if key[pygame.K_RIGHT]:
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
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill("black")
        self.running = True
        self.clock = pygame.time.Clock()

    def generate_shape(self):
        return Square(self.screen)

    def detect_collission(self, piece):
        # Bottom of the screen
        bottom_screen = self.screen.get_height()
        bottom_square = piece.rect.bottom
        # Bottom of the square
        if bottom_square == bottom_screen:
            piece.move = False
        # Generate random shape

    def start(self):
        square = Square(self.screen)
        self.screen.get_height()
        while self.running:
            square.handle_keys()
            self.detect_collission(square)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("black")
            self.draw_grid()
            square.draw()
            pygame.display.flip()
            square.move_down()
            self.clock.tick(60)

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
