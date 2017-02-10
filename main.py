import curses
import pygame
from board import Board

ROW_COUNT = 4
COL_COUNT = 10
board = []

print "For exit press '~'"
print 'Loading pygame...'
pygame.mixer.init()
sound = pygame.mixer.music

try:
    screen = curses.initscr()
    curses.noecho()
    screen.nodelay(1)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    screen.refresh()
    board = Board(screen, COL_COUNT, ROW_COUNT)
    while True:
        board.drawProgressLine(screen, sound)

finally:
    curses.endwin()
