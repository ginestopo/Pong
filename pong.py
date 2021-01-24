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

#functions
def ball_animation():
        global ball_speed_x,ball_speed_y

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1

        if ball.left <= 0 or ball.right >= screen_width:
            ball_speed_x *= -1

        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1


#colors
WHITE = (255,255,255)

#objects
ball = py.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = py.Rect(10,screen_height/2,10,70)
opponent = py.Rect(screen_width-20,screen_height/2,10,70)

bg_color = py.Color('grey12')
light_grey = (200,200,200)

#player
player_speed = 0
#ball parameters
ball_speed_x = 7
ball_speed_y = 7

while True:

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                player_speed += 7
            if event.key == py.K_UP:
                player_speed -= 7
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player_speed -= 7
            if event.key == py.K_UP:
                player_speed += 7

    screen.fill(bg_color)

    ball_animation()
    player.y += player_speed

    if(player.top <= 0):
        player.y = 0
    if(player.bottom >= screen_height):
        player.y = screen_height - 70


    py.draw.rect(screen,light_grey,player)
    py.draw.rect(screen,light_grey,opponent)
    py.draw.ellipse(screen,light_grey,ball)
    py.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))


    #update the window
    py.display.flip()
    clock.tick(60)
