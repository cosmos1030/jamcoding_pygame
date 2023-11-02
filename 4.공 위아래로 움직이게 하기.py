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
ball_speed = [0,2] # 각각 x축, y 축 초기 속도
move_speed = 4

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if ball_pos[0]>0: # 화면 왼쪽 끝보다 오른쪽에 있을때
            ball_pos[0] -= move_speed
    if keys[pygame.K_RIGHT]:
        if ball_pos[0] < screen_width:
            ball_pos[0] += move_speed
    ball_pos[1] += ball_speed[1] # 아래로 이동

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size)
    pygame.display.flip()

