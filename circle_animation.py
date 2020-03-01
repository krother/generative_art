"""
example of animating stuff with arcade
"""
import arcade
from math import radians, cos, sin

SIZEX = 1800
SIZE = 1000
ORI = SIZE // 2
ORIX = 800

#TODO: use a SpriteList to make the graphics faster

def circle(orix, oriy, angle, radius, size, col):
    ofsx = round(cos(radians(angle)) * radius)
    ofsy = round(sin(radians(angle)) * radius)
    arcade.draw_circle_filled(orix + ofsx, oriy + ofsy, size, col)
    #arcade.draw_circle_outline(orix + ofsx, oriy + ofsy, size, col)#, angle*5)

def circlecircle(angle_ofs, radius, size, col):
    for ang in range(0, 360, 30):
        circle(ORIX, ORI, ang + angle_ofs, radius, size, col)


class VJ(arcade.Window):

    def __init__(self):
        super().__init__(SIZEX, SIZE, "VJ")
        arcade.set_background_color(arcade.color.BLACK)
        self.x = 0

    def on_draw(self):
        arcade.start_render()
        circlecircle(self.x * 0.5, 400, 56, arcade.color.PURPLE)
        circlecircle(-self.x, 300, 42, arcade.color.BLUE)
        circlecircle(self.x * 1.5, 200, 28, arcade.color.GREEN)
        circlecircle(-self.x * 2, 100, 14, arcade.color.RED)
        #arcade.finish_render()

    def update(self, delta_time):
        self.x += 0.5
        if self.x > 360:
            self.x = 0


window = VJ()
arcade.run()
