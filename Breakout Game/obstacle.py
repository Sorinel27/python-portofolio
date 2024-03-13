import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, color, width, height, position_x, position_y):
        """
        This class represent a brick in the game. The width is random based on the range between 50 and 100.
        :param screen:
        :param color:
        :param width:
        :param height:
        :param position_x:
        :param position_y:
        """
        super().__init__()
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position_x, position_y

    def update(self):
        """
        Update the position of the brick.
        :return:
        """
        pygame.sprite.Sprite.update(self)

    def draw(self):
        """
        Draw the brick on the screen.
        :return:
        """
        self.screen.blit(self.image, self.rect)
        