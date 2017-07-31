#!/usr/bin/env python

"""
Lists Unicode characters page by page. Scroll with left/right keys.
"""

import curses
from curses import wrapper
import time
import sys

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)


def draw_ascii(stdscr, page=0):
    
    height,width = stdscr.getmaxyx()
    
    # Menu
    menutext = "{l}(Left Arrow){pad}You are viewing page {page:03d}. Quit (q){pad}(Right Arrow){r}"
    menu_padding = int((width - len(menutext)+15)/2)
    stdscr.addstr(height-2,0, "{0}".format(width*chr(9552)))
    stdscr.addstr(height-1 ,2, menutext.format(l=chr(10096), page=page, r=chr(10097), pad=menu_padding*" "))

    padding = 8
    
    amount = int(int(width/8) * (height-2))
    
    char_columns = int(width /8)
    char_rows = height - 2
    
    for char_column in range(char_columns):
        for char_row in range(char_rows):
            char_num = (page*amount)+(char_column*char_rows) + char_row
            ascii_fmt = "{0:04d} {1:2s}".format(char_num, chr(char_num))
            stdscr.addstr(char_row, char_column*padding, ascii_fmt)


def main(stdscr):

    stdscr.clear()
    
    page = 0
    draw_ascii(stdscr, page)
    stdscr.refresh()
    
    while True:
        c = stdscr.getch()
        if c == ord('n') or c == curses.KEY_RIGHT:
            page +=1
        elif c == ord('p') or c == curses.KEY_LEFT:
            if page > 0:
                page -=1
        elif c == curses.KEY_ENTER or c == ord('q'):
            sys.exit(1)
        draw_ascii(stdscr, page)
        stdscr.refresh()

if __name__ == "__main__":
    wrapper(main)
