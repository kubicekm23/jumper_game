import pygame
pygame.init()
import pygame.font

GRAYISH_WHITE = (242, 243, 245)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (245, 10, 10)

CONTINUE_RUNNING = True

# úvodní okno
INITIAL_WINDOW_WIDTH = 400
INITIAL_WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))
pygame.display.set_caption("Initial settings")

chosen_character = None


def drawing_initial_window():
    SCREEN.fill(GRAYISH_WHITE)

    background_image = pygame.image.load("images/potential_backgrond_full_effects.png")
    SCREEN.blit(background_image, (0, 0))

    button_distance_from_border = 60

    red_character_button_rect = pygame.Rect(button_distance_from_border, INITIAL_WINDOW_HEIGHT - 170, 100, 100)
    blue_character_button_rect = pygame.Rect(INITIAL_WINDOW_WIDTH - button_distance_from_border - 100, red_character_button_rect.y, 100, 100)

    # načtení postav
    red_character = pygame.image.load("images/red_character.png")
    blue_character = pygame.image.load("images/blue_character.png")

    blitted_red_character = pygame.transform.scale(red_character, (200, 200))
    blitted_blue_character = pygame.transform.scale(blue_character, (200, 200))

    # nastavení textu
    menu_text = pygame.font.SysFont('Calibri', 30)
    top_text = menu_text.render('Vyberte si postavu, se kterou', 1, BLACK)
    top_text_2 = menu_text.render('budete hrát tuto hru.', 1, BLACK)

    # zobrazení textu na okně
    SCREEN.blit(top_text, (INITIAL_WINDOW_WIDTH / 2 - top_text.get_width() / 2, 20))
    SCREEN.blit(top_text_2, (INITIAL_WINDOW_WIDTH / 2 - top_text_2.get_width() / 2, 55))

    # zobrazení postav na okně
    SCREEN.blit(blitted_red_character, (red_character_button_rect.x - blitted_red_character.get_width() / 2 + 60,
                                        185))
    SCREEN.blit(blitted_blue_character, (blue_character_button_rect.x - blitted_blue_character.get_width() / 2 + 60,
                                         185))

    pygame.display.update()
    return red_character_button_rect, blue_character_button_rect


# Create a pygame.event.MOUSEBUTTONDOWN event handler that checks if the mouse is clicked inside the button's boundaries
def on_mouse_button_down(event):
    global chosen_character

    button_distance_from_border = 60

    red_character_button_rect = pygame.Rect(button_distance_from_border, INITIAL_WINDOW_HEIGHT - 170, 100, 100)
    blue_character_button_rect = pygame.Rect(INITIAL_WINDOW_WIDTH - button_distance_from_border - 100,
                                             red_character_button_rect.y, 100, 100)

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and red_character_button_rect.collidepoint(event.pos):
        chosen_character = "red"

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and blue_character_button_rect.collidepoint(event.pos):
        chosen_character = "blue"


def main():
    global chosen_character

    initial_window_run = True
    continue_running_check = CONTINUE_RUNNING

    while initial_window_run:
        drawing_initial_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                initial_window_run = False
                continue_running_check = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            initial_window_run = False

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            on_mouse_button_down(event)
            initial_window_run = False

    pygame.quit()

    return continue_running_check, chosen_character
