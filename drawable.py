import pygame
from pygame.locals import *


class Drawable:

    def __init__(self, width, height, x, y, color =(255, 255, 255)):
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.surface.get_rect(x=x, y=y)

    def draw_on(self, surface):
        surface.blit(self.surface, self.rect)


class Ball(Drawable):

    def __init__(self, width, height, x, y, color=(255, 255, 255), x_speed=5, y_speed=5):
        super(Ball, self).__init__(width, height, x, y, color)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.start_x = x
        self.start_y = y

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset(self):
        self.rect.move(self.start_x, self.start_y)
        self.bounce_y()

    def move(self, board, *args):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x <= 0 or self.rect.x >= board.surface.get_width():
            self.bounce_x()

        if self.rect.y <= 15 or self.rect.y >= board.surface.get_height() - 30:
            self.bounce_y()

        for racket in args:
            if self.rect.colliderect(racket.rect):
                self.bounce_x()
                if 12 > self.x_speed > 0:
                    self.x_speed += 0.2
                elif -12 < self.x_speed < 0:
                    self.x_speed -= 0.2


class Racket(Drawable):

    def __init__(self, width, height, x, y, color=(255, 255, 255), max_speed=10):
        super(Racket, self).__init__(width, height, x, y, color)
        self.max_speed = max_speed
        self.surface.fill(color)

    def move(self):
        keys = pygame.key.get_pressed()  # checking pressed keys

        if keys[pygame.K_UP]:
            if self.rect.y > 15:
                self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if self.rect.y < 505:
                self.rect.y += 5

    def ai_move(self, y):
        delta = y - self.rect.y
        if abs(delta) > self.max_speed:
            delta = self.max_speed if delta > 0 else -self.max_speed
        if 520 > self.rect.y > 15:
            self.rect.y += delta
            print(self.rect.y)
        if self.rect.y == 520:
            print(self.rect.y)
            self.rect.y -= 10




class Ai(object):

    def __init__(self, racket, ball):
        self.ball = ball
        self.racket = racket

    def move(self):
        y = self.ball.rect.centery
        self.racket.ai_move(y)

