import pygame
from pygame.locals import *
import random

def on_grid_random():
    '''Essa função retorna uma posição aleatória 
    que seja válida na tela, considerando um grid 
    formado por quadrados de 10px por 10px'''

    x = random.randint(0, 490)
    y = random.randint(0, 490)
    return (x//10 * 10, y//10 * 10)

def collision(c1:tuple, c2:tuple):
    '''Essa função é responsável por verificar colisões'''
    return c1 == c2

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Inciando e setando a tela
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game - By Nathan Oliveira')

# Configurando a cobra
snake = [(250, 250), (250, 260), (250, 270)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# Direção inicial
my_direction = LEFT

# Configurando a fruta
berry = pygame.Surface((10, 10))
berry.fill((227, 30, 30))
berry_pos = on_grid_random()

clock = pygame.time.Clock()
while True:
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Movimentação
    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    # Colisão com a fruta e crescimento
    if collision(snake[0], berry_pos):
        berry_pos = on_grid_random()
        snake.append((0,0))

    # Movimentação do corpo
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Movimentação da cabeça
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # Limpando a tela e inserindo a nova fruta
    screen.fill((0, 0, 0))
    screen.blit(berry, berry_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
