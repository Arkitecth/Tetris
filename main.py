import pygame

# pygame setup

WHITE = (200, 200, 200)


class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Square:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.color = "blue"
        self.rect = pygame.Rect(400, 10, 60, 60)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)


class Game:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill("black")
        self.running = True
        self.clock = pygame.time.Clock()

    def start(self):
        square = Square((0, 0), self.screen)
        while self.running:
            self.draw_grid()
            square.draw(self.screen)
            square.handle_keys()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # self.screen.fill("black")
            pygame.display.flip()
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
