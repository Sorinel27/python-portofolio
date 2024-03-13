
"""
    This is the main file of the game. It contains the game loop and the main logic of the game.
    Use A and D to move the table left and right.
    Press R to randomize the ball position.
"""

import pygame
import numpy as np
from player import Player
from ball import Ball
from obstacle import Brick

BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 255, 255)
SPEED = 3

rgb_list = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (128, 0, 0),    # Maroon
    (0, 128, 0),    # Dark Green
    (0, 0, 128),    # Navy
    (128, 128, 0),  # Olive
    (128, 0, 128),  # Purple
    (192, 192, 192),# Silver
    (128, 128, 128) # Gray
]
np.random.shuffle(rgb_list)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

jackson = Player(screen, PLAYER_COLOR) # (pos.x, 680, 200, 30)
ball = Ball(screen, PLAYER_COLOR)
bricks = []

brick_sprite_group = pygame.sprite.Group()
position = pygame.Vector2(10, 20)
brick_height = 25
brick_width = 0
gap_y = 5
gap_x = 5
index_color = 0
while position.y < 380:
    position.x = 10
    clr = rgb_list[index_color]
    while position.x < 1270:
        brick_width = np.random.randint(50, 100)
        if position.x + brick_width > 1270:
            brick_width = 1270 - position.x
        brick = Brick(screen, clr, brick_width, brick_height, position.x, position.y)
        bricks.append(brick)
        brick_sprite_group.add(brick)
        position.x = position.x + brick_width + gap_x
    index_color = index_color + 1
    position.y = position.y + brick_height + gap_y

ball_sprite_group = pygame.sprite.Group()
ball_sprite_group.add(ball)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)

    keys = pygame.key.get_pressed()

    brick_sprite_group.update()
    brick_sprite_group.draw(screen)

    jackson.update(keys)
    jackson.draw()

    if keys[pygame.K_r]:
        ball.random_pos()
    ball_sprite_group.update()
    ball_sprite_group.draw(screen)

    if len(pygame.sprite.spritecollide(jackson, ball_sprite_group, False)) != 0:
        ball.velocity.y = -ball.velocity.y

    if pygame.sprite.groupcollide(brick_sprite_group, ball_sprite_group, True, False):
        ball.velocity.y = -ball.velocity.y

    pygame.display.flip()
    clock.tick(144)

pygame.quit()