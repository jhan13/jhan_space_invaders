# File created by: Joon Han 
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 
'''
I was considering adding an ability to the player that allows the player to destroy enemies causing the enemies to dissapear
the player could shoot object and hit the enemies that are coming towards the main player
the main player could also have 3 lives and everytime the enemies reach the player and touch him, the player could blink and lose a heart


'''
# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.backgroundImage = pg.image.load("./image/background.png").convert()
        self.backgroundImage = pg.transform.smoothscale(self.backgroundImage, self.screen.get_size())
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)

    def new(self):
        # starting a new game
        self.score = 0

        # platform
        self.platforms = pg.sprite.Group()

        # platform
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        
        self.platforms.add(self.plat1)      

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.platforms.add(p)

        # player
        self.player = Player(self)
        self.playerSprit = pg.sprite.Group()
        self.playerSprit.add(self.player)

        # mobs
        self.enemies = pg.sprite.Group()

        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.enemies.add(m)

        # blocks
        self.blocks = pg.sprite.Group()
        
    def run(self):
        self.running = True
        self.playing = True

        while self.running:
            self.clock.tick(FPS)
            self.events()

            if self.playing == True:
                self.update()
                self.draw()
            else:
                self.draw_text("Game over", 50, WHITE, WIDTH/2, HEIGHT/2)
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        self.enemies.update()
        self.playerSprit.update()
        self.blocks.update()
        self.platforms.update()
        
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.backgroundImage, (0, 0))

        self.playerSprit.draw(self.screen)
        self.blocks.draw(self.screen)
        self.enemies.draw(self.screen)
        self.platforms.draw(self.screen)

        # is this a method or a function?
        pg.display.flip()
        
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
g.new()

# run 
g.run()

pg.quit()