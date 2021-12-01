import pygame, random

class WorldMap:
    def __init__(self, map, sprites, brick_tile, surface, inner_trees):
        self.map = map
        self.surface = surface
        self.outer_trees = sprites[0]
        self.turf_tile = sprites[1]
        self.mainland = sprites[2:]
        self.total_sprite_list = []
        self.brick = brick_tile
        self.obstacles = []
        self.inner_trees = inner_trees


    def set_map(self):
        for rown, data in enumerate(self.map):
            for coln, tile in enumerate(data):
                if tile == '1':
                    self.total_sprite_list.append((self.outer_trees, self.outer_trees.get_rect(center = (50*coln, 50*rown))))
                
                elif tile == '.':
                    temp_img = random.choice(self.mainland)
                    self.total_sprite_list.append((temp_img, temp_img.get_rect(center = (50*coln, 50*rown))))
                
                elif tile == '0' or tile == '3':
                    if tile == '3':
                        self.total_sprite_list.append((self.inner_trees, self.inner_trees.get_rect(center = (50*coln, 50*rown))))
                    else:
                        img_rect = self.brick.get_rect(center = (50*coln, 50*rown))
                        self.total_sprite_list.append((self.brick, img_rect))
                        self.obstacles.append(img_rect)
                    
                elif tile == '2':
                    self.total_sprite_list.append((self.turf_tile, self.turf_tile.get_rect(center = (50*coln, 50*rown))))

    def blit_map(self):
        for tiles in self.total_sprite_list:
            self.surface.blit(*tiles)

    def collison_handling(self):
        # DOESN'T ACTUALLY HELP IN COLLISON HANDLING, JUST RETURNS THE TILE-LIST OF OBSTACLES
        # SO THAT COLLISONS CAN BE DETECTED IN THE PLAYER MODULE
        return self.obstacles