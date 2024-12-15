import time 
from config import *
from apple import Apple
from snake import Snake

player = Snake()
apple = Apple()

def generate_screen_border(stdscr) -> None:
    for i in range(screen_y_size + 1):
        stdscr.addstr(i, 0, "|")
        stdscr.addstr(i, screen_x_size, "|")
    for i in range(screen_x_size + 1):
        stdscr.addstr(0, i, "-")
        stdscr.addstr(screen_y_size, i, "-")

def start(stdscr):
    stdscr.clear()
    stdscr.addstr(screen_y_size // 2, screen_x_size // 2, "Snake Game! Press any key to start")
    stdscr.getch()
    stdscr.clear()
    stdscr.timeout(1000)

def end(stdscr):
    stdscr.refresh()
    stdscr.clear()
    stdscr.addstr(screen_y_size // 2, screen_x_size // 2, f"Game OVER, Apples eaten: {apple.counter}")
    time.sleep(0.4)
    stdscr.getch()

def game(stdscr):
    while True:

        if player.check_screen_collision() or player.check_self_collision():
            break 
            
        stdscr.refresh()

        player.next_direction(stdscr.getch())
        is_eaten = player.check_if_apple_is_eaten(apple)

        if is_eaten:
            apple.eaten_apple()

        player.move(is_eaten)
        stdscr.clear()

        generate_screen_border(stdscr)
        stdscr.addstr(apple.position[1], apple.position[0], apple_icon)

        for i in player.position_before_head:
            stdscr.addstr(i[1], i[0], snake_before_head_str)
        stdscr.addstr(player.head[1], player.head[0], snake_head)