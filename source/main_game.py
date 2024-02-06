import pygame
pygame.init()


def main(size):
    if size == "res_4k":
        WIDTH = 2500
        HEIGHT = 1200

    elif size == "res_fullhd":
        WIDTH = 1200
        HEIGHT = 500

    else:
        print("resolution setting failed")
        WIDTH = 1200
        HEIGHT = 500

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jumping game")

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue_running_check = False

#TODO: výhra
win = True