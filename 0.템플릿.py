import pygame

pygame.init()

screen_width = # 화면 넓이
screen_height = # 화면 높이
screen = pygame.display.set_mode((screen_width,screen_height))

FPS = # frame per second
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(RGB 색상)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size) # 화면, 색상, 중심 위치, 공 크기
    pygame.display.flip() # 화면 전환

