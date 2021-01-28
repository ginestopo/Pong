#Pong by Gines Diaz
import sys
import os
import pygame as py
import random

py.init()
clock = py.time.Clock()

#window
screen_width = 1000
screen_height = 600
screen = py.display.set_mode((screen_width,screen_height))
py.display.set_caption('Pong by Gines Diaz')

#functions
class ball(py.sprite.Sprite):
    def __init__(self,x,y,x_size,y_size,ball_speed):
        #ball parameters
        self.ball_speed_x = ball_speed
        self.ball_speed_y = ball_speed

        py.sprite.Sprite.__init__(self)

        self.rect = py.Rect(x,y,x_size,y_size)

    def ball_update(self):
            self.rect.x += self.ball_speed_x
            self.rect.y += self.ball_speed_y

            if self.rect.top <= 0 or self.rect.bottom >= screen_height:
                self.ball_speed_y *= -1

            if self.rect.left <= 0 or self.rect.right >= screen_width:
                self.ball_speed_x *= -1

            if self.rect.colliderect(player) or self.rect.colliderect(opponent):
                self.ball_speed_x *= -1

class player(py.sprite.Sprite):
    def __init__(self,x,y,x_size,y_size):
        #ball parameters
        self.player_speed = 0

        py.sprite.Sprite.__init__(self)

        self.rect = py.Rect(x,y,x_size,y_size)

    def player_move(self,vel):
            self.player_speed += vel

    def player_update(self):
            self.rect.y += self.player_speed
            if(self.rect.top <= 0):
                self.rect.y = 0
            if(self.rect.bottom >= screen_height):
                self.rect.y = screen_height - 70

class score(py.sprite.Sprite):
    def __init__(self,x,y):
        py.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0

        for i in range(0,10):
            img = py.image.load(os.path.join('resources','score0'+str(i)+'.png')).convert()
            img = py.transform.scale(img, (80, 80))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)

        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,score):
        for i in range (0,10):
            if(i == score):
                self.image = self.images[i]

#colors
WHITE = (255,255,255)
ALPHA = (0, 0, 0)

#objects
ball = ball(screen_width/2-15,screen_height/2-15,30,30,7)
player = player(10,screen_height/2,10,70)
opponent = py.Rect(screen_width-20,screen_height,10,70)
score_opponent = score(screen_width/2 ,10)
score_player = score(screen_width/2 - 100 ,10)
score_list = py.sprite.Group()
score_list.add(score_opponent)
score_list.add(score_player)
score_number_opponent = 0
score_number_player = 0
screenshake = 0

bg_color = py.Color('grey12')
light_grey = (200,200,200)



while True:

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                player.player_move(7)
            if event.key == py.K_UP:
                player.player_move(-7)
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player.player_move(-7)
            if event.key == py.K_UP:
                player.player_move(7)

    screen.fill(bg_color)

    ball.ball_update()
    player.player_update()

    if(ball.rect.x > screen_width/2):
        opponent.y = ball.rect.y

    #logic
    if ball.rect.x <= 0:
        score_number_opponent += 1
        score_opponent.update(score_number_opponent)
        score_list.draw(screen)
        screenshake = 30


        ball.rect.x = screen_width/2 - 15
        ball.rect.y = screen_height/2 - 15


    if ball.rect.right >= screen_width :
        score_number_player += 1
        score_player.update(score_number_player)
        score_list.draw(screen)
        screenshake = 30

        ball.rect.x = screen_width/2 - 15
        ball.rect.y = screen_height/2 - 15



    if screenshake > 0:
        screenshake -= 1

    render_offset = [0,0]
    if screenshake:
        render_offset[0] = random.randint(0,8) - 4
        render_offset[1] = random.randint(0,8) - 4

    #draw
    py.draw.rect(screen,light_grey,player)
    py.draw.rect(screen,light_grey,opponent)
    py.draw.ellipse(screen,light_grey,ball)
    py.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    py.draw.circle(screen,light_grey,(int(screen_width/2),int(screen_height/2)),4)
    score_list.draw(screen)

    #update the window
    screen.blit(screen, render_offset)
    py.display.flip()
    clock.tick(60)
