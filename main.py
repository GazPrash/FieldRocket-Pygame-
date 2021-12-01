import pygame, sys
from player import Player
from event_handling import Bullets
from world import WorldMap


#PYGAME CONFIGS--> INIT, CONSTS, SET WINDOW & LOADING SPRITES
pygame.init()

DISPLAY_X = 1200
DISPLAY_Y = 600
DISPLAY_RES = (DISPLAY_X, DISPLAY_Y)
BG_COLOR = (225, 163, 228)
POSX = 450
POSY = 350
GAME_FPS = 60
DISPLAY = pygame.display.set_mode(DISPLAY_RES)
pygame.display.set_caption('FIELD-ROCKET')
pygame.mouse.set_visible(False)

game_clock = pygame.time.Clock()

#PYMUNK CONFIGS--> CONSTS, SPACE
# FORCE = 500
# gamespace = pymunk.Space()
# gamespace.gravity = (0, FORCE)

map_load = []
map_sprites = []

with open('assets/binary_maps.txt', 'r') as f:
    for lines in f:
        map_load.append(lines)

outer_trees = pygame.image.load('assets/outer_trees.png')
outer_trees = pygame.transform.scale(outer_trees, (50, 50))
turf_tile = pygame.image.load('assets/leaves.png')
turf_tile = pygame.transform.scale(turf_tile, (50, 50))

brick_tile = pygame.image.load('assets/obstacle.png')
brick_tile = pygame.transform.scale(brick_tile, (50, 50))

inner_trees = pygame.image.load('assets/inner_trees.png')
inner_trees = pygame.transform.scale(inner_trees, (50, 50))

map_sprites.append(outer_trees)
map_sprites.append(turf_tile)

crosshair = pygame.image.load('assets/crosshair.png')
crosshair = pygame.transform.scale(crosshair, (21, 21))

for i in range(6, 8):
    img = pygame.image.load(f'assets/mainland{i}.png')
    img = pygame.transform.scale(img, (50, 50))
    map_sprites.append(img)


world1 = WorldMap(map_load, map_sprites, brick_tile, DISPLAY, inner_trees)
world1.set_map()
obst_list = world1.collison_handling()

player1 = Player(POSX, POSY, 32, 32, *(pygame.mouse.get_pos()), DISPLAY)
bullets_spritegroup = pygame.sprite.Group()

#MAINLOOP
while True:
    DISPLAY.fill((46, 204, 113))
    world1.blit_map()
    game_clock.tick(GAME_FPS)
    DISPLAY.blit(crosshair, pygame.mouse.get_pos())
    # print(game_clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            bullets_spritegroup.add(Bullets(*(player1.shoot()), mousex, mousey, player1.DIRECTION))


    player1.draw_player()

    key = pygame.key.get_pressed()   
    if key:
        player1.check_collisons(obst_list)
        player1.movement(key)

    bullets_spritegroup.update(obst_list)
    bullets_spritegroup.draw(DISPLAY)

    pygame.display.update()


pygame.quit()