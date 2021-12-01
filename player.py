import pygame
from pygame.draw import rect
from collisons import Collison

class Player:
    def __init__(self, posx, posy, OBJX, OBJY, P_MOUSEX, P_MOUSEY, WIN):
        self.posx = posx
        self.posy = posy
        self.obj_width = OBJX
        self.obj_height = OBJY
        self.mouse_x = P_MOUSEX
        self.mouse_y = P_MOUSEY
        self.VELO = 4
        self.VELX = self.VELO
        self.VELY = self.VELO

        # section of constructor used for biltting the player onto the screen
        self.playerlist_left = []
        self.playerlist_right = []
        self.current_frame = 0
        self.framecount = 0
        
        self.WALK_COOLDOWN = 7
        self.WIN = WIN
        # direction of the player sprite, to help with the animation; 1-> facing right, 0 for left
        self.DIRECTION = 1


        for _ in range(1, 4):
            tempimg_left = pygame.image.load(f'assets/player{_}.png')
            tempimg_left = pygame.transform.scale(tempimg_left, (36, 36))
         
            tempimg_right = pygame.transform.flip(tempimg_left, True, False)

            self.playerlist_left.append(tempimg_left)
            self.playerlist_right.append(tempimg_right)

        self.checker = Collison(self.playerlist_right[0]) # COLLISON CHECKING


    def draw_player(self):
        if self.DIRECTION == 0:
            self.oneframe_image = self.playerlist_right[self.current_frame]
        else:
            self.oneframe_image = self.playerlist_left[self.current_frame]
        
        self.oneframe_rect = self.oneframe_image.get_rect(center = (self.posx, self.posy))
        self.WIN.blit(self.oneframe_image, self.oneframe_rect)

    def check_collisons(self, maplist):
        self.x_obs, self.y_obs = self.checker.find_collisons(self.posx, self.posy, maplist, self.VELX, self.VELY)

    def movement(self, key):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        
        if self.mouse_x > self.posx:
            self.DIRECTION = 1
        else:
            self.DIRECTION = 0

        if self.y_obs:
            self.posy += -(self.VELY)
        
        if self.x_obs:
            self.posx += -(self.VELX)


        if key[pygame.K_w] and self.posy > 30:
            self.VELY = -(self.VELO)
            self.posy += self.VELY
            self.framecount += 1
            
        if key[pygame.K_s] and self.posy + self.obj_height < 580:
            self.VELY = (self.VELO)

            self.posy += self.VELY
            self.framecount += 1

        if key[pygame.K_a] and self.posx > 45:
            self.VELX = -(self.VELO)
            self.posx += self.VELX
            self.framecount += 1

        if key[pygame.K_d] and self.posx + self.obj_width < 1180:
            self.VELX = (self.VELO)

            self.posx += self.VELX
            self.framecount += 1

        if not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_s] and not key[pygame.K_d]:
            self.framecount = 0
            self.current_frame = 0
         
        if self.framecount > self.WALK_COOLDOWN:
            self.framecount = 0
            if self.DIRECTION == 1:
                self.current_frame = (self.current_frame + 1)%len(self.playerlist_right)
            else:
                self.current_frame = (self.current_frame + 1)%len(self.playerlist_left)

            
    def shoot(self):
        return (self.posx, self.posy)



if __name__ == "__main__":
    player1 = Player()