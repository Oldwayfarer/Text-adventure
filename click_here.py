#!/usr/bin/env python3

import curses
import json
from PIL import Image
from image_to_ASCII import processer
from image_to_ASCII import end_safe
from time import sleep


class Player:
    def __init__(self, stren, intel, agil, atten, charis):
        self.stren = stren
        self.intel = intel
        self.agil = agil
        self.atten = atten
        self.charis = charis
        self.money = 15
        self.inventory = {}

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


def player_creator(stdscr):
    rem_points = 5
    points = [5, 5, 5, 5, 5]
    stdscr.addstr(0, 0, "Skill points: ", curses.A_BOLD)
    stdscr.addstr(1, 0, "Remaining points: ")
    stdscr.addstr(2, 0, "<   > Strength")
    stdscr.addstr(3, 0, "<   > Intellegence")
    stdscr.addstr(4, 0, "<   > Agillity")
    stdscr.addstr(5, 0, "<   > Attentiveness")
    stdscr.addstr(6, 0, "<   > Charisma")
    stdscr.addstr(7, 0, "Use arrows key to add or substruct points and navigate . Press RETURN when you are ready")
    stdscr.refresh()
    position = 0
    while True:
        stdscr.addstr(1, 19,' ')
        stdscr.addstr(1, 18, str(rem_points))
        for i in range(0, 5):
            stdscr.addstr(2 + i, 3, " ")
        for i in range(0, 5):
            if i == position:
                stdscr.addstr(2 + i, 2, str(points[i]), curses.A_REVERSE)
            else:
                stdscr.addstr(2 + i, 2, str(points[i]))
        stdscr.refresh()
        key = stdscr.getch()
        if key == 259:
            if position > 0:
                position -= 1
        elif key == 258:
            if position < 4:
                position += 1
        elif key == 260:
            if points[position] > 0:
                points[position] -= 1
                rem_points += 1
        elif key == 261:
            if points[position] < 10 and rem_points:
                points[position] += 1
                rem_points -= 1
        elif key == ord('\n'):
            if not rem_points:
                break
            else:
                stdscr.addstr(1, 0, "Remaining points", curses.A_REVERSE)
        player = Player(points[0],points[1],points[2],points[3],points[4])
    return player
                

def main():
    stdscr = curses.initscr()
    stdscr.keypad(True)
    curses.noecho()
    curses.curs_set(0)

    player = player_creator(stdscr)
    end_safe(0)

    
if __name__ == "__main__":
    main()