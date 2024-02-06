import pygame
pygame.init()

GRAYISH_WHITE = (242, 243, 245)

# úvodní okno
INITIAL_WINDOW_WIDTH = 400
INITIAL_WINDOW_HEIGHT = 400
initial_window_run = True

CONTINUE_RUNNING = True


def drawing_initial_window():
    screen.fill(GRAYISH_WHITE)

while initial_window_run:
    continue_running_check = True

    screen = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))
    pygame.display.set_caption("Initial settings")

    drawing_initial_window()
    screen.fill(GRAYISH_WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            initial_window_run = False
            continue_running_check = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        initial_window_run = False
pygame.quit()

chosen_size = input("4k or hd: ")
if chosen_size == "4k":
    size = "res_4k"
else:
    size = "res_fullhd"