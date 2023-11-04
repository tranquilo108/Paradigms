import pygame
import sys


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.size_block = 120
        self.margin = 10
        self.width = self.height = self.size_block * 3 + self.margin * 4
        self.size_window = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size_window)
        pygame.display.set_caption('Крестики-нолики')
        self.black, self.green, self.white = 'black', 'green', 'white'
        self.table = [[0] * 3 for _ in range(3)]
        self.counter = 0
        self.offset = 10
        self.game_over = False

    def check_win(self, sign):
        zeroes = 0
        for row in self.table:
            zeroes += row.count(0)
            if row.count(sign) == 3:
                return sign
        for col in range(3):
            if self.table[0][col] == sign and self.table[1][col] == sign and self.table[2][col] == sign:
                return sign
        if self.table[0][0] == sign and self.table[1][1] == sign and self.table[2][2] == sign:
            return sign
        if self.table[0][2] == sign and self.table[1][1] == sign and self.table[2][0] == sign:
            return sign
        if zeroes == 0:
            return 'Ничья'
        return False

    def draw_board(self):
        for row in range(3):
            for col in range(3):
                x = col * self.size_block + (col + 1) * self.margin
                y = row * self.size_block + (row + 1) * self.margin
                pygame.draw.rect(self.screen, self.green, (x, y, self.size_block, self.size_block))
                if self.table[row][col] == 'x':
                    pygame.draw.line(self.screen, self.white, (x + self.offset, y + self.offset),
                                     (x + self.size_block - self.offset, y + self.size_block - self.offset), 10)
                    pygame.draw.line(self.screen, self.white, (x + self.offset, y + self.size_block - self.offset),
                                     (x - self.offset + self.size_block, y + self.offset), self.offset)
                elif self.table[row][col] == 'o':
                    pygame.draw.circle(self.screen, self.black, (x + self.size_block // 2, y + self.size_block // 2),
                                       self.size_block // 2 - 10, self.offset)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over and pygame.mouse.get_pressed().index(
                        True) == 0:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (self.size_block + self.margin + self.margin // 2)
                    row = y_mouse // (self.size_block + self.margin + self.margin // 2)
                    if self.table[row][col] == 0:
                        if self.counter % 2 == 0:
                            self.table[row][col] = 'x'
                        else:
                            self.table[row][col] = 'o'
                        self.counter += 1
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed().index(True) == 2:
                    self.game_over = False
                    self.table = [[0] * 3 for _ in range(3)]
                    self.counter = 0
                    self.screen.fill(self.black)

            if not self.game_over:
                self.draw_board()

            if (self.counter - 1) % 2 == 0:
                self.game_over = self.check_win('x')
            else:
                self.game_over = self.check_win('o')

            if self.game_over:
                self.screen.fill(self.black)
                font = pygame.font.SysFont('Ubuntu', 27)
                text1 = font.render(f'Победил {self.game_over}', True, self.white)
                text2 = font.render('Нажмите ПКМ', True, self.white)
                x1 = self.screen.get_width() / 2 - text1.get_rect().width / 2
                y1 = self.screen.get_height() / 2 - text1.get_rect().height / 2
                x2 = self.screen.get_width() / 2 - text2.get_rect().width / 2
                y2 = self.screen.get_height() / 2 - text2.get_rect().height / 2
                self.screen.blit(text1, [x1, y1])
                self.screen.blit(text2, [x2, y2 + 30])
            pygame.display.update()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
