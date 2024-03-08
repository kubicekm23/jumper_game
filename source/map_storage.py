import pygame
pygame.init()


class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, general_scroll):
        self.rect.x += general_scroll

    def movey(self, scroll_up):
        self.rect.y += scroll_up


def first_map():
    obstacle1 = Obstacle(1475, 1030, 211, 30)
    obstacle2 = Obstacle(1750, 940, 138, 23)
    obstacle3 = Obstacle(1901, 1009, 138, 23)
    obstacle4 = Obstacle(2123, 1004, 138, 23)
    obstacle5 = Obstacle(2318, 926, 138, 23)
    obstacle6 = Obstacle(2533, 818, 138, 23)
    obstacle7 = Obstacle(2296, 696, 138, 23)
    #obstacle6 = Obstacle(2395, 818, 138, 23)
    #obstacle6 = Obstacle(2395, 818, 138, 23)

    obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7]

    return obstacles


def second_map():
    # maybe differences in Y of about 670??  + obstacles height??? SAVE MF
    difference_smol = 670

    obstacle1 = Obstacle(1475, 360, 211, 30)
    obstacle2 = Obstacle(1750, 274, 138, 23)
    obstacle3 = Obstacle(1901, 1009 - difference_smol, 138, 23)
    obstacle4 = Obstacle(2123, 1004 - difference_smol, 138, 23)
    obstacle5 = Obstacle(2318, 926 - difference_smol, 138, 23)
    obstacle6 = Obstacle(2533, 818 - difference_smol, 138, 23)
    obstacle7 = Obstacle(2296, 696 - difference_smol, 138, 23)

    obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7]

    return obstacles
