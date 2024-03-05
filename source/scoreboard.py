#TODO: scoreboard loading
#TODO: scoreboard display

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

# Set up initial score
score = 0


def draw(time_spent):
    screen.fill(WHITE)

    score_text = font.render("Your time spent Playing: " + str(time_spent), True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 20))

    pygame.display.flip()


def main(minutes, seconds):
    run = True
    time_spent = "%d:%d" % (minutes, seconds)

    while run:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(time_spent)

    pygame.quit()
    sys.exit()
