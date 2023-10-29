import pygame

pygame.init() # pygame 모듈 사용 시작

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

WHITE = (255,255,255) # R, G, B 색상

ball_size = 20 # 반지름
ball_pos = [ball_size, screen_height//2] # 공 위치
ball_speed = [0,0] # 공속도, 각각 x축 y축 속도

while 1:
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size) # 어디에 그릴지, 색깔, 공 중심 위치, 공 크기
    pygame.display.flip() # 화면 전환하기
