null_char = chr(0)
null2 = null_char * 2
null5 = null_char * 5

lowercase = {
    "a": null5 + chr(4) +  null5,
    "b": null5 + chr(5) +  null5,
    "c": null5 + chr(6) +  null5,
    "d": null5 + chr(7) +  null5,
    "e": null5 + chr(8) +  null5,
    "f": null5 + chr(9) +  null5,
    "g": null5 + chr(10) + null5,
    "h": null5 + chr(11) + null5,
    "i": null5 + chr(12) + null5,
    "j": null5 + chr(13) + null5,
    "k": null5 + chr(14) + null5,
    "l": null5 + chr(15) + null5,
    "m": null5 + chr(16) + null5,
    "n": null5 + chr(17) + null5,
    "o": null5 + chr(18) + null5,
    "p": null5 + chr(19) + null5,
    "q": null5 + chr(20) + null5,
    "r": null5 + chr(21) + null5,
    "s": null5 + chr(22) + null5,
    "t": null5 + chr(23) + null5,
    "u": null5 + chr(24) + null5,
    "v": null5 + chr(25) + null5,
    "w": null5 + chr(26) + null5,
    "x": null5 + chr(27) + null5,
    "y": null5 + chr(28) + null5,
    "z": null5 + chr(29) + null5
}

uppercase = {
    "A": chr(32) + null_char + chr(4) +  null5,
    "B": chr(32) + null_char + chr(5) +  null5,
    "C": chr(32) + null_char + chr(6) +  null5,
    "D": chr(32) + null_char + chr(7) +  null5,
    "E": chr(32) + null_char + chr(8) +  null5,
    "F": chr(32) + null_char + chr(9) +  null5,
    "G": chr(32) + null_char + chr(10) + null5,
    "H": chr(32) + null_char + chr(11) + null5,
    "I": chr(32) + null_char + chr(12) + null5,
    "J": chr(32) + null_char + chr(13) + null5,
    "K": chr(32) + null_char + chr(14) + null5,
    "L": chr(32) + null_char + chr(15) + null5,
    "M": chr(32) + null_char + chr(16) + null5,
    "N": chr(32) + null_char + chr(17) + null5,
    "O": chr(32) + null_char + chr(18) + null5,
    "P": chr(32) + null_char + chr(19) + null5,
    "Q": chr(32) + null_char + chr(20) + null5,
    "R": chr(32) + null_char + chr(21) + null5,
    "S": chr(32) + null_char + chr(22) + null5,
    "T": chr(32) + null_char + chr(23) + null5,
    "U": chr(32) + null_char + chr(24) + null5,
    "V": chr(32) + null_char + chr(25) + null5,
    "W": chr(32) + null_char + chr(26) + null5,
    "X": chr(32) + null_char + chr(27) + null5,
    "Y": chr(32) + null_char + chr(28) + null5,
    "Z": chr(32) + null_char + chr(29) + null5
}

number = {
    "1": null5 + chr(30) + null5,
    "2": null5 + chr(31) + null5,
    "3": null5 + chr(32) + null5,
    "4": null5 + chr(33) + null5,
    "5": null5 + chr(34) + null5,
    "6": null5 + chr(35) + null5,
    "7": null5 + chr(36) + null5,
    "8": null5 + chr(37) + null5,
    "9": null5 + chr(38) + null5,
    "0": null5 + chr(39) + null5
}

operation = {
    "release": null_char * 8,
    "terminal_linux": chr(5) + null_char + chr(23) + null5,
}

special_key = {
    "+": chr(32) + null_char + chr(30) + null5,
    "\"": chr(32) + null_char + chr(31) + null5,
    "*": chr(32) + null_char + chr(32) + null5,
    "%": chr(32) + null_char + chr(34) + null5,
    "&": chr(32) + null_char + chr(35) + null5,
    "/": chr(32) + null_char + chr(36) + null5,
    "(": chr(32) + null_char + chr(37) + null5,
    ")": chr(32) + null_char + chr(38) + null5,
    "=": chr(32) + null_char + chr(39) + null5,
    "enter": null2 + chr(40) + null5,
    "esc": null2 + chr(41) + null5,
    "del": null2 + chr(42) + null5,
    "tab": null2 + chr(43) + null5,
    "space": null2 + chr(44) + null5,
    "'": null2 + chr(45) + null5,
    "?": chr(32) + null_char + chr(45) + null5,
    "^": null2 + chr(46) + null5,
    "`": chr(32) + null_char + chr(46) + null5,
    "~": chr(64) + null_char + chr(46) + null5,
    "[": chr(64) + null_char + chr(47) + null5,
    "]": chr(64) + null_char + chr(47) + null5,
    "!": chr(32) + null_char + chr(47) + null5,
    "{": chr(64) + null_char + chr(52) + null5,
    "}": chr(64) + null_char + chr(49) + null5,
    "|": chr(64) + null_char + chr(30) + null5,  # or "chr(64) + null_char + chr(36) + null5"
    "@": chr(64) + null_char + chr(31) + null5,
    "#": chr(64) + null_char + chr(32) + null5,
    "$": null2 + chr(50) + null5,
    ",": null2 + chr(54) + null5,
    ";": chr(32) + null_char + chr(54) + null5,
    ".": null2 + chr(55) + null5,
    ":": chr(32) + null_char + chr(55) + null5,
    "-": null2 + chr(56) + null5,
    "_": chr(32) + null_char + chr(56) + null5,
    "<": null2 + chr(100) + null5,
    ">": chr(32) + null_char + chr(100) + null5,
    "\\": chr(64) + null_char + chr(100) + null5
}
