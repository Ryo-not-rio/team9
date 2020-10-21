import pygame as py

import beat

py.init()

display = py.display.set_mode((800, 800))
clock = py.time.Clock()

game_exit = False

beats = [1.9, 2.01]
beat_objs = [beat.Beat(1)]
speed = 10

while not game_exit:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_exit = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                pass

    for beat in beat_objs:
        beat.pos[1] += speed


    ### Drawing ###
    display.fill(py.Color('white'))
    for beat in beat_objs:
        beat.draw(display)
    # py.draw.rect(display, py.Color('blue'), (0, 0, 100 ,100))

    clock.tick(50)
    py.display.update()

py.quit()
exit()