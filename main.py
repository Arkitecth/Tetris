import pygame

# pygame setup

WHITE = (200, 200, 200)


class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Square:
    def __init__(self, pos, win) -> None:
        self.pos = pos
        self.color = "blue"
        self.win = win

    def move(self, rect, pos):
        rect.move_ip(pos)

    def draw(self):
        rect = pygame.draw.rect(self.win, self.color,
                                pygame.Rect(400, 10, 60, 60))
        return rect


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
        tetronimoe = Square((0, 0), self.screen)
        while self.running:
            self.draw_grid()
            piece = tetronimoe.draw()
            tetronimoe.move(piece, (500, 500))
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
