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

# Game loop
running = True
clock = pygame.time.Clock()

pygame.mixer.init()
shootsound = pygame.mixer.Sound("shoot.wav")

ship = pygame.image.load("Man.png").convert_alpha()
shiprect = ship.get_rect(center=(400,300))

while running:
    screen.fill(BLACK)
    screen.blit(ship,shiprect)
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
