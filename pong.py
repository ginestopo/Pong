#Pong by Gines Diaz
import sys
import pygame as py

py.init()
clock = py.time.Clock()

#window
screen_width = 1000
screen_height = 600
screen = py.display.set_mode((screen_width,screen_height))
py.display.set_caption('Game')

while True:

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()


    #update the window
    py.display.flip()
    clock.tick(60)
