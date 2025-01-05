import curses
from operations import *
import config
import pygame.mixer

def main(stdscr):
    pygame.mixer.init()
    y, x = stdscr.getmaxyx()
    config.screen_y_size = y - 1
    config.screen_x_size = x - 1
    start(stdscr)
    game(stdscr)
    end(stdscr)


curses.wrapper(main)
