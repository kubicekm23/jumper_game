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
    obstacle8 = Obstacle(2528, 573, 138, 23)
    obstacle9 = Obstacle(2324, 464, 138, 23)
    obstacle10 = Obstacle(1920, 384, 348, 50)
    obstacle11 = Obstacle(2111, 236, 138, 23)
    obstacle12 = Obstacle(1900, 97, 138, 23)
    obstacle13 = Obstacle(1672, -92, 211, 30)
    obstacle14 = Obstacle(1487, -220, 138, 23)
    obstacle15 = Obstacle(1677, -376, 138, 23)
    obstacle16 = Obstacle(1479, -531, 138, 23)
    obstacle17 = Obstacle(1677, -691, 138, 23)
    obstacle18 = Obstacle(1487, -868, 138, 23)
    obstacle19 = Obstacle(1670, -1025, 138, 23)
    obstacle20 = Obstacle(1832, -1181, 138, 23)

    obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, obstacle9,
                 obstacle10, obstacle11, obstacle12, obstacle13, obstacle14, obstacle15, obstacle16, obstacle17,
                 obstacle18, obstacle19, obstacle20]

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
    obstacle8 = Obstacle(2528, 573 - difference_smol, 138, 23)
    obstacle9 = Obstacle(2324, 464 - difference_smol, 138, 23)
    obstacle10 = Obstacle(1920, 384 - difference_smol, 348, 50)
    obstacle11 = Obstacle(2111, 236 - difference_smol, 138, 23)
    obstacle12 = Obstacle(1900, 97 - difference_smol, 138, 23)
    obstacle13 = Obstacle(1672, -92 - difference_smol, 211, 30)
    obstacle14 = Obstacle(1487, -220 - difference_smol, 138, 23)
    obstacle15 = Obstacle(1677, -376 - difference_smol, 138, 23)
    obstacle16 = Obstacle(1479, -531 - difference_smol, 138, 23)
    obstacle17 = Obstacle(1677, -691 - difference_smol, 138, 23)
    obstacle18 = Obstacle(1487, -868 - difference_smol, 138, 23)
    obstacle19 = Obstacle(1670, -1025 - difference_smol, 138, 23)
    obstacle20 = Obstacle(1832, -1181 - difference_smol, 138, 23)

    obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6, obstacle7, obstacle8, obstacle9,
                 obstacle10, obstacle11, obstacle12, obstacle13, obstacle14, obstacle15, obstacle16, obstacle17,
                 obstacle18, obstacle19, obstacle20]

    return obstacles
