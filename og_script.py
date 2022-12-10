#!/usr/bin/env python3
from time import sleep
import characters_swiss as _
from os import name as OS


sleep(5)



def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


if OS == 'posix':
    write_report(_.release)
    write_report(_.terminal_linux)
    write_report(_.release)

    sleep(1)

    write_report(_.e)
    write_report(_.c)
    write_report(_.h)
    write_report(_.o)
    write_report(_.release)

    write_report(_.spacebar)
    write_report(_.release)

    write_report(_.l)
    write_report(_.o)
    write_report(_.l)
    write_report(_.release)

    write_report(_.enter)
    write_report(_.release)
else: # script for Windows os
    pass