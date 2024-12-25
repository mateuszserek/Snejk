import curses
from operations import *
import config
import pygame.mixer

def main(stdscr):
    # # curses.start_color()
    # # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Green background

    # # Set background character and color
    # # stdscr.bkgd(' ', curses.color_pair(1))  # Space character with color pair 1
    # # stdscr.clear()

    # # Refresh to apply changes
    # generate_screen_border(stdscr)
    #stdscr.refresh()
    pygame.mixer.init()
    y, x = stdscr.getmaxyx()
    config.screen_y_size = y - 1
    config.screen_x_size = x - 1
    start(stdscr)
    game(stdscr)
    end(stdscr)


curses.wrapper(main)
