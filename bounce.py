import pygame
import sys

# pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bounce Ball')

# 공 변수 설정
ball_radius = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 5, 5

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 공 위치 업데이트
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽에 부딪힐 때 반사
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    # 프레임 설정
    pygame.time.Clock().tick(60)
