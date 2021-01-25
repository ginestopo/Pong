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
class ball(py.sprite.Sprite):
    def __init__(self,x,y,x_size,y_size):
        #ball parameters
        self.ball_speed_x = 7
        self.ball_speed_y = 7

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
            pos = py.mouse.get_pos()
            self.rect.center = pos
            '''self.rect.y += self.player_speed
            if(self.rect.top <= 0):
                self.rect.y = 0
            if(self.rect.bottom >= screen_height):
                self.rect.y = screen_height - 70'''


#colors
WHITE = (255,255,255)

#objects
ball = ball(screen_width/2-15,screen_height/2-15,30,30)
player = player(10,screen_height/2,10,70)
opponent = py.Rect(screen_width-20,screen_height/2,10,70)

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

    #draw
    py.draw.rect(screen,light_grey,player)
    py.draw.rect(screen,light_grey,opponent)
    py.draw.ellipse(screen,light_grey,ball)
    py.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))


    #update the window
    py.display.flip()
    clock.tick(60)
