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
    MOVEMENT_MODIFIER = 2
    EXTRA_SIZE_X = 1020
    EXTRA_SIZE_Y = 700

elif system_width > 1200:
    WIDTH = 1500
    HEIGHT = 500
    MOVEMENT_MODIFIER = 1
    EXTRA_SIZE_X = 0
    EXTRA_SIZE_Y = 0

else:
    print("resolution setting failed")
    WIDTH = 1200
    HEIGHT = 500
    MOVEMENT_MODIFIER = 1
    EXTRA_SIZE_X = 0
    EXTRA_SIZE_Y = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping game")

clock = pygame.time.Clock()

# characters
red_character = pygame.image.load("images/red_character.png")
blittable_red_character = pygame.transform.scale(red_character, (50, 50))

blue_character = pygame.image.load("images/blue_character.png")
blittable_blue_character = pygame.transform.scale(blue_character, (50, 50))

# hodnoty pohybu pozadí
cloud_scroll = 0
ground_scroll = 0
general_scroll = 0

PLAYER_VEL = 5

# background images
cloud_image = pygame.image.load("images/clouds.png").convert_alpha()
ground_image = pygame.image.load("images/ground.png").convert()
if not large_window:
    mountain_image = pygame.transform.scale(pygame.image.load("images/mountain.png"), (1200 + EXTRA_SIZE_X, 500 + EXTRA_SIZE_Y))
    ground = pygame.transform.scale(ground_image, (50, 50))
elif large_window:
    mountain_image = pygame.transform.scale(pygame.image.load("images/mountain.png"), (1200 + EXTRA_SIZE_X, 500 + EXTRA_SIZE_Y))
    ground = pygame.transform.scale(ground_image, (100, 100))
    # TODO: add a large mountain.png

# nastavení proměnných pozadí
tiles = math.ceil(WIDTH / mountain_image.get_height())
ground_tiles = math.ceil(WIDTH / mountain_image.get_width() + 30)
ground_width = ground.get_width()
ground_height = ground.get_height()

# pozice hráče
player_initial_position = (WIDTH / 2 - 27, HEIGHT - ground_height)
player_height, player_width = 55, 50
player_rect = pygame.Rect((player_initial_position[0], player_initial_position[1] - player_height, player_height, player_width))

# pohybové rozmezí pro postavu
zone_left = pygame.Rect((WIDTH / 2 - 80), 0, 5, HEIGHT)
zone_right = pygame.Rect((WIDTH / 2 + 80), 0, 5, HEIGHT)

# otočení postavy
facing_left = False
facing_right = False

# sbíratelné hvězdičky
collectible_star1 = pygame.image.load("images/star.png").convert_alpha()
collectible_star2 = pygame.image.load("images/star.png").convert_alpha()
collectible_star3 = pygame.image.load("images/star.png").convert_alpha()

collected_star1 = False
collected_star2 = False
collected_star3 = False


#hráč
class Character:
    def __init__(self, name, skin, health, health_max):
        self.name = name
        self.skin = skin
        self.health = health
        self.health_max = health_max
        self.rect = pygame.Rect(WIDTH / 2, HEIGHT - ground_height - player_height, 50, 50)
        self.velocity = 0
        self.collected_star1 = False
        self.collected_star2 = False
        self.collected_star3 = False


def movement(player):
    global facing_left, facing_right, general_scroll, cloud_scroll, PLAYER_VEL, ground_scroll

    delta_time = clock.tick(60) / 25
    keys = pygame.key.get_pressed()
    touching_ground = False
    touching_top = False

    ground_collisions = pygame.Rect(0, (HEIGHT - ground_height), WIDTH, ground_height)

    #kontrola proti skákání ve vzduchu
    if player_rect.colliderect(ground_collisions):
        touching_ground = True
    elif not player_rect.colliderect(ground_collisions):
        touching_ground = False

    #kontrola zda je hráč na zemi, pokud jo tak ho posune na tu zem
    if player_rect.y > HEIGHT - ground_height:
        player_rect.y = HEIGHT - ground_height - player_rect.height

    #pohyb do leva
    if keys[pygame.K_LEFT] and player_rect.colliderect(zone_left) or keys[pygame.K_a] and player_rect.colliderect(
        zone_left):
        general_scroll += PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        cloud_scroll += PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        ground_scroll += PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        #for obstacle in obstacles:
        #    obstacle.move(PLAYER_VEL * delta_time)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= 2 * MOVEMENT_MODIFIER
        #otáčení hráče
        if not facing_left:
            facing_right = False
            facing_left = True
            player.skin = pygame.transform.flip(player.skin, True, False)

    #pohyb do prava
    if keys[pygame.K_RIGHT] and player_rect.colliderect(zone_right) or keys[pygame.K_d] and player_rect.colliderect(
            zone_right):
        general_scroll -= PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        cloud_scroll -= PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        ground_scroll -= PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        #for obstacle in obstacles:
        #    obstacle.move(-PLAYER_VEL * delta_time)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += 2 * MOVEMENT_MODIFIER
        if not facing_right:
            facing_right = True
            facing_left = False
            player.skin = pygame.transform.flip(player.skin, True, False)


def draw(character_skin):
    global cloud_scroll, general_scroll, ground_scroll
    clock.tick(60)
    screen.fill((0, 0, 0))

    screen.blit(mountain_image, (0, 0))

    # clouds
    for i in range(-2, tiles + 2):
        screen.blit(cloud_image, (i * mountain_image.get_width() + cloud_scroll, 0))

        # vyresetování scroll_cloud
        if abs(cloud_scroll) > mountain_image.get_width():
            cloud_scroll = 0
    cloud_scroll += 0.2 * MOVEMENT_MODIFIER

    # zem
    for i in range(-9, ground_tiles + 9):
        screen.blit(ground, (i * ground_width + ground_scroll, HEIGHT - ground_height))
        screen.blit(ground, (i * ground_width + ground_scroll - 50, HEIGHT - ground_height))
        # vyresetování scroll
        if abs(ground_scroll) > ground_width:
            ground_scroll = 0

    screen.blit(character_skin, (player_rect.x, player_rect.y))

    pygame.display.update()


def main(chosen_character):
    global continue_running_check

    run = True

    if chosen_character == "red":
        character_skin = blittable_red_character
    elif chosen_character == "blue":
        character_skin = blittable_blue_character
    else:
        print("choosing character failed in main_game.py, choosing red")
        character_skin = blittable_red_character
    player = Character(name="test", skin=character_skin, health=5, health_max=5)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue_running_check = False

        draw(character_skin)
        movement(player)


# TODO: postava
# TODO: pohyb
# TODO: překážky
#   možná použít upravený ground images a dát jim rect vlastnosti?
# TODO: výhra
win = True
time_spent = 0
