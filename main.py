import pygame

# pygame setup


class Game:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill("black")
        self.running = True
        self.clock = pygame.time.Clock()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("black")
            pygame.display.flip()
            self.clock.tick(60)


def main():
    game = Game(800, 600)
    game.start()
    pygame.quit()


main()
