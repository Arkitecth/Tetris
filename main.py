import pygame

# pygame setup

WHITE = (200, 200, 200)


class Tetronimoe: 
    def __init__(self) -> None:
        self.x = 0 
        


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
        while self.running:
            self.draw_grid()
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
                rect = pygame.Rect(x, y,`` blockSize, blockSize)
                pygame.draw.rect(self.screen, WHITE, rect, 1)


def main():
    game = Game(800, 600)
    game.start()
    pygame.quit()


main()
