from player import Player
from scene import Scene
from inventory import Inventory
from item import Item
from colors import Colors
import pygame, sys


class Game():
    def __init__(self):
        width = 1080
        height = 720

        self.inventory = Inventory()
        player = Player("Logan", 10, 100, 100, 0, None, inventory)
        map = Map(10, 10)

        pygame.init()
        self.window = pygame.display.set_mode((width, height, 0, 32))

    def drawScene(self, scene):
        pygame.draw.rect(self.window, Colors.blue, (200, 100, 150, 50))

    def play():
        self.drawScene()
        while True:
            for event in pygame.event.get():
                if event.key == pygame.K_w:
                    print('w')
                    ##move forward by 1
                    pass
        if event.type == pygame.local.QUIT:
            pygame.exit()
            sys.exit()


if __name__ == "__main__":
    play()
