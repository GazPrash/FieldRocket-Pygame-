import pygame, math
class Bullets(
    pygame.sprite.Sprite
):  # posx-->player posn, for objs we can use objx, objy
    def __init__(self, objx, objy, xprime, yprime, player_direct):
        super().__init__()
        self.xprime = xprime
        self.yprime = yprime
        self.objx = objx
        self.objy = objy

        self.image = pygame.image.load("assets/bullet_alt.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect(center=(objx, objy))
        self.rect.x = objx
        self.rect.y = objy

        self.theta = math.atan2(self.yprime - objy, self.xprime - objx)
        # self.theta_deg = (self.theta * 180)/math.pi   // FOR CHECKING AND DEBBUGING
        self.VELOCITY = 15
        self.direction = player_direct
        self.terminal = False

    def update(self, obst_list):
        for rect in obst_list:
            if rect.colliderect(
                self.objx, self.objy, self.image.get_width(), self.image.get_height()
            ):
                self.terminal = True

        if (
            (self.direction == 1 and self.xprime >= self.objx and not self.terminal)
            or (self.direction == 0 and self.xprime < self.objx and not self.terminal)
        ):

            self.velx = self.VELOCITY * (math.cos(self.theta))
            self.vely = self.VELOCITY * (math.sin(self.theta))

            self.objx += self.velx
            self.objy += self.vely

            self.rect.x = int(self.objx)
            self.rect.y = int(self.objy)

        else:
            self.kill()
            self.terminal = False

    def termination(self):
        pass

        # if self.rect.x+ self.rect.y >= self.xprime + self.yprime:
        #     self.kill()


class StaticBodies(pygame.sprite.Sprite):
    pass
