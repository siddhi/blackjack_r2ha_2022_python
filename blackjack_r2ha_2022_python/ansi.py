from enum import Enum


class Colour(Enum):
    BLACK = (30, 40)
    RED = (31, 41)
    GREEN = (32, 42)
    YELLOW = (33, 43)
    BLUE = (34, 44)
    MAGENTA = (35, 45)
    CYAN = (36, 46)
    WHITE = (37, 47)
    DEFAULT = (39, 49)


class Ansi:
    fg_colour = Colour.DEFAULT.value[0]
    bg_colour = Colour.DEFAULT.value[1]

    def __init__(self, string=""):
        self.string = string

    def _append(self, code):
        return Ansi(self.string + code)

    def reset(self):
        return self._append("\x1b[0;m")

    def erase(self):
        return self._append("\x1b[2J")

    def cursor_up(self, count):
        code = f"\x1b[{count}A"
        return self._append(code)

    def cursor_down(self, count):
        code = f"\x1b[{count}B"
        return self._append(code)

    def cursor_right(self, count):
        code = f"\x1b[{count}C"
        return self._append(code)

    def cursor_left(self, count):
        code = f"\x1b[{count}D"
        return self._append(code)

    def cursor(self, line, col):
        code = f"\x1b[{line};{col}H"
        return self._append(code)

    def fg(self, colour):
        Ansi.fg_colour = colour.value[0]
        code = f"\x1b[0;{Ansi.fg_colour};{Ansi.bg_colour}m"
        return self._append(code)

    def bg(self, colour):
        Ansi.bg_colour = colour.value[1]
        code = f"\x1b[0;{Ansi.fg_colour};{Ansi.bg_colour}m"
        return self._append(code)

    def __str__(self):
        return self.string
