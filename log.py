from sys import platform

end = '\x1b[0m'

windows = [
    'win32',
    'win64'
]

windows = []                      # Uncomment / Comment this line to see colors in Windows / Not to see colors in Windows

colors = {
    'BLACK': '\x1b[30;0m',
    'RED': '\x1b[31;0m',
    'GREEN': '\x1b[32;0m',
    'YELLOW': '\x1b[33;0m',
    'BLUE': '\x1b[34;0m',
    'PURPLE': '\x1b[35;0m',
    'LIGHT_BLUE': '\x1b[36;0m',
    'WHITE': '\x1b[37;0m',

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

    'BLACK_BLINDING': '\x1b[30;5m',
    'RED_BLINDING': '\x1b[31;5m',
    'GREEN_BLINDING': '\x1b[32;5m',
    'YELLOW_BLINDING': '\x1b[33;5m',
    'BLUE_BLINDING': '\x1b[34;5m',
    'PURPLE_BLINDING': '\x1b[35;5m',
    'LIGHT_BLUE_BLINDING': '\x1b[36;5m',
    'WHITE_BLINDING': '\x1b[37;5m',
}

if platform in windows:
    linux = False
    print('[!] Log lib warning: colors may not be displayed in windows console. You can uncomment line 10 in log.py, to see colors on Windows.')
    print()

else:
    linux = True

    b_ = colors['WHITE_BOLD'] + '[' + end
    _b = colors['WHITE_BOLD'] + '] ' + end

def show_colors():
    i = 0

    for color in colors:
        if i % 3 == 0:
            print()

        print(colors[color] + color + end, end=' / ')
        i += 1

    exit(0)

def raiseError(color):
    print(colors['RED_BOLD'] + 'Log lib error: Incorrect collor "' + color + '". Use one of the following:\n' + end)
    show_colors()

def constructor(color, central_text, main_text):
    central_text = str(central_text)
    main_text = str(main_text)

    if linux:
        text = colors['WHITE_BOLD'] + main_text + end

        if color.upper() in colors:
            print(b_ + colors[color.upper()] + central_text + end + _b + text)

        else:
            raiseError(color)

    else:
        print('[' + central_text + '] ' + main_text)

def plus(text, color=None):
    text = str(text)

    if linux:
        text = colors['WHITE_BOLD'] + text + end

        if color:

            if color.upper() in colors:
                print(b_ + colors[color.upper()] + '+' + end + _b + text)

            else:
                raiseError(color)

        else:
            print(b_ + colors['GREEN_BOLD'] + '+' + end + _b + text)

    else:
        print('[+]' + ' ' + text)

def minus(text, color=None):
    text = str(text)

    if linux:
        text = colors['WHITE_BOLD'] + text + end

        if color:

            if color.upper() in colors:
                print(b_ + colors[color.upper()] + '-' + end + _b + text)

            else:
                raiseError(color)

        else:
            print(b_ + colors['RED_BOLD'] + '-' + end + _b + text)

    else:
        print('[-]' + ' ' + text)

def info(text, color=None):
    text = str(text)

    if linux:
        text = colors['WHITE_BOLD'] + text + end

        if color:

            if color.upper() in colors:
                print(b_ + colors[color.upper()] + '*' + end + _b + text)

            else:
                raiseError(color)

        else:
            print(b_ + colors['BLUE_BOLD'] + '*' + end + _b + text)

    else:
        print('[*]' + ' ' + text)

def warning(text, color=None):
    text = str(text)

    if linux:
        text = colors['WHITE_BOLD'] + text + end

        if color:

            if color.upper() in colors:
                print(b_ + colors[color.upper()] + '!' + end + _b + text)

            else:
                raiseError(color)

        else:
            print(b_ + colors['RED_BOLD'] + '!' + end + _b + text)

    else:
        print('[!] ' + text)

def error(text):                            # Experimental method
    text = str(text)

    if linux:
        text = colors['WHITE_BOLD'] + text + end

        print(colors['YELLOW_BOLD'] + '⚠' + end + ' ' + text)
    else:
       print('⚠' + ' ' + text)

# Thank you for using my lib <3
