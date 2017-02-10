import sys

class KeyMap(object):
    keys = {
    ord('1') : [0, 0],
    ord('2') : [1, 0],
    ord('3') : [2, 0],
    ord('4') : [3, 0],
    ord('5') : [4, 0],
    ord('6') : [5, 0],
    ord('7') : [6, 0],
    ord('8') : [7, 0],
    ord('9') : [8, 0],
    ord('0') : [9, 0],

    ord('q') : [0, 1],
    ord('w') : [1, 1],
    ord('e') : [2, 1],
    ord('r') : [3, 1],
    ord('t') : [4, 1],
    ord('y') : [5, 1],
    ord('u') : [6, 1],
    ord('i') : [7, 1],
    ord('o') : [8, 1],
    ord('p') : [9, 1],

    ord('a') : [0, 2],
    ord('s') : [1, 2],
    ord('d') : [2, 2],
    ord('f') : [3, 2],
    ord('g') : [4, 2],
    ord('h') : [5, 2],
    ord('j') : [6, 2],
    ord('k') : [7, 2],
    ord('l') : [8, 2],
    ord(';') : [9, 2],

    ord('z') : [0, 3],
    ord('x') : [1, 3],
    ord('c') : [2, 3],
    ord('v') : [3, 3],
    ord('b') : [4, 3],
    ord('n') : [5, 3],
    ord('m') : [6, 3],
    ord(',') : [7, 3],
    ord('.') : [8, 3],
    ord('/') : [9, 3],
    }

    def handleKey(self, key, board, screen):
        if key == ord('`'):
            sys.exit(0)

        point = self.keys.get(key)
        if point:
            box = board[point[0]][point[1]]
            if box.selected:
                box.unselect()
                screen.refresh()
            else:
                box.select()
                screen.refresh()
