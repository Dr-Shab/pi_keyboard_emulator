numbers = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}

specials = {
    '!': 'esclamation',
    '"': 'doublequote',
    '#': 'hashtag',
    '$': 'dollar',
    '%': 'percent',
    '&': 'ampersand',
    "'": 'singlequote',
    '(': 'leftparent',
    ')': 'rightparent',
    '*': 'asterisk',
    '+': 'plus',
    ',': 'comma',
    '-': 'minus',
    '.': 'point',
    '/': 'slash',
    ':': 'semicolon',
    '<': 'less',
    '=': 'equal',
    '>': 'greater',
    '?': 'question',
    '@': 'at',
    '[': 'leftbracket',
    '\\': 'backslash',
    ']': 'rightbracket',
    '^': 'caret',
    '_': 'underscore',
    '{': 'leftbrace',
    '|': 'pipe',
    '}': 'rightbrace',
    '~': 'tilde'
}

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def letter_to_USB(word):
    for letter in word:
        if letter in numbers:
            number = numbers[letter]
            f.write(f"    write_report(_.{number})\n")
            f.write("    sleep(0.1)\n")
            f.write("    write_report(_.release)\n")
        elif letter in specials:
            special = specials[letter]
            f.write(f"    write_report(_.{special})\n")
            f.write("    sleep(0.1)\n")
            f.write("    write_report(_.release)\n")
        elif letter in uppercase:
            f.write(f"    write_report(_.{letter})\n")
            f.write("    sleep(0.1)\n")
            f.write("    write_report(_.release)\n")
        else:
            f.write(f"    write_report(_.{letter})\n")
            f.write("    sleep(0.1)\n")
            f.write("    write_report(_.release)\n")

    f.write("    write_report(_.spacebar)\n")
    f.write("    write_report(_.release)\n\n")


with open('victim_script.py', 'x') as f:
    f.write("from time import sleep\nimport characters_swiss as _\nfrom os import name as OS\n\n")
    f.write("sleep(5)\n\nNULL_CHAR = chr(0)\n\n\n")
    f.write("def write_report(report):\n    with open('/dev/hidg0', 'rb+') as fd:\n         fd.write(report.encode())\n\n\n")
    f.write("if OS == 'posix':\n")
    f.write("    write_report(_.release)\n")
    f.write("    write_report(_.terminal_linux)\n")
    f.write("    write_report(_.release)\n")
    f.write("    sleep(1)\n\n")
    with open('raw_script_posix.txt', 'r') as rsf:
        lines = rsf.readlines()
        for line in lines:
            words = line.split(" ")
            for word in words:
                if "\n" in word:
                    letter_to_USB(word.strip("\n"))
                    f.write("    write_report(_.enter)\n")
                    f.write("    write_report(_.release)\n\n")
                    f.write("    sleep(0.5)\n\n")
                else:
                    letter_to_USB(word)






