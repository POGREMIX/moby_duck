import random

from game import level, gun
from pyglet import clock

# schedulers = []
weapons = []
bullets = []

# def load_level(all_weapons):
    # global weapons

    # clock.schedule_interval(update_level, 1)
    # weapons = all_weapons
    # schedulers.append(update_level)

    # print('load_level')


# def update_level(dt, game):
#     print('update_level')
#     seconds = game.seconds
#     weapons = game.all_weapons
#     core_label = game.core_label
#     main_batch = game.main_batch
#     gun_group = game.gun_group
#     bullet_group = game.bullet_group
#
#
#     if seconds < 5:
#         # len(all_weapons[0].bullets) < 3:
#         ran = random.uniform(-90, 0)
#         weapons[0].gun_top_sprite.rotation = ran
#         weapons[0].fire()
#         core_label.text = f"Создано ядер: {len(weapons[0].bullets)}"
#
#
#     elif seconds >= 5:
#         cannon = gun.Cannon(batch=main_batch, group=gun_group, bullet_group=bullet_group, y=200, x=200)
#         # weapons.append(cannon)





    # core_label.text = f"Создано ядер: {len(weapons[0].bullets)}"


level1 = level.Level()
