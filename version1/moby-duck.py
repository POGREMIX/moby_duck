import random
import time
from datetime import datetime, timedelta
import pyglet
from game import resources
from game import animals
from game import gun
import math
from pyglet import clock
from pyglet.window import mouse
from game import game


window = pyglet.window.Window(800, 600)
r, g, b, alpha = 0.64, 0.5, 0.6, 1
pyglet.gl.glClearColor(r, g, b, alpha)

game = game.Game(window)





# def level_1_update(dt):
#     # if 5 < seconds < 10:
#     #     return
#
#
#     if len(all_weapons[0].bullets) < 3:
#         ran = random.uniform(-90, 0)
#         all_weapons[0].gun_top_sprite.rotation = ran
#         all_weapons[0].fire()
#
#
#
#     core_label.text = f"Создано ядер: {len(all_weapons[0].bullets)}"


# def level_2_update(dt):
#     print('level2')
#     ran = random.uniform(-90, 0)
#     all_weapons[0].gun_top_sprite.rotation = ran
#     # all_weapons[0].fire()
#     # clock.schedule_once(all_weapons[0].fire, 3)


#
# def level_3_update(dt):
#     print('level3')


# levels = {
#     1: level_1_update,
#     2: level_2_update,
#     3: level_3_update
# }

# def load_level(dt):
#     # level_1_update(dt)
#     if seconds < 10:
#         levels[1](dt)
#     elif seconds < 20:
#         levels[2](dt)


game.start_game()


# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if len(game.all_weapons):

        if button == mouse.LEFT:
            if __name__ == '__main__':
                cannon = game.all_weapons[0]
            cannon.fire()
            game.core_label.text = 'Создано ядер: ' + str(len(cannon.bullets))
            # gun.bullets.
            # main_batch.add(gun.bullets)


@window.event
def on_mouse_motion(x, y, button, modifiers):
    if len(game.all_weapons):
        cannon = game.all_weapons[0]
        degree = cannon.calc_gun_degree(x, y)

        cannon.gun_top_sprite.rotation = -degree
        game.degree_label.text = "Угол наклона пушки: " + str(degree)

        cannon.set_bullet_start_position(degree)


@window.event
def on_draw():
    window.clear()
    game.main_batch.draw()

    # for bullet in gun.bullets:
    #     bullet.draw()

    pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                         ('v2i', (210, 95))
                         )


def update(dt):
    game.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120.)
    pyglet.app.run()
