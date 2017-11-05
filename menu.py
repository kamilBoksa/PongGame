import pygame


class Button:
    def __init__(self, screen, text, x, y, width, height, active_color, inactive_color, action=None):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active_color = active_color
        self.inactive_color = inactive_color

    def draw_inactive_button(self):
        return pygame.draw.rect(self.screen, self.inactive_color, (self.x, self.y, self.width, self.height))

    def draw_active_button(self):
        return pygame.draw.rect(self.screen, self.active_color, (self.x, self.y, self.width, self.height))

    def show_button_text(self, font_name, font_size):
        font = pygame.font.Font(font_name, font_size)
        textSurf, textRect = self.text_objects(self.text, font)
        textRect.center = ((self.x + (self.width / 2)), self.y + (self.height / 2))
        self.screen.blit(textSurf, textRect)

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, (255, 255, 255))
        return text_surface, text_surface.get_rect()


class GameMenu:
    def __init__(self, screen, bg_color=(0, 0, 0)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        self.button_1 = Button(self.screen, "Single PLayer", 250, 150, 150, 30, (0, 0, 255), (0, 0, 230))
        self.button_2 = Button(self.screen, "Multi PLayer", 250, 190, 150, 30, (0, 0, 255), (0, 0, 230))
        self.button_3 = Button(self.screen, "Quit", 250, 230, 150, 30, (255, 0, 0), (230, 0, 0))

    def run(self):
        mainloop = True

        while mainloop:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # Limit frame speed to 50 FPS
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            # Redraw the background
            self.screen.fill(self.bg_color)

            # Showing buttons
            if 250 + 150 > mouse[0] > 250 and 150 + 30 > mouse[1] > 150:
                self.button_1.draw_active_button()
                if click[0] == 1:
                    return("Single Player")
            else:
                 self.button_1.draw_inactive_button()
            if 250 + 150 > mouse[0] > 250 and 190 + 30 > mouse[1] > 190:
                self.button_2.draw_active_button()
                if click[0] == 1:
                    return("Multi Player")
            else:
                self.button_2.draw_inactive_button()
            if 250 + 150 > mouse[0] > 250 and 230 + 30 > mouse[1] > 230:
                self.button_3.draw_active_button()
                if click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                self.button_3.draw_inactive_button()

            self.button_1.show_button_text("freesansbold.ttf", 16)
            self.button_2.show_button_text("freesansbold.ttf", 16)
            self.button_3.show_button_text("freesansbold.ttf", 16)

            pygame.display.flip()