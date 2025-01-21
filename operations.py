import config
from apple import Apple
from snake import Snake
from curses import napms
from functions import *

player = Snake()
apple = Apple()

def generate_screen_border(stdscr) -> None:
    for i in range(config.game_screen_y_start + 1, config.screen_y_size):
        stdscr.addstr(i, config.game_screen_x_start, "|")
        stdscr.addstr(i, config.screen_x_size, "|")

    for i in range(config.game_screen_x_start + 1, config.screen_x_size):
        stdscr.addstr(config.game_screen_y_start, i, "-")
        stdscr.addstr(config.screen_y_size, i, "-")

def generate_points(stdscr) -> None:
    stdscr.addstr(config.game_screen_y_start // 2, middle_screen_location(config.point_text), f"{config.point_text} {apple.counter}")

def check_game_over() -> bool: 
    if len(player.position_before_head) >= get_game_screen_size():
        config.end_text = config.end_win_text
        return True 
    else:
        return False
 
def start(stdscr):
    apple.create_all_position_list_and_first_position(player)
    stdscr.clear()
    stdscr.addstr(config.screen_y_size // 2, middle_screen_location(config.start_text), config.start_text)
    stdscr.getch()
    stdscr.clear()
    stdscr.timeout(config.game_tick_ms)

def end(stdscr):
    stdscr.refresh()
    stdscr.clear()
    stdscr.addstr(config.screen_y_size // 2, middle_screen_location(config.end_text), f"{config.end_text} {apple.counter}")
    stdscr.refresh()
    napms(1000)
    stdscr.timeout(10000)
    stdscr.getch()

def game(stdscr):
    while True:

        stdscr.timeout(config.game_tick_ms)
        
        if player.check_screen_collision() or player.check_self_collision() or check_game_over():
            play_music(config.game_over_sound)
            break 
            
        stdscr.refresh()
        
        player.next_direction(stdscr.getch())
        is_eaten = player.check_if_apple_is_eaten(apple)

        if is_eaten:
            apple.eaten_apple(player)

        player.move(is_eaten)
        stdscr.clear()

        generate_screen_border(stdscr)
        generate_points(stdscr)
        stdscr.addstr(apple.position[1], apple.position[0], config.apple_icon)

        for i in player.position_before_head:
            stdscr.addstr(i[1], i[0], config.snake_before_head_str)
        stdscr.addstr(player.head[1], player.head[0], config.snake_head)