import pygame
pygame.init()


class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, general_scroll):
        self.rect.x += general_scroll


def first_map():
    obstacle1 = Obstacle(1475, 1030, 211, 30)
    obstacle2 = Obstacle(1750, 940, 138, 23)
    obstacle3 = Obstacle(1901, 1009, 138, 23)
    obstacle4 = Obstacle(2123, 1004, 138, 23)
    obstacle5 = Obstacle(2318, 926, 138, 23)

    obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5]

    return obstacles