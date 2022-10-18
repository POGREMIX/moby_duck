import pyglet
from . import resources
from . import physicalobject
from pyglet.window import key


class Duck(physicalobject.PhysicalObject):

    dx = 400
    dy = 240

    scaleX = 0.7
    scaleY = 0.7

    is_dead = False

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.duck_image, *args, **kwargs)

        self.scale_x = self.scaleX
        self.scale_y = self.scaleY
        self.x = self.width/2
        self.y = self.height/2

        self.key_handler = key.KeyStateHandler()

        self.radius = self.width/2


    def say(self):
        print('quack, quack!!!')

    def jump(self):
        self.y += 15

    def update(self, dt):

        speed = 5
        if self.key_handler[key.A]:
            # print('L')
            self.x-=speed
        if self.key_handler[key.D]:
            # print('R')
            self.x += speed
        if self.key_handler[key.W]:
            # print('U')
            self.y += speed
        if self.key_handler[key.S]:
            # print('D')
            self.y -= speed
        if self.key_handler[key.SPACE]:
            self.jump()

    def set_start_position(self, x, y):
        self.x = x
        self.y = y


