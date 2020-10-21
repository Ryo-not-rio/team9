import pygame as py

py.init()

display = py.display.set_mode((800, 800))

game_exit = False

# beats = [1.9, 2.01, ...]

while not game_exit:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_exit = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                pass

    ### Drawing ###
    display.fill(py.Color('white'))
    py.draw.rect(display, py.Color('blue'), (0, 0, 100 ,100))
    py.display.update()

py.quit()
exit()