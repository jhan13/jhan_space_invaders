WIDTH = 1000
HEIGHT = 800
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 15
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (1,1,100), "bouncey"),
                 (250, HEIGHT - 350, 100, 20, (200,100,50), "disappearing"),
                 (230, HEIGHT - 250, 100, 20, (200,100,50), "disappearing"),
                 (450, 300, 100, 20, (200,200,200), "normal"),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (WIDTH / 2 - 350, HEIGHT * 2 / 4, 100, 20, (1,1,100), "bouncey"),
                 (175, 100, 50, 20, (200,200,200), "normal")]
                 