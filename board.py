import pygame
import pygame.locals


class Board:
    """
    Handles showing game screen
    """

    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption("PONG GAME")

    def draw(self, *args):
        black = (0, 0, 0)
        background = pygame.image.load('field.png')
        self.surface.blit(background, (0,0))
        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.update()

