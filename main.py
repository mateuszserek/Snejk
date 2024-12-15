import curses
from operations import *

def main(stdscr):
    start(stdscr)
    game(stdscr)
    end(stdscr)


curses.wrapper(main)
