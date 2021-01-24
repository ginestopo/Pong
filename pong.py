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

#colors
WHITE = (255,255,255)

#objects
ball = py.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = py.Rect(10,screen_height/2,10,70)
opponent = py.Rect(screen_width-20,screen_height/2,10,70)

bg_color = py.Color('grey12')
light_grey = (200,200,200)

#ball parameters
ball_speed_x = 7
ball_speed_y = 7

while True:

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    screen.fill(bg_color)

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    py.draw.rect(screen,light_grey,player)
    py.draw.rect(screen,light_grey,opponent)
    py.draw.ellipse(screen,light_grey,ball)
    py.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))


    #update the window
    py.display.flip()
    clock.tick(60)
