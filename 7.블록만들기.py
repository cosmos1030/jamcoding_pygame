import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)  # 블록 색상

# 게임 설정
FPS = 120
clock = pygame.time.Clock()

# 공 설정
ball_size = 10
ball_pos = [30, screen_height // 2+100]
ball_speed = [0, 0]  # 초기 속도
ball_initial_speed_y = -5  # 튀어오르는 속도
ball_acc = 0.1  # 중력가속도
move_speed = 4

# 별 위치
star_pos = [screen_width - 30, screen_height // 2]

# 블록 설정
class Block:
    def __init__(self, pos):
        self.block_size = [30,30]
        self.block_pos = pos
    def get_size(self):
        return self.block_size
    def get_pos(self):
        return self.block_pos
block_list = []
for i in range(10,20):
    block = Block([i*30, screen_height-(i-9)*30])
    block_list.append(block)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if ball_pos[0] > 0:
            ball_pos[0] -= move_speed
    if keys[pygame.K_RIGHT]:
        if ball_pos[0] < screen_width:
            ball_pos[0] += move_speed

    # 공의 중력 및 움직임
    ball_speed[1] += ball_acc
    ball_pos[1] += ball_speed[1]

    # 바닥에 닿았을 때 튕겨나오는 로직
    if ball_pos[1] >= screen_height - ball_size:
        ball_speed[1] = ball_initial_speed_y

    # 블록에 닿았을 때 튕겨나오는 로직
    for block in block_list:
        block_pos = block.get_pos()
        block_size = block.get_size()
        if (block_pos[0] < ball_pos[0] < block_pos[0] + block_size[0]) and \
        (block_pos[1] < ball_pos[1] + ball_size < block_pos[1] + block_size[1]):
            ball_speed[1] = ball_initial_speed_y
    
    # 별 먹으면 게임 종료
    if (star_pos[0]-ball_pos[0])**2 + (star_pos[1]-ball_pos[1])**2 < (ball_size*2)**2:
        running = False

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_size)
    pygame.draw.circle(screen, YELLOW, star_pos, ball_size)
    for block in block_list:
        block_pos = block.get_pos()
        block_size = block.get_size()
        pygame.draw.rect(screen, GREEN, (*block_pos, *block_size))  # 블록 그리기

    pygame.display.flip()

pygame.quit()
