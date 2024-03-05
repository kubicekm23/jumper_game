import pygame
pygame.init()

GRAYISH_WHITE = (242, 243, 245)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (245, 10, 10)
ACTIVE_COLOR = (230, 211, 125)
INACTIVE_COLOR = (219, 193, 74)

CONTINUE_RUNNING = True

INITIAL_WINDOW_WIDTH = 400
INITIAL_WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))
pygame.display.set_caption("Initial settings")

chosen_character = None

name_input_box = pygame.Rect(INITIAL_WINDOW_WIDTH / 2 - 125, 100, 250, 70)
input_box_color = INACTIVE_COLOR
active = False
text = ''
name_chosen = False


def input_box():
    global done, active, text, input_box_color

    for event in pygame.event.get():
        print("Event type:", event.type)  # Debug print
        if event.type == pygame.QUIT:
            return True, None

        if event.type == pygame.MOUSEBUTTONDOWN:
            if name_input_box.collidepoint(event.pos):
                active = True
                print("test")
            else:
                active = False
            print("test2")
            input_box_color = ACTIVE_COLOR if active else INACTIVE_COLOR

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            print("test 3")

    if text == "":
        text = "Vyberte si jméno"

    return False, None


def drawing_initial_window():
    global text

    SCREEN.fill(GRAYISH_WHITE)
    SCREEN.blit(pygame.image.load("images/potential_backgrond_full_effects.png"), (0, 0))

    # Drawing input box
    pygame.draw.rect(SCREEN, input_box_color, name_input_box, 2)
    font = pygame.font.SysFont('Calibri', 30)
    text_surface = font.render(text, True, BLACK)
    SCREEN.blit(text_surface, (name_input_box.centerx - text_surface.get_width() / 2, name_input_box.centery - text_surface.get_height() / 2))

    button_distance_from_border = 60
    red_character_button_rect = pygame.Rect(button_distance_from_border, INITIAL_WINDOW_HEIGHT - 170, 100, 100)
    blue_character_button_rect = pygame.Rect(INITIAL_WINDOW_WIDTH - button_distance_from_border - 100,
                                             red_character_button_rect.y, 100, 100)

    red_character = pygame.image.load("images/red_character.png")
    blue_character = pygame.image.load("images/blue_character.png")

    blitted_red_character = pygame.transform.scale(red_character, (200, 200))
    blitted_blue_character = pygame.transform.scale(blue_character, (200, 200))

    menu_text = pygame.font.SysFont('Calibri', 28)
    top_text = menu_text.render('Vyberte si postavu a jméno,', 1, BLACK)
    top_text_2 = menu_text.render('se kterými budete hrát tuto hru.', 1, BLACK)

    SCREEN.blit(top_text, (INITIAL_WINDOW_WIDTH / 2 - top_text.get_width() / 2, 20))
    SCREEN.blit(top_text_2, (INITIAL_WINDOW_WIDTH / 2 - top_text_2.get_width() / 2, 55))

    SCREEN.blit(blitted_red_character, (red_character_button_rect.x - blitted_red_character.get_width() / 2 + 60,
                                        185))
    SCREEN.blit(blitted_blue_character, (blue_character_button_rect.x - blitted_blue_character.get_width() / 2 + 60,
                                         185))

    pygame.display.update()
    return red_character_button_rect, blue_character_button_rect


def on_mouse_button_down(event):
    global chosen_character

    button_distance_from_border = 60
    red_character_button_rect = pygame.Rect(button_distance_from_border, INITIAL_WINDOW_HEIGHT - 170, 100, 100)
    blue_character_button_rect = pygame.Rect(INITIAL_WINDOW_WIDTH - button_distance_from_border - 100,
                                             red_character_button_rect.y, 100, 100)

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if red_character_button_rect.collidepoint(event.pos):
            chosen_character = "red"
        elif blue_character_button_rect.collidepoint(event.pos):
            chosen_character = "blue"


def main():
    global chosen_character

    initial_window_run = True
    continue_running_check = CONTINUE_RUNNING

    while initial_window_run:
        done, character = input_box()
        if done:
            return False, None

        drawing_initial_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                initial_window_run = False
                continue_running_check = False
            on_mouse_button_down(event)  # Move this line inside the event loop

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            initial_window_run = False

        name_chosen = True
        if (chosen_character == "red" or chosen_character == "blue") and name_chosen:
            initial_window_run = False

    pygame.quit()
    return continue_running_check, chosen_character

if __name__ == "__main__":
    main()
