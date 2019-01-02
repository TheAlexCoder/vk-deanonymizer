end = '\x1b[0m'

colors = {
    'BLACK_DEFAULT': '\x1b[30m',
    'RED_DEFAULT': '\x1b[31m',
    'GREEN_DEFAULT': '\x1b[32m',
    'YELLOW_DEFAULT': '\x1b[33m',
    'BLUE_DEFAULT': '\x1b[34m',
    'PURPLE_DEFAULT': '\x1b[35m',
    'LIGHT_BLUE_DEFAULT': '\x1b[36m',
    'WHITE_DEFAULT': '\x1b[37m',

    'BLACK_BOLD': '\x1b[30;1m',
    'RED_BOLD': '\x1b[31;1m',
    'GREEN_BOLD': '\x1b[32;1m',
    'YELLOW_BOLD': '\x1b[33;1m',
    'BLUE_BOLD': '\x1b[34;1m',
    'PURPLE_BOLD': '\x1b[35;1m',
    'LIGHT_BLUE_BOLD': '\x1b[36;1m',
    'WHITE_BOLD': '\x1b[37;1m',

    'BLACK_UNDERLINED': '\x1b[30;4m',
    'RED_UNDERLINED': '\x1b[31;4m',
    'GREEN_UNDERLINED': '\x1b[32;4m',
    'YELLOW_UNDERLINED': '\x1b[33;4m',
    'BLUE_UNDERLINED': '\x1b[34;4m',
    'PURPLE_UNDERLINED': '\x1b[35;4m',
    'LIGHT_BLUE_UNDERLINED': '\x1b[36;4m',
    'WHITE_UNDERLINED': '\x1b[37;4m',

    'BLACK_FLASHING': '\x1b[30;5m',
    'RED_FLASHING': '\x1b[31;5m',
    'GREEN_FLASHING': '\x1b[32;5m',
    'YELLOW_FLASHING': '\x1b[33;5m',
    'BLUE_FLASHING': '\x1b[34;5m',
    'PURPLE_FLASHING': '\x1b[35;5m',
    'LIGHT_BLUE_FLASHING': '\x1b[36;5m',
    'WHITE_FLASHING': '\x1b[37;5m',

    'BLACK_INVERTED': '\x1b[30;7m',
    'RED_INVERTED': '\x1b[31;7m',
    'GREEN_INVERTED': '\x1b[32;7m',
    'YELLOW_INVERTED': '\x1b[33;7m',
    'BLUE_INVERTED': '\x1b[34;7m',
    'PURPLE_INVERTED': '\x1b[35;7m',
    'LIGHT_BLUE_INVERTED': '\x1b[36;7m',
    'WHITE_INVERTED': '\x1b[37;7m',

    'BLACK_INVISIBLE': '\x1b[30;8m',
    'RED_INVISIBLE': '\x1b[31;8m',
    'GREEN_INVISIBLE': '\x1b[32;8m',
    'YELLOW_INVISIBLE': '\x1b[33;8m',
    'BLUE_INVISIBLE': '\x1b[34;8m',
    'PURPLE_INVISIBLE': '\x1b[35;8m',
    'LIGHT_BLUE_INVISIBLE': '\x1b[36;8m',
    'WHITE_INVISIBLE': '\x1b[37;8m',
}

class black:
    def default(self: str):
        return colors['BLACK_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['BLACK_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['BLACK_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['BLACK_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['BLACK_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['BLACK_INVISIBLE'] + str(self) + end

class red:
    def default(self: str):
        return colors['RED_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['RED_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['RED_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['RED_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['RED_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['RED_INVISIBLE'] + str(self) + end

class green:
    def default(self: str):
        return colors['GREEN_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['GREEN_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['GREEN_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['GREEN_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['GREEN_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['GREEN_INVISIBLE'] + str(self) + end

class yellow:
    def default(self: str):
        return colors['YELLOW_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['YELLOW_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['YELLOW_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['YELLOW_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['YELLOW_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['YELLOW_INVISIBLE'] + str(self) + end

class blue:
    def default(self: str):
        return colors['BLUE_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['BLUE_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['BLUE_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['BLUE_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['BLUE_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['BLUE_INVISIBLE'] + str(self) + end

class purple:
    def default(self: str):
        return colors['PURPLE_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['PURPLE_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['PURPLE_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['PURPLE_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['PURPLE_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['PURPLE_INVISIBLE'] + str(self) + end

class light_blue:
    def default(self: str):
        return colors['LIGHT_BLUE_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['LIGHT_BLUE_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['LIGHT_BLUE_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['LIGHT_BLUE_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['LIGHT_BLUE_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['LIGHT_BLUE_INVISIBLE'] + str(self) + end

class white:
    def default(self: str):
        return colors['WHITE_DEFAULT'] + str(self) + end

    def bold(self: str):
        return colors['WHITE_BOLD'] + str(self) + end

    def underlined(self: str):
        return colors['WHITE_UNDERLINED'] + str(self) + end

    def flashing(self: str):
        return colors['WHITE_FLASHING'] + str(self) + end

    def inverted(self: str):
        return colors['WHITE_INVERTED'] + str(self) + end

    def invisible(self: str):
        return colors['WHITE_INVISIBLE'] + str(self) + end
