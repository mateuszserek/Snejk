import time 
import config
from apple import Apple
from snake import Snake
from curses import napms

player = Snake()
apple = Apple()

def middle_screen_location(text: str) -> int:
    return (config.screen_x_size // 2) - (len(text) // 2)

def generate_screen_border(stdscr) -> None:
    for i in range(config.game_screen_y_start + 1, config.screen_y_size):
        stdscr.addstr(i, config.game_screen_x_start, "|")
        stdscr.addstr(i, config.screen_x_size, "|")

    for i in range(config.game_screen_x_start, config.screen_x_size):
        stdscr.addstr(config.game_screen_y_start, i, "-")
        stdscr.addstr(config.screen_y_size, i, "-")

def generate_points(stdscr) -> None:
    stdscr.addstr(config.game_screen_y_start // 2, middle_screen_location(config.point_text), f"{config.point_text} {apple.counter}")

def get_game_screen_size() -> int: #do solidnego potestowania (wstepnie dziala)
    x = config.screen_x_size - config.game_screen_x_start - 1
    y = config.screen_y_size - config.game_screen_y_start - 1
    return (x * y) 

def check_game_over() -> bool: #do poprawy
    if len(player.position_before_head) + 1 >= get_game_screen_size():
        config.end_text = "GG WP"
        return True 
    else:
        return False
 
def start(stdscr):
    stdscr.clear()
    stdscr.addstr(config.screen_y_size // 2, middle_screen_location(config.start_text), config.start_text)
    stdscr.getch()
    stdscr.clear()
    stdscr.timeout(100)

def end(stdscr): #do poprawy zamykanie
    stdscr.refresh()
    stdscr.clear()
    stdscr.addstr(config.screen_y_size // 2, middle_screen_location(config.end_text), f"{config.end_text} {apple.counter}")
    stdscr.refresh()
    napms(500)
    stdscr.timeout(10000)
    stdscr.getch()

def game(stdscr):
    while True:

        if player.check_screen_collision() or player.check_self_collision() or check_game_over():
            break 
            
        stdscr.refresh()
        
        player.next_direction(stdscr.getch())
        is_eaten = player.check_if_apple_is_eaten(apple)

        if is_eaten:
            apple.eaten_apple()

        player.move(is_eaten)
        stdscr.clear()

        generate_screen_border(stdscr)
        generate_points(stdscr)
        stdscr.addstr(apple.position[1], apple.position[0], config.apple_icon)

        for i in player.position_before_head:
            stdscr.addstr(i[1], i[0], config.snake_before_head_str)
        stdscr.addstr(player.head[1], player.head[0], config.snake_head)