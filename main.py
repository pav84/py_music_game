import curses
import time
import pygame
from box import Box
from keyMap import KeyMap

ROW_COUNT = 4
COL_COUNT = 10
boxes = []
boxes_cols = []

pygame.mixer.init()
sound = pygame.mixer.music
q = -1

def drawBoxes():
    for col in range(0, COL_COUNT):
        boxes_cols = []
        for row in range(0, ROW_COUNT):
            box = Box(
                screen.subwin(height, width, (height + 1) * row + 1, (width + 1) * col + 1),
                'mp3/%d.ogg'%(row*2)
                )
            boxes_cols.append(box)
        boxes.append(boxes_cols)

def drawProgress():
    for i in range(0, len(boxes)):
        max_len = len(boxes) - 1
        if i == 0:
            middle = max_len
            low = max_len - 1
        elif i == 1:
            middle = 0
            low = max_len
        else:
            middle = i - 1
            low = i - 2
        setColumnColor(middle, "LOW")
        # setColumnColor(middle, "MIDDLE")
        setColumnColor(i, "HIGH")

        curses.doupdate()
        global q
        q = screen.getch()
        if q != -1:
            selectBox()
        time.sleep(0.17)

def setColumnColor(column_idx, highlight):
    for box in boxes[column_idx]:
        if highlight == "HIGH":
            if box.selected == True:
                sound.load(box.sound)
                sound.play()
                box.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE | curses.A_BOLD)
            else:
                box.window.bkgd(' ', curses.color_pair(2) | curses.A_REVERSE | curses.A_BOLD)
        # elif highlight == "MIDDLE":
        #     if box.selected == True:
        #         box.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE)
        #     else:
        #         box.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE | curses.A_BOLD)
        else:
            if box.selected == True:
                box.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE)
            else:
                box.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
        box.window.noutrefresh()

def selectBox():
    global q
    point = KeyMap.keys[q]
    box = boxes[point[0]][point[1]]
    if box.selected:
        box.unselect()
        screen.refresh()
    else:
        box.select()
        screen.refresh()
    q = -1


try:
    screen = curses.initscr()
    curses.noecho()
    screen.nodelay(1)
    curses.start_color()
    dims = screen.getmaxyx()
    height = (dims[0] - ROW_COUNT - 1) / ROW_COUNT
    width = (dims[1] - COL_COUNT - 1) / COL_COUNT

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    screen.refresh()
    drawBoxes()

    while q != ord('`'):
        drawProgress()

finally:
    curses.endwin()
