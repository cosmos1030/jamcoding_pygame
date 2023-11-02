import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

WHITE = (255,255,255)
BLACK = (0,0,0) # 배경색

FPS = 120 # Frame per Second. 1초에 전환되는 화면 개수
clock = pygame.time.Clock()

ball_size = 20 # 공 반지름
ball_pos = [screen_width//2, screen_height//2]
ball_speed = [0,0] # 처음 공 속도. 각각 x축 ,y축 속도
move_speed = 4 # 화살표를 눌렀을 때 이동하는 속도

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get(): # 클릭, 키보드 누르기 등 이벤트 감지
        if event.type == pygame.QUIT: # 종료 버튼을 눌렀을 때
            running = False
    keys = pygame.key.get_pressed() # 키보드가 눌렸을 때
    if keys[pygame.K_LEFT]: # 왼쪽 화살표가 눌렸을때
        ball_pos[0] -= move_speed
    if keys[pygame.K_RIGHT]:# 오른쪽 화살표가 눌렸을 때
        ball_pos[0] += move_speed
        # print(ball_pos)
    
    ball_pos[0] += ball_speed[0] # 새로운 공의 x축 위치
    ball_pos[1] += ball_speed[1] # 새로운 공의 y축 위치

    screen.fill(BLACK) # 화면 색 검은색
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size) # 공 새로 그리기
    pygame.display.flip()

