import pyglet


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()


duck_image = pyglet.resource.image("duck.png")
gun_bottom_image = pyglet.resource.image("gun_bottom2.png")

gun_top_image = pyglet.resource.image("gun_top.png")
gun_top_image.anchor_x = gun_top_image.width - 190
wick = 14
gun_top_image.anchor_y = gun_top_image.height / 2 - wick

bullet_image = pyglet.resource.image("bullet.png")

gun_shot = pyglet.resource.media("shot.wav", streaming=False)
gun_rikoshet = pyglet.resource.media("rikoshet.wav", streaming=False)


center_image(duck_image)
center_image(bullet_image)
# center_image(gun_top_image)
center_image(gun_bottom_image)
