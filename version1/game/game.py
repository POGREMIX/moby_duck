import pyglet
from pyglet import clock
from game import gun, levels
from game import animals
from pyglet.window import key

# from game.levels import update_level


class Game:
    def __init__(self, window):
        self.window = window

        self.main_batch = pyglet.graphics.Batch()
        self.gun_group = pyglet.graphics.OrderedGroup(1)
        self.bullet_group = pyglet.graphics.OrderedGroup(0)

        self.lives = 3
        self.step = 16
        self.seconds = 0
        self.highest_score = 0

        self.all_animals = []
        self.all_weapons = []
        self.all_bullets = []
        self.schedulers = []
        self.labels = []

        self.core_label = pyglet.text.Label()
        self.degree_label = pyglet.text.Label()
        self.time_label = pyglet.text.Label()
        self.live_label = pyglet.text.Label()
        self.score_label = pyglet.text.Label()
        self.game_over_label = pyglet.text.Label()

        self.labels.append(self.core_label)
        self.labels.append(self.degree_label)
        self.labels.append(self.live_label)
        self.labels.append(self.time_label)
        self.labels.append(self.score_label)
        self.labels.append(self.game_over_label)

        for i in range(0, len(self.labels)):
            self.labels[i].font_name = font_name = 'Times New Roman'
            self.labels[i].font_size = 14
            self.labels[i].x = 0
            self.labels[i].y = window.height - self.step * i
            self.labels[i].anchor_x = 'left'
            self.labels[i].anchor_y = 'top'
            self.labels[i].batch = self.main_batch

        self.game_over_label.y = 300

        self.key_handler = key.KeyStateHandler()
        window.push_handlers(self.key_handler)

    # def init(self):

    def load_level(self, level):
        # print('load_level')
        # update_level(dt, self)
        for cannon in level.cannons:
            cannon.batch = self.main_batch
            cannon.group = self.gun_group
            cannon.bullet_group = self.bullet_group


    def start_game(self):
        print('begin')

        # self.load_level(levels.level1)

        self.live_label.text = f"Кол-во жизней: {self.lives}"
        self.score_label.text = f"Лучший счет: {self.highest_score}"

        duck = animals.Duck(batch=self.main_batch)
        duck.set_start_position(self.window.width - duck.x, self.window.height - duck.y)
        self.window.push_handlers(duck.key_handler)
        self.all_animals.append(duck)

        cannon = gun.Cannon(batch=self.main_batch, group=self.gun_group, bullet_group=self.bullet_group)
        self.all_weapons.append(cannon)

        self.core_label.text = 'Создано ядер: ' + str(len(cannon.bullets))
        self.degree_label.text = "Угол наклона пушки: " + str(0)
        self.time_label.text = f"{self.seconds}"

        clock.schedule_interval(self.update_time, 1 / 10)
        self.schedulers.append(self.update_time)

        # clock.schedule_interval(self.load_level, 1)
        # self.schedulers.append(self.load_level)
        # print(self.all_weapons)
        # load_level(self.all_weapons)
        # self.schedulers.append(levels.schedulers)
        # print(self.schedulers)

    def reset_level(self):
        self.clear_all()
        self.start_game()

    def clear_all(self):
        for animal in self.all_animals:
            animal.delete()
            self.all_animals.remove(animal)
            # animal.batch = None

        for weapon in self.all_weapons:

            for bullet in weapon.bullets:
                bullet.delete()
            weapon.bullets.clear()

        self.all_weapons.clear()

        for method in self.schedulers:
            clock.unschedule(method)

        self.seconds = 0

    def update(self, dt):
        self.update_space_handler()
        # for obj in game_objects:
        #     obj.update(dt)

        # gun.update()
        # update_space_handler()
        #
        for weapon in self.all_weapons:
            # print(weapon)
            for bullet in weapon.bullets:
                bullet.update(dt)
                bullet.collides_with_walls()
                if self.all_animals:
                    bullet.collides_with_animal(self.all_animals[0])

        are_all_dead = self.check_on_dead()

        if are_all_dead:
            self.lives -= 1
            cur_score = float(self.time_label.text)

            if self.highest_score < cur_score:
                self.highest_score = cur_score
            self.score_label.text = str(self.highest_score)
            self.clear_all()

            # highest_score =
            if self.lives > 0:
                self.reset_level()
            else:
                # for label in labels:
                #     label.delete()
                self.core_label.text = f"{0}"
                self.degree_label.text = f"{0}"
                self.time_label.text = f"{0}"
                self.live_label.text = f"{self.lives}"

                # for scheduler in schedulers:
                #     clock.unschedule(scheduler)
                self.game_over_label.y = 300
                self.game_over_label.text = "GAME OVER"

        else:
            for an in self.all_animals:
                an.update(dt)

    def update_time(self, dt):

        self.seconds += dt
        rounded = round(self.seconds, 2)
        self.time_label.text = f"{rounded}"

    def check_on_dead(self):
        for animal in self.all_animals:
            if not animal.is_dead:
                return False
        if len(self.all_animals) == 0:
            return False
        return True

    def update_space_handler(self):
        if self.key_handler[key.SPACE]:
            self.lives = 3
            self.game_over_label.y = 1000
            self.clear_all()
            self.highest_score = 0
            self.reset_level()
