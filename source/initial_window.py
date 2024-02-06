import pygame.font

GRAYISH_WHITE = (242, 243, 245)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

CONTINUE_RUNNING = True

# úvodní okno
INITIAL_WINDOW_WIDTH = 400
INITIAL_WINDOW_HEIGHT = 600

SCREEN = pygame.display.set_mode((INITIAL_WINDOW_WIDTH, INITIAL_WINDOW_HEIGHT))
pygame.display.set_caption("Initial settings")


def drawing_initial_window():
    SCREEN.fill(GRAYISH_WHITE)
    resol_4k_rect = pygame.Rect(60, INITIAL_WINDOW_HEIGHT - 120, 100, 100)
    resol_hd_rect = pygame.Rect(INITIAL_WINDOW_WIDTH - 160, INITIAL_WINDOW_HEIGHT - 120, 100, 100)

    menu_text = pygame.font.SysFont('Calibri', 30)
    top_text = menu_text.render('Vyberte rozlišení, pro které', 1, BLACK)
    top_text_2 = menu_text.render('bude hra uzpůsobena.', 1, BLACK)

    SCREEN.blit(top_text, (INITIAL_WINDOW_WIDTH / 2 - top_text.get_width() / 2, INITIAL_WINDOW_HEIGHT - 202))
    SCREEN.blit(top_text_2, (INITIAL_WINDOW_WIDTH / 2 - top_text_2.get_width() / 2, INITIAL_WINDOW_HEIGHT - 170))

    pygame.draw.circle(SCREEN, BLUE, resol_4k_rect.center, 50)
    pygame.draw.circle(SCREEN, BLUE, resol_hd_rect.center, 50)

    pygame.display.update()


def main():
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

    pygame.quit()

    return continue_running_check

chosen_size = "4k"
if chosen_size == "4k":
    size = "res_4k"
else:
    size = "res_fullhd"

#TODO: zmáčknutelné tlačítko
#TODO: vybírání postav