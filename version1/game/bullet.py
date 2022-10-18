import pyglet
from . import physicalobject
from . import resources
from . import util

import math


bullets = []


class Bullet(physicalobject.PhysicalObject):

    # dx = 500
    # dy = 500

    dx = 10
    dy = 10

    def __init__(self, corner, *args, **kwargs):
        super().__init__(img=resources.bullet_image, *args, **kwargs)
        self.corner = corner
        # print(corner)
        self.scale_x = 5
        self.scale_y = 5
        bullets.append(self)


    def update(self, dt):
        rad = -math.radians(self.corner)
        cosA = math.cos(rad)
        sinA = math.sin(rad)
        # print(cosA)
        shiftX = self.dx  * cosA
        shiftY = self.dy  * sinA
        radius = self.width/2


        # print(right_wall_distance)
        self.x += shiftX
        self.y += shiftY





    def collides_with_walls(self):
        collision_distance = self.width / 2
        left = [0, self.y]
        right = [800, self.y]
        bottom = [self.x, 0]
        top = [self.x, 600]

        if self.x + collision_distance >= right[0]:#and top and bottom
            self.dx *= -1

        if self.x - collision_distance <= left[0]:#and top and bottom
            self.dx *= -1

        if self.y + collision_distance >= top[1]:
            self.dy *= -1

        if self.y - collision_distance <= bottom[1]:
            self.dy *= -1

        # collision_distance = self.width / 2
        # left = [0, self.y]
        # right = [800, self.y]
        # bottom = [self.x, 0]
        # top = [self.x, 600]
        # walls = [right, left, top, bottom]
        # for wall in walls:
        #     actual_distance = util.distance(self.position, wall)
        #     collision = actual_distance <= collision_distance
        #     if collision:
        #         # print(wall == right)
        #         if wall == right:
        #             self.dx *= -1
        #         if wall == left:
        #             self.dx *= -1
        #         if wall == top:
        #             self.dy *= -1
        #         if wall == bottom:
        #             self.dy *= -1


    def collides_with_animal(self, animal):
        collision_distance = self.width / 2 + animal.radius
        # print(collision_distance)

        distance = util.distance(self.position, animal.position)
        if distance <= collision_distance:
            if not animal.is_dead:
                animal.is_dead = True
                print('killed')










