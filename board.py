import curses
import pygame
import time
from box import Box
from keyMap import KeyMap

class Board(object):
    key = -1
    board = []
    keyMap = KeyMap()

    def __init__(self, screen, COL_COUNT, ROW_COUNT):
        self.ROW_COUNT = ROW_COUNT
        self.COL_COUNT = COL_COUNT
        self.createBoard(screen)

    def createBoard(self, screen):
        dims = screen.getmaxyx()
        height = (dims[0] - self.ROW_COUNT - 1) / self.ROW_COUNT
        width = (dims[1] - self.COL_COUNT - 1) / self.COL_COUNT

        for col in range(0, self.COL_COUNT):
            column = []
            for row in range(0, self.ROW_COUNT):
                box = Box(
                    screen.subwin(height, width, (height + 1) * row + 1, (width + 1) * col + 1),
                    'mp3/%d.ogg'%(row*2)
                    )
                column.append(box)
            self.board.append(column)

    def drawProgressLine(self, screen, mixer):
        board_size = len(self.board)
        for i in range(0, board_size):
            max_len =board_size - 1
            if i == 0:
                low = max_len
            else:
                low = i - 1
            self.setProgressColor(low, "LOW", None)
            self.setProgressColor(i, "HIGH", mixer)

            curses.doupdate()
            newKey = screen.getch()
            if self.key != newKey:
                self.keyMap.handleKey(self.key, self.board, screen)
                self.key = newKey
            time.sleep(0.25)

    def setProgressColor(self, column_idx, highlight, mixer):
        for box in self.board[column_idx]:
            if highlight == "HIGH":
                if box.selected == True:
                    s = mixer.Sound(box.sound)
                    mixer.find_channel().play(s)
                    box.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE | curses.A_BOLD)
                else:
                    box.window.bkgd(' ', curses.color_pair(2) | curses.A_REVERSE | curses.A_BOLD)
            else:
                if box.selected == True:
                    box.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE)
                else:
                    box.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
            box.window.noutrefresh()
