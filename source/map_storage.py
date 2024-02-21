import pygame
pygame.init()


class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, general_scroll):
        self.rect.x += general_scroll


def first_map():
    obstacle1 = Obstacle(1475, 1030, 211, 30)

    obstacles = [obstacle1]

    return obstacles