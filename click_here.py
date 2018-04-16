#!/usr/bin/env python3

import curses
import json
from PIL import Image
from image_to_ASCII import processer
from image_to_ASCII import end_safe
from time import sleep

class Player:
    pass

def choice(speach, shift, stdscr):
    choice = 0
    while True:
        for i in range(0, len(speach)):
            stdscr.addstr(shift + i, 1,"{})".format(i) + speach[i])
        for i in range(0, len(speach)):
            if i == choice:
                stdscr.addstr(shift + choice, 0, " ", curses.A_REVERSE)
            else:
                stdscr.addstr(shift + i, 0, ' ')
        stdscr.refresh()
        key = stdscr.getch()
        if key == 259:
            if choice > 0:
                choice -= 1
        elif key == 258:
            if choice < len(speach)-1:
                choice += 1
        elif key == ord('\n'):
            return choice


def main():
    stdscr = curses.initscr()
    stdscr.keypad(True)
    curses.noecho()
    curses.curs_set(0)

    speach1 = [
        'Ha-ha-ha-ha',
        'Use dark magic',
        'Use sword do slain this giant lizard',
        'By the way, how is your sex life?',
        'Realise that you don\'t realy need this tresher'
    ]
    
    res = choice(speach1, 20, stdscr)
    if res >= 0:
        stdscr.clear()
        stdscr.addstr(20, 10, "YOU DIED", curses.A_BOLD)
        stdscr.refresh()
        sleep(3)
    end_safe(0)

if __name__ == "__main__":
    main()