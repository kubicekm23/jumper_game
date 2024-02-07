import pygame



def main(chosen_character):
    pygame.init()

    #výběr velikosti okna
    system_width = pygame.display.Info().current_w
    if system_width > 2500:
        WIDTH = 2520
        HEIGHT = 1200

    elif system_width > 1200:
        WIDTH = 1500
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