import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

WHITE = (255,255,255)

ball_size = 20
ball_pos = [screen_width//2, screen_height//2]
ball_speed = [0,0]

while 1:
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size)
    pygame.display.flip()
