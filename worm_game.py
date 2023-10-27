import pygame
import random

# 초기화
pygame.init()

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 화면 크기
WIDTH, HEIGHT = 640, 480

# 블록 크기
BLOCK_SIZE = 20

# 화면 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("지렁이 게임")

class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)

    def move(self):
        head = self.body[0]
        new_head = ((head[0] + self.direction[0]) % (WIDTH // BLOCK_SIZE),
                    (head[1] + self.direction[1]) % (HEIGHT // BLOCK_SIZE))
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def collision_with_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

class Apple:
    def __init__(self, snake_body):
        while True:
            self.position = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1), random.randint(0, (HEIGHT // BLOCK_SIZE) - 1))
            if self.position not in snake_body:
                break

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0] * BLOCK_SIZE, self.position[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

snake = Snake()
apple = Apple(snake.body)  # 처음에도 지렁이의 몸 정보를 전달합니다.
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    snake.move()

    if snake.body[0] == apple.position:
        snake.grow()
        apple = Apple(snake.body)  # 지렁이의 몸 정보를 전달하여 새로운 사과 객체를 생성합니다.

    if snake.collision_with_self():
        running = False

    snake.draw(screen)
    apple.draw(screen)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
