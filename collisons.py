import pygame


class Collison:
    def __init__(self, player_img):
        self.player = player_img
        self.player_rect = self.player.get_rect()
        self.player_width = self.player.get_width()
        self.player_height = self.player.get_height()

    def find_collisons(self, posx, posy, obst_list, dx, dy):
        x_blocked = False
        y_blocked = False

        if dx < 0:
            dx *= 6


        # checks collisons for x direction
        for rect in obst_list:
            if rect.colliderect(
                posx + dx,
                posy,
                self.player_width,
                self.player_height
            ):
                x_blocked = True

        for rect in obst_list:
            if rect.colliderect(
                posx,
                posy + dy,
                self.player_width,
                self.player_height
            ):
                y_blocked = True

        
        return (x_blocked, y_blocked)











