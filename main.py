import pygame
from pygame.locals import *
import random
from typing import Tuple, List

SCREEN_SIZE = 500
OBJECTS_SIZE = 10

def on_grid_random() -> Tuple:
    '''Essa função retorna uma posição aleatória 
    que seja válida na tela, considerando um grid 
    formado por n unidades de tamanho = OBJECTS_SIZE'''

    limit_position_x = SCREEN_SIZE - OBJECTS_SIZE
    limit_position_y = SCREEN_SIZE - OBJECTS_SIZE
    random_x = random.randint(0, limit_position_x)
    random_y = random.randint(0, limit_position_y)

    valid_x = random_x // 10 * 10
    valid_y = random_y // 10 * 10

    return (valid_x, valid_y)

def screen_collision(head_pos: Tuple):
    '''Essa função é responsável por verificar 
    colisões com as "paredes" da tela'''
    head_pos_x = head_pos[0]
    head_pos_y = head_pos[1]
    if head_pos_x > SCREEN_SIZE or head_pos_y > SCREEN_SIZE:
        return True
    elif head_pos_x < 0 or head_pos_y < 0:
        return True
    
def self_collision(snake: List[Tuple]):
    '''Essa função é responsável por verificar 
    colisões com as "paredes" da tela'''
    snake_head = snake[0]
    snake_body = snake[1:]
    for section in snake_body:
        if section == snake_head:
            return True

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Inciando e setando a tela
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Snake Game - By Nathan Oliveira')

# Configurando a cobra
snake = [(250, 250), (250, 260), (250, 270)]
snake_shape = pygame.Surface((OBJECTS_SIZE, OBJECTS_SIZE))
snake_shape.fill((255, 255, 255))

# Direção inicial
my_direction = LEFT

# Configurando a fruta
berry = pygame.Surface((OBJECTS_SIZE, OBJECTS_SIZE))
berry.fill((227, 30, 30))
berry_pos = on_grid_random()

clock = pygame.time.Clock()
while True:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Movimentação
    if event.type == KEYDOWN:
        if event.key == K_UP and my_direction != DOWN:
            my_direction = UP
        elif event.key == K_DOWN and my_direction != UP:
            my_direction = DOWN
        elif event.key == K_LEFT and my_direction != RIGHT:
            my_direction = LEFT
        elif event.key == K_RIGHT and my_direction != LEFT:
            my_direction = RIGHT

    # Colisão com a fruta e crescimento
    if snake[0] == berry_pos:
        berry_pos = on_grid_random()
        snake.append((0,0))

    # Movimentação do corpo
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Movimentação da cabeça
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - OBJECTS_SIZE)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + OBJECTS_SIZE)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + OBJECTS_SIZE, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - OBJECTS_SIZE, snake[0][1])

    if screen_collision(snake[0]) or self_collision(snake):
        pygame.quit()

    # Limpando a tela e inserindo a nova fruta
    screen.fill((0, 0, 0))
    screen.blit(berry, berry_pos)

    for pos in snake:
        screen.blit(snake_shape, pos)

    pygame.display.update()
