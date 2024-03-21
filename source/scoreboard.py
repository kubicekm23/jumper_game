import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scoreboard")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 20)

# Set up initial score
score = 0


def draw(time_spent, score_list):
    screen.fill(WHITE)

    difference = 0
    distance = 20

    score_text = font.render("Váš čas: " + str(time_spent), True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 25))

    # tabulka s minulými skóre
    for score in score_list:
        player_name, player_time = score.split(", ")

        name_list_text = font.render(str(player_name), True, BLACK)
        screen.blit(name_list_text, (12, 60 + distance + difference + 2))

        time_list_text = font.render(str(player_time), True, BLACK)
        screen.blit(time_list_text, (SCREEN_WIDTH - 12 - time_list_text.get_width(), 60 + distance + difference + 2))

        line = pygame.Rect(10, 60 + distance + difference, 480, 2)
        pygame.draw.rect(screen, BLACK, line)

        difference += 25

    pygame.display.flip()


def main(minutes, seconds, player_name, win_check):
    run = True
    time_spent = "%d:%02d" % (minutes, seconds)
    win = win_check

    if win:
        soubor = open('scoreboard_data.txt', 'a', encoding='utf-8')
        soubor.write(player_name + ", " + time_spent + '\n')
        soubor.close()

    soubor = open("scoreboard_data.txt", 'r', encoding='utf-8')
    score_list = []

    for radek in soubor:
        score_list.append(radek[:-1])

    soubor.close()



    while run:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(time_spent, score_list)

    pygame.quit()
    sys.exit()
