import pygame
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# 스크린 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# 스크린 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("공 튕기기 게임")

# 변수 설정
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_speed = [random.choice([-3, 3]), random.choice([-3, 3])]
ball_radius = 15

yellow_ball_pos = [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4]
yellow_ball_speed = 5
yellow_ball_radius = 20

def balls_collided(pos1, r1, pos2, r2):
    distance = ((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)**0.5
    return distance < (r1 + r2)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        yellow_ball_pos[0] -= yellow_ball_speed
    if keys[pygame.K_RIGHT]:
        yellow_ball_pos[0] += yellow_ball_speed
    if keys[pygame.K_UP]:
        yellow_ball_pos[1] -= yellow_ball_speed
    if keys[pygame.K_DOWN]:
        yellow_ball_pos[1] += yellow_ball_speed

    # 볼의 위치 업데이트
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 볼이 경계에 닿으면 튕기기
    if ball_pos[0] <= ball_radius or ball_pos[0] >= SCREEN_WIDTH - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius or ball_pos[1] >= SCREEN_HEIGHT - ball_radius:
        ball_speed[1] = -ball_speed[1]

    # 스크린 클리어
    screen.fill(WHITE)

    # 볼 그리기
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)
    pygame.draw.circle(screen, YELLOW, yellow_ball_pos, yellow_ball_radius)

    # 노란공과 빨간공이 부딪혔는지 체크
    if balls_collided(ball_pos, ball_radius, yellow_ball_pos, yellow_ball_radius):
        running = False

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 제한
    pygame.time.Clock().tick(60)

pygame.quit()
