import pygame
import math
import numpy as np

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, color):
        """
        This class represents the ball in the game. The ball will bounce off the walls, table and bricks.
        :param screen:
        :param color:
        """
        super().__init__()
        self.screen = screen
        self.color = color
        self.diameter = 10
        self.radius = self.diameter / 2.0
        self.image = pygame.Surface((self.diameter, self.diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = np.random.randint(300, 900), np.random.randint(400, 600)

        self.velocity = pygame.Vector2()
        self.velocity.x, self.velocity.y = np.random.randint(3, 5), np.random.randint(3, 5) 

    def update(self):
        """
        Update the position of the ball. This includes the logic of bouncing off the walls and the table.
        :return:
        """
        width, height = 1280, 720

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Bounce off the walls if the ball reaches the screen edges
        if self.rect.left <= 5 or self.rect.right >= width - 5:
            self.velocity.x = -self.velocity.x
        if self.rect.top <= 5:
            self.velocity.y = -self.velocity.y

        if self.rect.bottom >= height - 5:
            self.random_pos()

    def random_pos(self):
        """
        Randomize the position of the ball when the player presses R.
        :return:
        """
        self.rect.x, self.rect.y = np.random.randint(300, 900), np.random.randint(400, 600)

