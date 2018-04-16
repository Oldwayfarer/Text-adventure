#!/usr/bin/env python3

import curses
import json
from PIL import Image
from image_to_ASCII import processer
from image_to_ASCII import end_safe
from image_to_ASCII import default_ascii_dict
from time import sleep
import enemy


class Player:
    def __init__(self, stren, intel, agil, atten, charis):
        self.stren = stren
        self.intel = intel
        self.agil = agil
        self.atten = atten
        self.charis = charis
        self.money = 15
        self.inventory = {}

def choice(message, speach, shift, stdscr):
    choice = 0
    for i in range(0, len(message)):
        stdscr.addstr(shift+i, 0, message[i])
    shift = shift + len(message) + 1
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
            stdscr.clear()
            stdscr.refresh()
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
        player = Player(points[0], points[1], points[2], points[3], points[4])
    stdscr.clear()
    return player
                

def main():
    stdscr = curses.initscr()
    stdscr.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    try:
        logo = Image.open('./Image_Folder/logo.jpg')
    except FileNotFoundError:
        end_safe(0)
        print("Na-Na-Na-Na-Na")
    width, height = logo.size

    frame = processer(logo.load(), stdscr, width, height, 100, default_ascii_dict, 0, 1)
    stdscr.addstr(0, 0, "Press any key to continue")
    if len(frame[0]) > curses.COLS-1:
        visible_cols = curses.COLS
    else:
        visible_cols = len(frame[0])
    if len(frame) > curses.LINES - 3:
        visible_lines = curses.LINES - 2
    else:
        visible_lines = len(frame)
    for i in range(0, visible_lines):
        add = frame[i][0:visible_cols]
        stdscr.addstr(i+1, 0, add)
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()
    #small demonstration of capability
    message = [
        'You are on the beginning of the greates adventure in your life!',
        'All you was dreaming about is now just behind this old massive door.',
        'But at that moment you started to turn over the key inside the lock',
        'you felt a little chill inside you. Does it really worth it...All',
        'this place looks crippy'
        'Do you want to proceed? '
    ]

    speach = [
        'Hell! It\'s not a time for a doubts!(Enter the door)',
        'Well. That\'s all seems like a greate mistake. I\'d better leave'
    ]  
    player = player_creator(stdscr)
    res = choice(message, speach, 20, stdscr)
    stdscr.clear()
    if res == 0:
        message = [
            'You got into the big hall of ancient castle. Spellboud by it\'s splendor',
            'you have not noticed the small horny creature sneaking behind. It was to',
            'late when it\'s narrow long tail enveloped your neck and cnocked over you.',
            'Before you managed do get up the creature rushed over toward your face and ',
            'And paralised your mind with some sort of a magic coming out of his horns',
            'It\'s delving inside your head. It want\'s to know who you are...'
        ]
        speach =[
            'Try to resist. GET OUT OFF MY MIND!',
            'Try to get over the paralysis and take off the creature.',
            'Let the creature do what it wants'
        ]
        res = choice(message, speach, 20, stdscr)
        if res == 0 and player.intel > 8:
            message = [
                'The creature loose in the mind battle and runaway! It\'s no doubght you have a strong mind'
            ]
            speach = [
                'perfect!'
            ]
            choice(message, speach, 20, stdscr)
        elif res == 1 and player.stren > 7:
            message = [
                'You have managed to get it of your face! Creature astonishedly pent and disappiar in the darkness'
            ]
            speach = [
                'Nice try!'
            ]
            choice(message, speach, 20, stdscr)
        elif res == 2:
            message = [
                'Having satisfied its interest creature leaves. For some time you lay on the ground in full perplexity'
            ]

            speach = [
                'Everything mixed up in my head'
            ]
            choice(message, speach, 20, stdscr)
        else:
            message = [
                'You have not managed to bit the creature'
            ]

            speach = [
                'How can this happen...'
            ]
            choice(message, speach, 20, stdscr)
    if res == 1:
        message = [
            'You have left this place and will never know what secrets it keeps'
        ]

        speach = [
            'But i will be allive'
        ]
        choice(message, speach, 20, stdscr)
    end_safe(0)

    
if __name__ == "__main__":
    main()