import curses

class Box(object):
    selected = False

    def __init__(self, window, sound):
        self.window = window
        self.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
        self.window.noutrefresh()
        self.sound = sound

    def reset(self):
        self.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
        self.window.noutrefresh()

    def select(self):
        self.selected = True
        self.window.bkgd(' ', curses.color_pair(3) | curses.A_REVERSE)
        self.window.noutrefresh()

    def unselect(self):
        self.selected = False
        self.window.bkgd(' ', curses.color_pair(1) | curses.A_REVERSE)
        self.window.noutrefresh()
