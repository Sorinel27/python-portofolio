import pygame
import numpy as np

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, color):
        """
        This class represents the player or the moving table in the game. Use A and D to move the table left and right.
        :param screen:
        :param color:
        """
        super().__init__()
        self.screen = screen
        self.color = color
        self.width = 200
        self.height = 18
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = np.random.randint(300, 900), 680
        self.speed = 3

    def update(self, keys):
        """
        Update the position of the table based on the keys pressed.
        :param keys:
        :return:
        """
        pygame.sprite.Sprite.update(self)
        if keys[pygame.K_a]:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.speed
        if keys[pygame.K_d]:
            if self.rect.x >= 1080:
                self.rect.x = 1080
            else:
                self.rect.x += self.speed

    def draw(self):
        """
        Draw the table on the screen.
        :return:
        """
        self.screen.blit(self.image, self.rect)
