import curses
import time

ROW_COUNT = 4
COL_COUNT = 8
boxes = []
boxes_cols = []

def drawBoxes():
    for col in range(0, COL_COUNT):
        boxes_cols = []
        for row in range(0, ROW_COUNT):
            box = curses.newwin(height, width, (height + 1) * row + 1, (width + 1) * col + 1)
            box.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
            box.refresh()
            boxes_cols.append(box)
        boxes.append(boxes_cols)

def setColColor(column_idx, highlight):
    if column_idx > 0:
        for box in boxes[column_idx - 1]:
            if highlight == True:
                box.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE | curses.A_BOLD)
            else:
                box.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
            box.refresh()
    else:
        pass

    for box in boxes[column_idx]:
        if highlight == True:
            box.bkgd(' ', curses.color_pair(2) | curses.A_REVERSE | curses.A_BOLD)
        else:
            box.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
        box.refresh()


screen = curses.initscr()
curses.noecho()
screen.nodelay(1)
curses.start_color()
dims = screen.getmaxyx()
height = (dims[0] - ROW_COUNT - 1) / ROW_COUNT
width = (dims[1] - COL_COUNT - 1) / COL_COUNT

curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

screen.refresh()
drawBoxes()

q = -1
while q != ord('q'):
    for i in range(0, len(boxes)):
        setColColor(i, True)
        time.sleep(0.5)
        setColColor(i, False)
    q = screen.getch()

# screen.refresh()
curses.endwin()
