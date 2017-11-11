from board import *
from drawable import *
from menu import *
from pygame import *
import time


class Judge(object):

    def __init__(self, board, ball, *args):
        self.ball = ball
        self.board = board
        self.rackets = args
        self.score = [0, 0]
        self.score_fx = pygame.mixer.Sound('score.wav')

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 64)

    def update_score(self, board_width):
        if self.ball.rect.x < 0:
            self.score_fx.play()
            self.score[1] += 1
            self.ball.reset()
        elif self.ball.rect.x > board_width:
            self.score_fx.play()
            self.score[0] += 1
            self.ball.reset()

    def reset_score(self):
        self.score = [0, 0]

    def draw_text(self, surface,  text, x, y):
        text = self.font.render(text, True, (150, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)

    def draw_on(self, surface):
        width = self.board.surface.get_width()
        self.update_score(width)

        height = self.board.surface.get_height()
        self.draw_text(surface, "Player I: {}".format(self.score[0]), width/2, height * 0.3)
        self.draw_text(surface, "Player II: {}".format(self.score[1]), width/2, height * 0.7)

        if self.score[0] == 10:  # player 1 win
            self.draw_text(surface, "Player I WINS", width/2, height/2)
        elif self.score[1] == 10:
            self.draw_text(surface, "Player II WINS", width/2, height/2)


class PongGame():

    def __init__(self, width, height):
        pygame.init()
        mixer.init()
        self.board = Board(width, height)
        self.menu = GameMenu(self.board.surface)
        self.fps_clock = pygame.time.Clock()
        self.ball = Ball(20, 20, width/2, height/2)
        self.player1 = Racket(width=20, height=80, x=80, y=height/10)
        self.player2 = Racket(width=20, height=80, x=720, y=height/10, color=(255, 255, 255))
        self.ai = Ai(self.player2, self.ball)
        self.judge = Judge(self.board, self.ball, self.player2, self.ball)

    def run(self):
        """
        Main game loop
        """
        game_mode = self.menu.run()
        self.judge.reset_score()
        if game_mode == "Single Player":
            while True:
                self.handle_quit()
                self.ball.move(self.board, self.player1, self.player2)
                self.board.draw(
                    self.ball,
                    self.player1,
                    self.player2,
                    self.judge
                )
                self.ai.move()
                self.player1.move_player_one()

                if self.judge.score[0] == 10 or self.judge.score[1] == 10:
                    time.sleep(1)
                    self.run()

                self.fps_clock.tick(30)
        elif game_mode == "Multi Player":
            while True:
                self.handle_quit()
                self.ball.move(self.board, self.player1, self.player2)
                self.board.draw(
                    self.ball,
                    self.player1,
                    self.player2,
                    self.judge
                )
                self.player1.move_player_one()
                self.player2.move_player_two()

                if self.judge.score[0] == 10 or self.judge.score[1] == 10:
                    time.sleep(1)
                    self.run()

                self.fps_clock.tick(30)
        elif game_mode == "Controls":
            while True:
                self.handle_quit()
                move_back = self.menu.controls_screen()
                if move_back == "Back":
                    self.run()

    def handle_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run()


if __name__ == "__main__":
    game = PongGame(800, 600)
    game.run()
