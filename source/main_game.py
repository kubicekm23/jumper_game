import pygame
import math
pygame.init()

large_window = False

continue_running_check = True

# výběr velikosti okna
system_width = pygame.display.Info().current_w
if system_width > 2500:
    large_window = True
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

clock = pygame.time.Clock()

# characters
red_character = pygame.image.load("images/red_character.png")
blittable_red_character = pygame.transform.scale(red_character, (50, 50))

blue_character = pygame.image.load("images/red_character.png")
blittable_blue_character = pygame.transform.scale(blue_character, (50, 50))

# hodnoty pohybu pozadí
cloud_scroll = 0
ground_scroll = 0
general_scroll = 0

# background images
cloud_image = pygame.image.load("images/clouds.png").convert_alpha()
ground_image = pygame.image.load("images/ground.png").convert()
if not large_window:
    mountain_image = pygame.image.load("images/mountain.png")
    ground = pygame.transform.scale(ground_image, (50, 50))
elif large_window:
    mountain_image = pygame.image.load("images/mountain.png")
    ground = pygame.transform.scale(ground_image, (100, 100))
    # TODO: add a large mountain.png

# nastavení proměnných pozadí
tiles = math.ceil(WIDTH / mountain_image.get_height())
ground_tiles = math.ceil(WIDTH / mountain_image.get_width() + 30)
ground_width = ground.get_width()
ground_height = ground.get_height()


def draw(blittable_chosen_character):
    global cloud_scroll
    clock.tick(60)

    screen.blit(blittable_chosen_character, (0, 0))
    screen.blit(mountain_image, (0, 0))

    # clouds
    for i in range(-1, tiles + 1):
        screen.blit(cloud_image, (i * mountain_image.get_width() + cloud_scroll, 0))

        # vyresetování scroll_cloud
        if abs(cloud_scroll) > mountain_image.get_width():
            cloud_scroll = 0
    cloud_scroll += 0.1

    # zem
    for i in range(-9, ground_tiles + 9):
        screen.blit(ground, (i * ground_width + ground_scroll, HEIGHT - ground_height))
        screen.blit(ground, (i * ground_width + ground_scroll - 50, HEIGHT - ground_height))
        # vyresetování scroll
        if abs(ground_scroll) > ground_width:
            scroll = 0

    pygame.display.update()


def main(chosen_character):
    global continue_running_check

    run = True

    if chosen_character == "red":
        blittable_chosen_character = blittable_red_character
    elif chosen_character == "blue":
        blittable_chosen_character = blittable_blue_character
    else:
        print("choosing character failed in main_game.py, choosing red")
        blittable_chosen_character = blittable_red_character

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue_running_check = False

        draw(blittable_chosen_character)


# TODO: postava
# TODO: pohyb
# TODO: překážky
#   možná použít upravený ground images a dát jim rect vlastnosti?
# TODO: výhra
win = True
