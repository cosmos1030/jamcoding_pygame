import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 120
clock = pygame.time.Clock()

ball_size = 20
ball_pos = [screen_width//2, screen_height//2]
ball_speed = [0,0] # 각각 x축, y 축 초기 속도
ball_initial_speed_y = -8
ball_acc = 0.1
move_speed = 4

running = True
while running:
    clock.tick(FPS)
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
    ball_speed[1] += ball_acc
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] >= screen_height:
        ball_speed[1] = ball_initial_speed_y

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size)
    pygame.display.flip()

