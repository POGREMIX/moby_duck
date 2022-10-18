import pyglet
from . import physicalobject
from . import resources
from . import bullet
from pyglet.window import key
from pyglet.window import mouse
import math


class Cannon(physicalobject.PhysicalObject):
    bullets = []

    def __init__(self, batch, group, bullet_group, *args, **kwargs):
        super().__init__(img=resources.gun_bottom_image, batch=batch, *args, **kwargs)
        self.x = self.width / 2

        # убрал фитиль
        self.y = self.height / 2 - 20
        self.scale_y = 0.7
        self.scale_x = 0.7

        self.gun_top_sprite = pyglet.sprite.Sprite(resources.gun_top_image, *args, **kwargs)
        self.gun_top_sprite.visible = True

        self.gun_top_sprite.x = self.x

        # соединение ствола с опорой
        self.gun_top_sprite.y = self.y + 45

        self.gun_top_sprite.scale_y = self.scale_y
        self.gun_top_sprite.scale_x = self.scale_x

        # self.gun_top_sprite.batch = batch
        # self.batch = batch
        self.gun_top_sprite.batch = self.batch
        self.gun_top_sprite.group = group
        self.group = group
        self.bullet_group = bullet_group

        # self.mouse_handler = mouse.MouseStateHandler()

        self.bullet_start_position_x = 210 - 40#self.gun_top_sprite.x
        self.bullet_start_position_y = 95#self.gun_top_sprite.y


    def update(self):
        print('s')
        # if self.mouse_handler[mouse.LEFT]:
        #     print('L')
        # if self.mouse_handler[mouse.RIGHT]:
        #     print('R')
        # if self.mouse_handler[mouse.MIDDLE]:
        #     print('M')

    def fire(self):

        gun_height = self.gun_top_sprite.height/2

        new_bullet = bullet.Bullet(corner=self.gun_top_sprite.rotation,
                                   x=self.bullet_start_position_x, y=self.bullet_start_position_y,
                                   batch=self.batch,
                                   group=self.bullet_group)
        resources.gun_shot.play()
        self.bullets.append(new_bullet)
        # self.group

    def calc_gun_degree(self, x, y):
        b = x - self.gun_top_sprite.x
        a = y - self.gun_top_sprite.y

        c = math.sqrt(a ** 2 + b ** 2)

        cos = b / c
        arccos = math.acos(cos)
        d = math.degrees(arccos)
        # print(d)

        if x >= self.gun_top_sprite.x and y >= self.gun_top_sprite.y:
            degree = d
        if x < self.gun_top_sprite.x and y >= self.gun_top_sprite.y:
            degree = d
        if x <= self.gun_top_sprite.x and y < self.gun_top_sprite.y:
            degree = 180 + 180 - d
        if x > self.gun_top_sprite.x and y < self.gun_top_sprite.y:
            degree = 180 + (180 - d)
        return degree

    def set_bullet_start_position(self, degree):
        radians = math.radians(degree)
        gunTopWidth = self.gun_top_sprite.width / 2 - 20  # - 130

        bullet_x = self.gun_top_sprite.x + math.cos(radians) * gunTopWidth
        bullet_y = self.gun_top_sprite.y + math.sin(radians) * gunTopWidth

        self.bullet_start_position_x = bullet_x
        self.bullet_start_position_y = bullet_y

    def delete(self):
        self.gun_top_sprite.delete()
        super(physicalobject.PhysicalObject, self).delete()




