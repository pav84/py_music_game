import curses
import time
from box import Box

ROW_COUNT = 4
COL_COUNT = 16
boxes = []
boxes_cols = []
selected = []
q = -1

def drawBoxes():
    for col in range(0, COL_COUNT):
        boxes_cols = []
        for row in range(0, ROW_COUNT):
            box = Box(screen.subwin(height, width, (height + 1) * row + 1, (width + 1) * col + 1))
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
        setColumnColor(low, "LOW")
        setColumnColor(middle, "MIDDLE")
        setColumnColor(i, "HIGH")

        curses.doupdate()
        time.sleep(0.1)

def setColumnColor(column_idx, highlight):
    for box in boxes[column_idx]:
        # box.setColor(highlight)
        if box.selected == True:
            box.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE | curses.A_BOLD)
        else:
            if highlight == "HIGH":
                box.window.bkgd(' ', curses.color_pair(2) | curses.A_REVERSE | curses.A_BOLD)
            elif highlight == "MIDDLE":
                box.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE | curses.A_BOLD)
            else:
                box.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
        box.window.noutrefresh()

def selectBox():
    box = boxes[7][1]
    # if q == ord('z'):
    box.select()
    # elif q == ord('x'):
        # box.unselect()
    # else:
        # pass


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
    selectBox()

    while q != ord('q'):
        drawProgress()
        q = screen.getch()

finally:
    curses.endwin()
