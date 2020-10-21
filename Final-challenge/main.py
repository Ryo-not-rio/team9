import pygame as py

py.init()

display = py.display.set_mode((800, 800))

game_exit = False

while not game_exit:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_exit = True

    ### Drawing ###
    display.fill(py.Color('white'))
    py.display.update()

py.quit()
exit()