import pygame
import random
import os


# Computers Attack!
# TODO
# draw computers: ZX81, C64, etc. They are the robots and shoot disks and CD-ROMs
# create cute creatures to rescue - GitHub furry, Linux Penguin, etc
# Keep LED graphics for special effects
# full game
# read joystciks - simple ..? see copilot
# upload to GitHub

# Initialize Pygame
pygame.init()

# mark sure sprites are drawn rectangular (not isometric diagonal) for easy collision rectangles
charZX80 = [(0,0,"#DDDDDD"), (0,1,"#DDDDDD"), (0,2,"#DDDDDD"), (0,3,"#DDDDDD"), (0,4,"#DDDDDD"), (0,5,"#DDDDDD"), (0,6,"#DDDDDD"), (0,7,"#DDDDDD"), (0,8,"#DDDDDD"), (0,9,"#DDDDDD"), (0,10,"#DDDDDD"), (0,11,"#DDDDDD"), (0,12,"#DDDDDD"), (0,13,"#DDDDDD"), (1,0,"#DDDDDD"), (1,1,"#DDDDDD"), (1,2,"#DDDDDD"), (1,3,"#DDDDDD"), (1,4,"#DDDDDD"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (1,8,"#FFFF00"), (1,9,"#FFFF00"), (1,10,"#0000FF"), (1,11,"#4C3A23"), (1,12,"#0000FF"), (1,13,"#DDDDDD"), (2,0,"#AAAAAA"), (2,1,"#AAAAAA"), (2,2,"#AAAAAA"), (2,3,"#AAAAAA"), (2,4,"#AAAAAA"), (2,5,"#FFFF00"), (2,6,"#DDDDDD"), (2,7,"#FFFF00"), (2,8,"#DDDDDD"), (2,9,"#FFFF00"), (2,10,"#4C3A23"), (2,11,"#4C3A23"), (2,12,"#4C3A23"), (2,13,"#DDDDDD"), (3,0,"#AAAAAA"), (3,1,"#4C3A23"), (3,2,"#AAAAAA"), (3,3,"#4C3A23"), (3,4,"#AAAAAA"), (3,5,"#FFFF00"), (3,6,"#FFFF00"), (3,7,"#FFFF00"), (3,8,"#FFFF00"), (3,9,"#FFFF00"), (3,10,"#0000FF"), (3,11,"#4C3A23"), (3,12,"#0000FF"), (3,13,"#DDDDDD"), (4,0,"#AAAAAA"), (4,1,"#4C3A23"), (4,2,"#AAAAAA"), (4,3,"#4C3A23"), (4,4,"#AAAAAA"), (4,5,"#DDDDDD"), (4,6,"#DDDDDD"), (4,7,"#DDDDDD"), (4,8,"#DDDDDD"), (4,9,"#DDDDDD"), (4,10,"#4C3A23"), (4,11,"#4C3A23"), (4,12,"#4C3A23"), (4,13,"#DDDDDD"), (5,0,"#AAAAAA"), (5,1,"#4C3A23"), (5,2,"#AAAAAA"), (5,3,"#4C3A23"), (5,4,"#AAAAAA"), (5,5,"#FFFF00"), (5,6,"#FFFF00"), (5,7,"#FFFF00"), (5,8,"#FFFF00"), (5,9,"#FFFF00"), (5,10,"#0000FF"), (5,11,"#4C3A23"), (5,12,"#0000FF"), (5,13,"#DDDDDD"), (6,0,"#AAAAAA"), (6,1,"#4C3A23"), (6,2,"#AAAAAA"), (6,3,"#4C3A23"), (6,4,"#AAAAAA"), (6,5,"#FFFF00"), (6,6,"#DDDDDD"), (6,7,"#DDDDDD"), (6,8,"#DDDDDD"), (6,9,"#FFFF00"), (6,10,"#4C3A23"), (6,11,"#4C3A23"), (6,12,"#4C3A23"), (6,13,"#DDDDDD"), (7,0,"#AAAAAA"), (7,1,"#AAAAAA"), (7,2,"#AAAAAA"), (7,3,"#AAAAAA"), (7,4,"#AAAAAA"), (7,5,"#FFFF00"), (7,6,"#FFFF00"), (7,7,"#FFFF00"), (7,8,"#FFFF00"), (7,9,"#FFFF00"), (7,10,"#0000FF"), (7,11,"#4C3A23"), (7,12,"#0000FF"), (7,13,"#DDDDDD"), (8,0,"#DDDDDD"), (8,1,"#DDDDDD"), (8,2,"#DDDDDD"), (8,3,"#DDDDDD"), (8,4,"#DDDDDD"), (8,5,"#DDDDDD"), (8,6,"#DDDDDD"), (8,7,"#DDDDDD"), (8,8,"#DDDDDD"), (8,9,"#DDDDDD"), (8,10,"#4C3A23"), (8,11,"#4C3A23"), (8,12,"#4C3A23"), (8,13,"#DDDDDD"), (9,0,"#DDDDDD"), (9,1,"#DDDDDD"), (9,2,"#DDDDDD"), (9,3,"#DDDDDD"), (9,4,"#DDDDDD"), (9,5,"#DDDDDD"), (9,6,"#DDDDDD"), (9,7,"#DDDDDD"), (9,8,"#DDDDDD"), (9,9,"#DDDDDD"), (9,10,"#DDDDDD"), (9,11,"#DDDDDD"), (9,12,"#DDDDDD"), (9,13,"#DDDDDD")]

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Computers Attack!")

current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

STEPD = 3 # speed of ship

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# Ball
BALL_RADIUS = 8
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx, ball_dy = 4, -4

# Bricks
BRICK_ROWS, BRICK_COLS = 5, 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
bricks = [pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
          for row in range(BRICK_ROWS) for col in range(BRICK_COLS)]

# Font
font = pygame.font.SysFont("Arial", 24)


def createCharColourSolid(screen,x,y,colourpoints, LEDpoints):
  for p in colourpoints:
    x1 = x+p[0]*psize
    y1 = y+p[1]*psize
    srect = pygame.Rect(x1,y1, psize, psize)
    pygame.draw.rect(screen, p[2], srect)

class pygameLEDobj:
    def __init__(self, screen,x=0,y=0,dx=0,dy=0, CharPoints = [], pixelsize = 2, typestring = "unknown"):
         global psize
         self.alive = True
         self.x = x
         self.y = y
         self.dx = dx
         self.dy = dy
         self.screen = screen
         self.typestring = typestring
         self.LEDPoints = []
         self.OriginalCharPoints = CharPoints
         self.CharPoints = CharPoints.copy()
         self.PointsType = 0
         self.collisionrect = (0,0,0,0)  # top left to bottom right
         self.CollisionPoints = [(0,0,0)]
         self.RotatedCollisionPoints = [(0,0,0)]
         self.collisionimage = 0
         self.collisionlinesimage = 0
         self.collisionrectshow = False
         self.collisionlinesshow = False
         self.pixelsize = pixelsize
         psize = self.pixelsize
         createCharColourSolid(screen,x,y,CharPoints,self.LEDPoints)
    def resetposition(self,x,y):
        self.x, self.y = x,y
        self.dx, self.dy = 0,0
        self.draw()
    def draw(self):
        global psize
        psize = self.pixelsize
        createCharColourSolid(self.screen,self.x,self.y,self.CharPoints,self.LEDPoints)
    def move(self): 
         self.x = self.x + self.dx
         self.y = self.y + self.dy


# Game loop
running = True
clock = pygame.time.Clock()

pygame.mixer.init()
shootsound = pygame.mixer.Sound("shoot.wav")

ship = pygame.image.load("Man.png").convert_alpha()
shiprect = ship.get_rect(center=(400,300))

myship = pygameLEDobj(screen,200,300,dx = 0,dy = 0,CharPoints=charZX80, pixelsize = 2,typestring = "human")



while running:
    screen.fill(BLACK)
    screen.blit(ship,shiprect)
    myship.draw()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
    if ball.bottom >= HEIGHT:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dy *= -1

    # Paddle collision
    if ball.colliderect(paddle):
        ball_dy *= -1

    # Brick collision
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_dy *= -1
        shootsound.play()

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw score
    score_text = font.render(f"Bricks left: {len(bricks)}", True, GREEN)
    screen.blit(score_text, (10, HEIGHT - 30))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        shiprect.y -= STEPD
    if keys[pygame.K_s]:
        shiprect.y += STEPD
    if keys[pygame.K_a]:
        shiprect.x -= STEPD
    if keys[pygame.K_d]:
        shiprect.x += STEPD

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
