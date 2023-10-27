import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60
clock = pygame.time.Clock()

ball_size = 20
ball_pos = [screen_width//2, screen_height//2]
ball_speed = [0,0]
move_speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if ball_pos[0]>0:
            ball_pos[0] -= move_speed
    if keys[pygame.K_RIGHT]:
        if ball_pos[0] < screen_width:
            ball_pos[0] += move_speed
        print(ball_pos)
    
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size)
    pygame.display.flip()
    clock.tick(FPS)
