import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

# player class

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.SPEED = 5
        self.SIZE = 20

    def input(self):
        keystate = pg.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        # if keystate[pg.K_s]:
        #     self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # if keystate[pg.K_p]:
        #     if PAUSED == False:
        #         PAUSED = True
        #         print(PAUSED)
        #     else:
        #         PAUSED = False
        #         print(PAUSED)
        if keystate[pg.K_f]:
            b = Block(self.game, self.pos.x, self.pos.y - self.rect.height/2)
            self.game.blocks.add(b)
    # ...
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        # if hits:
        self.vel.y = -PLAYER_JUMP
    
    def inbounds(self):
        if self.rect.centerx > WIDTH - self.rect.width/2:
            self.pos.x = WIDTH - self.rect.width/2
            self.vel.x = -5
            print("i am off the right side of the screen...")
        if self.rect.centerx < self.rect.width/2:
            self.pos.x = self.rect.width/2
            self.vel.x = 5
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            print("i am off the top of the screen...")
            
    def mob_collide(self):
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                self.game.score += 1
                print(SCORE)
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        #checks if the player is off screen
        self.inbounds()

        # if self.rect.centerx > WIDTH - self.rect.width/2:
        #     print("Bump")
        #     self.vel.x= -5
        # if self.rect.centerx < self.rect.width/2: 
        #     print("Bump")
        #     self.vel.x = 5 
        # if self.rect.y < 0:
        #     print("Bump")
        #     self.vel.y = 5
        # #if self.rect.y < 

# Define the block that the player shoots
class Block(Sprite):
    def __init__(self, game, x, y):
        Sprite.__init__(self)
        self.game = game
        self.width = 15
        self.height = 15
        self.image = pg.Surface((self.width,self.height))
        self.color = (255, 0, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(x, y)
        self.vel = vec(0, -5) # shooting up

    def inbounds(self):
        # check if the block is out of screen. If so, remove it. 
        out = False 

        if self.rect.x > WIDTH:
           out = True
        elif self.rect.x < 0:
            out = True
        elif self.rect.y < 0:
            out = True
        elif self.rect.y > HEIGHT:
            out = True

        if out:
             self.game.blocks.remove(self)

    def mob_collide(self):
            # Check if this block hits any enemy. If so, delete the enemy by passing True to spritecollide's dokill argument. 
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)

            # If this block hits any enemy, delete this block itself. 
            if hits:
                self.game.blocks.remove(self) 

    def update(self):
        self.mob_collide()
        self.inbounds()
        self.pos = self.pos + self.vel
        self.rect.center = self.pos

class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

# create a new platform class...
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant