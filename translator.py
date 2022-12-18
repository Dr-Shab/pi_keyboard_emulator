import sys

specials = "+\"*ç%&/()=?`|@#¼½¬|¢]}´~[]{}!,;.:-_<\\>"


def letter_to_key(word, file):
    for letter in word:
        if letter.isnumeric():
            file.write(f"    write_report(_.number[\"{letter}\"])\n")
            file.write("    write_report(_.operation[\"release\"])\n")
            file.write("    sleep(0.1)\n\n")

        elif letter in specials:
            file.write(f"    write_report(_.special_key[\"{letter}\"])\n")
            file.write("    sleep(0.1)\n\n")  # when shift key is pressed sleep needs to be here so the terminal can react...
            file.write("    write_report(_.operation[\"release\"])\n")

        elif letter.islower():
            file.write(f"    write_report(_.lowercase[\"{letter}\"])\n")
            file.write("    write_report(_.operation[\"release\"])\n")
            file.write("    sleep(0.1)\n\n")

        elif letter.isupper():
            file.write(f"    write_report(_.uppercase[\"{letter}\"])\n")
            file.write("    sleep(0.1)\n\n")  # when shift key is pressed sleep needs to be here so the terminal can react...
            file.write("    write_report(_.operation[\"release\"])\n")

    file.write("    write_report(_.special_key[\"space\"])\n")
    file.write("    write_report(_.operation[\"release\"])\n")
    file.write("    sleep(0.1)\n\n")
    return "lets buckling go"


def translate(cmd_file, output_file="cmd_to_strokes.py"):
    lang = input("Which keyboard layout is used? ch or.. ")
    if len(lang) == 2 and lang.isalpha():
        with open(f'{output_file}.py', 'x') as wf:
            wf.write(f"from time import sleep\nimport keys_{lang}_keyboard as _\nfrom os import name as OS\n\n")
            wf.write("sleep(5)\n\nNULL_CHAR = chr(0)\n\n\n")
            wf.write(
                "def write_report(report):\n    with open('/dev/hidg0', 'rb+') as fd:\n         fd.write(report.encode())\n\n\n")
            wf.write("if OS == 'posix':\n")
            wf.write("    write_report(_.operation[\"release\"])\n")
            wf.write("    write_report(_.operation[\"terminal_linux\"])\n")
            wf.write("    write_report(_.operation[\"release\"])\n")
            wf.write("    sleep(2)\n\n")
            with open(cmd_file, 'r') as rf:
                lines = rf.readlines()
                for line in lines:
                    words = line.split(" ")
                    for word in words:
                        if "\n" in word:
                            letter_to_key(word.strip("\n"), wf)
                            wf.write("    write_report(_.special_key[\"enter\"])\n")
                            wf.write("    write_report(_.operation[\"release\"])\n\n")
                            wf.write("    sleep(0.5)\n\n")
                        else:
                            letter_to_key(word, wf)
        print(f'successfully generated the script {output_file}.py')
        exit(0)
    else:
        print("are you kidding me?!")
        exit(1)


if __name__ == "__main__":
    translate(str(sys.argv[1]), str(sys.argv[2]))
