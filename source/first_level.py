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
    SIZE_MODIFIER = 2
    EXTRA_SIZE_X = 1020
    EXTRA_SIZE_Y = 700
    BACKGROUND_INIT_X = 800
    BACKGROUND_INIT_Y = -10855
    LARGE_MAP = True
    star1_x = 2318
    star1 = pygame.Rect(star1_x, 926 - 40, 40, 40)
    star2_x = 1487
    star2 = pygame.Rect(star2_x, -868, 40, 40)

elif system_width > 1200:
    WIDTH = 1500
    HEIGHT = 500
    MOVEMENT_MODIFIER = 1.5
    SIZE_MODIFIER = 1
    EXTRA_SIZE_X = 0
    EXTRA_SIZE_Y = 0
    BACKGROUND_INIT_X = 800
    BACKGROUND_INIT_Y = -11525
    LARGE_MAP = False
    star1_x = 2318
    star1 = pygame.Rect(star1_x, 926 - 670 - 40, 40, 40)
    star2_x = 1487
    star2 = pygame.Rect(star2_x, -868 - 670, 40, 40)

else:
    print("resolution setting failed")
    WIDTH = 1200
    HEIGHT = 500
    MOVEMENT_MODIFIER = 1.5
    SIZE_MODIFIER = 1
    EXTRA_SIZE_X = 0
    EXTRA_SIZE_Y = 0
    BACKGROUND_INIT_X = 800
    BACKGROUND_INIT_Y = -11525
    LARGE_MAP = False
    star1_x = 2318
    star1 = pygame.Rect(star1_x, 926 - 670 - 50, 50, 50)
    star2_x = 1487
    star2 = pygame.Rect(star2_x, -868 - 670, 40, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping game")

clock = pygame.time.Clock()

# barvičky
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# characters
red_character = pygame.image.load("images/red_character.png")
blittable_red_character = pygame.transform.scale(red_character, (50 * SIZE_MODIFIER, 50 * SIZE_MODIFIER))

blue_character = pygame.image.load("images/blue_character.png")
blittable_blue_character = pygame.transform.scale(blue_character, (50 * SIZE_MODIFIER, 50 * SIZE_MODIFIER))

# hodnoty pohybu pozadí
cloud_scroll = 0
ground_scroll = 0
general_scroll = 0

PLAYER_VEL = 5
player_up_speed = 0
GRAVITY = 1
player_speed_x = 0

# background images
cloud_image = pygame.image.load("images/clouds.png").convert_alpha()
ground_image = pygame.image.load("images/ground.png").convert()
mountain_image = pygame.transform.scale(pygame.image.load("images/mountain.png"), (1200 + EXTRA_SIZE_X,
                                                                                   500 + EXTRA_SIZE_Y))
ground = pygame.transform.scale(ground_image, (50 * MOVEMENT_MODIFIER, 50 * MOVEMENT_MODIFIER))
main_background_image = pygame.image.load("images/background.png").convert_alpha()
main_background_image_y = 0
main_background_image_opendoors = pygame.image.load("images/door_opened.png").convert_alpha()


# nastavení proměnných pozadí
tiles = math.ceil(WIDTH / mountain_image.get_height())
ground_tiles = math.ceil(WIDTH / mountain_image.get_width() + 30)
ground_width = ground.get_width()
ground_height = ground.get_height()

# pozice hráče
player_initial_position = (WIDTH / 2 - 27, HEIGHT - ground_height)
player_height = 55 * SIZE_MODIFIER
player_width = 50 * SIZE_MODIFIER
player_rect = pygame.Rect((
    player_initial_position[0],
    player_initial_position[1] - player_height,
    player_height,
    player_width))

# pohybové rozmezí pro postavu
zone_left = pygame.Rect((WIDTH / 2 - 80), 0, 5, HEIGHT)
zone_right = pygame.Rect((WIDTH / 2 + 80), 0, 5, HEIGHT)

# otočení postavy
facing_left = False
facing_right = False

# skákací hodnoty
touching_ground = False
touching_top = False

# sbíratelné hvězdičky
collectible_star1 = pygame.image.load("images/star.png").convert_alpha()
collectible_star2 = pygame.image.load("images/star.png").convert_alpha()
collectible_star3 = pygame.image.load("images/star.png").convert_alpha()

collected_star1 = False
collected_star2 = False
collected_star3 = False


# hráč
class Character:
    def __init__(self, name, skin, health, health_max):
        self.name = name
        self.skin = skin
        self.health = health
        self.health_max = health_max
        self.rect = pygame.Rect(WIDTH / 2, HEIGHT - ground_height - player_height, 50, 50)
        self.velocity = 0


# platformy
class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, general_scroll):
        self.rect.x += general_scroll

    def movey(self, scroll_up):
        self.rect.y += scroll_up


def movement(player, obstacles):
    global facing_left, facing_right, general_scroll, cloud_scroll, PLAYER_VEL, ground_scroll, player_up_speed, \
        touching_ground, touching_top, player_speed_x, main_background_image_y, collected_star1, collected_star2, \
        collected_star3

    delta_time = clock.tick(60) / 25
    keys = pygame.key.get_pressed()

    ground_collisions = pygame.Rect(0, (HEIGHT - ground_height), WIDTH, ground_height)
    upper_barrier = pygame.Rect(0, 80 * MOVEMENT_MODIFIER, WIDTH, 1)
    bottom_barrier = pygame.Rect(0, HEIGHT - ground_height, WIDTH, 1)

    main_background_image_y = 0

    # kontrola proti skákání ve vzduchu
    if player_rect.colliderect(ground_collisions):
        touching_ground = True
    else:
        touching_ground = False

    for obstacle in obstacles:
        # povolit skákání z překážek
        if player_rect.colliderect(obstacle):
            touching_ground = True

        if player_rect.colliderect(obstacle.rect):
            # TODO: fix both sides of the obstacles
            # If there is a collision with the left side of the obstacle
            if player_rect.centery - 2 < obstacle.rect.bottomleft[1] and player_rect.centery - 2 > \
                    obstacle.rect.topleft[1] and facing_right:
                player_rect.x -= 5

            # If there is a collision with the right side of the obstacle
            elif player_rect.centery - 2 < obstacle.rect.bottomright[1] and player_rect.centery - 2 > \
                    obstacle.rect.topright[1] and facing_left:
                player_rect.x += 5

            # If there is a collision with the top of the obstacle
            elif (player_rect.top < obstacle.rect.top and player_rect.right > obstacle.rect.left + 4 and
                  player_rect.left < obstacle.rect.right - 4):
                player_rect.y = obstacle.rect.y - player_rect.height
                player_up_speed = 0  # Stop the player's vertical movement
                touching_ground = True

            # If there is a collision with the bottom of the obstacle, move the player down
            elif player_rect.y < obstacle.rect.bottom and player_rect.y > obstacle.rect.top and \
                    player_rect.x > obstacle.rect.left and player_rect.x < obstacle.rect.right:
                player_rect.y = obstacle.rect.y + player_rect.height
                player_up_speed = 0

    # kontrola zda je hráč na zemi, pokud jo tak ho posune na tu zem
    if player_rect.y + player_height > ground_collisions.y:
        player_rect.y = HEIGHT - ground_height - player_rect.height

    # pohyb do leva
    if keys[pygame.K_LEFT] and player_rect.colliderect(zone_left) or keys[pygame.K_a] and player_rect.colliderect(
            zone_left):
        general_scroll += PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        cloud_scroll += PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        ground_scroll += PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        for obstacle in obstacles:
            obstacle.move(PLAYER_VEL * delta_time * MOVEMENT_MODIFIER)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_speed_x = -PLAYER_VEL * MOVEMENT_MODIFIER * delta_time

        # otáčení hráče
        if not facing_left:
            facing_right = False
            facing_left = True
            player.skin = pygame.transform.flip(player.skin, True, False)

    # pohyb do prava
    if keys[pygame.K_RIGHT] and player_rect.colliderect(zone_right) or keys[pygame.K_d] and player_rect.colliderect(
            zone_right):
        general_scroll -= PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        cloud_scroll -= PLAYER_VEL * delta_time * MOVEMENT_MODIFIER
        ground_scroll -= PLAYER_VEL * delta_time * MOVEMENT_MODIFIER

        for obstacle in obstacles:
            obstacle.move(-PLAYER_VEL * delta_time * MOVEMENT_MODIFIER)

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_speed_x = PLAYER_VEL * MOVEMENT_MODIFIER * delta_time
        if not facing_right:
            facing_right = True
            facing_left = False
            player.skin = pygame.transform.flip(player.skin, True, False)

    # pohyby nahoru a dolů
    if keys[pygame.K_UP] and touching_ground or keys[pygame.K_SPACE] and touching_ground or keys[
            pygame.K_w] and touching_ground:
        player_up_speed = 15 * 1.3
        touching_ground = False

    # save
    if player_rect.y < upper_barrier.bottom and player_up_speed > 0:
        for obstacle in obstacles:
            obstacle.movey(player_up_speed)
        main_background_image_y += player_up_speed

    if (player_rect.y > bottom_barrier.top and player_up_speed < 0 and ground_collisions.y > HEIGHT
            - ground_collisions.height / 2):
        for obstacle in obstacles:
            obstacle.movey(-player_up_speed)
        main_background_image_y += player_up_speed

    else:
        player_rect.y -= player_up_speed

    if player_rect.y < 5:
        player_rect.y = 10

    star1.x = star1_x + general_scroll
    star1.y = obstacles[2].rect.y - star1.height * 4 - 5
    star2.x = star2_x + general_scroll + 20
    star2.y = obstacles[17].rect.y - star2.height - 5
    if player_rect.colliderect(star1):
        collected_star1 = True

    if player_rect.colliderect(star2):
        collected_star2 = True

    player_rect.x += player_speed_x
    if not touching_ground:
        player_up_speed -= GRAVITY
    # TODO: opravit pohyb mapy dolů, ground_collisions se nepohybuje dolů a asi ani nahoru, jelikož se nehýbe vůbec
    if not player_rect.colliderect(ground_collisions):
        ground_collisions.y += player_up_speed
    player_speed_x = 0


def draw(character_skin, current_character_skin, obstacles):
    global cloud_scroll, general_scroll, ground_scroll, main_background_image_y
    clock.tick(60)
    screen.fill((0, 168, 255))
    pygame.draw.rect(screen, (10, 68, 5), (0, obstacles[0].rect.y + 80, WIDTH, 100))

    if facing_left:
        current_character_skin = pygame.transform.flip(character_skin, True, False)
    if facing_right:
        current_character_skin = character_skin

    # clouds
    for i in range(-2, tiles + 2):
        screen.blit(cloud_image, (i * mountain_image.get_width() + cloud_scroll, -1000 + player_up_speed))

        # vyresetování scroll_cloud
        if abs(cloud_scroll) > mountain_image.get_width():
            cloud_scroll = 0
    cloud_scroll += 0.2 * MOVEMENT_MODIFIER

    # pozadí (800 + general_scroll, -10855
    screen.blit(main_background_image, (BACKGROUND_INIT_X + general_scroll, main_background_image_y))

    # vyresetování scroll
    if abs(ground_scroll) > ground_width:
        ground_scroll = 0

    if not collected_star1:
        screen.blit(collectible_star1, (star1.x, star1.y))
    if not collected_star2:
        screen.blit(collectible_star1, (star2.x, star2.y))
    if not collected_star3:
        pass

    screen.blit(current_character_skin, (player_rect.x, player_rect.y))

    pygame.display.update()


def level_finish_sequence(character_skin):
    screen.fill((0, 168, 255))

    screen.blit(main_background_image_opendoors, (BACKGROUND_INIT_X + general_scroll, main_background_image_y))

    if facing_left:
        current_character_skin = pygame.transform.flip(character_skin, True, False)
    if facing_right:
        current_character_skin = character_skin

    screen.blit(current_character_skin, (player_rect.x, player_rect.y))
    pygame.display.flip()

    # pozastavení před vypnutím
    pygame.time.wait(3000)


def main(chosen_character):
    global continue_running_check, main_background_image_y

    import map_storage
    if LARGE_MAP:
        returned_obstacles = map_storage.first_map()
        obstacles = returned_obstacles
    else:
        returned_obstacles = map_storage.second_map()
        obstacles = returned_obstacles

    win = None
    run = True
    time_playing = 0

    if chosen_character == "red":
        character_skin = blittable_red_character
    elif chosen_character == "blue":
        character_skin = blittable_blue_character
    else:
        print("choosing character failed in main_game.py, choosing red")
        character_skin = blittable_red_character
    player = Character(name="test", skin=character_skin, health=5, health_max=5)
    current_character_skin = character_skin

    door_unlock_rect = pygame.Rect(obstacles[24].rect.centerx - 25, obstacles[24].rect.y - 339, 50, 339)

    while run:
        time_playing += 1

        if collected_star1 and collected_star2:
            if player_rect.colliderect(door_unlock_rect):
                level_finish_sequence(character_skin)

                win = True
                continue_running_check = True
                run = False
                break

        draw(character_skin, current_character_skin, obstacles)
        movement(player, obstacles)

        # kolize k otevření dveří
        door_unlock_rect.x = obstacles[25].rect.centerx - 25
        door_unlock_rect.y = obstacles[25].rect.y - 339

        # nastavení pozadí.y aby bylo relativně k překážkám
        main_background_image_y = obstacles[0].rect.y - 10495 - 1385
        # TODO: překážky nesedí k pozadí, potřeba lehce upravit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue_running_check = False

    continue_running_check = True
    time_right_now = pygame.time.get_ticks()
    time_played = time_right_now - time_playing

    return win, time_played, continue_running_check

# TODO: pohyb obrazovky nahoru dolů
# TODO: překážky se nepohybují stejně
# TODO: výhra
