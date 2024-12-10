import curses
from snake import Snake
from apple import Apple 
import config

def generate_screen_border(stdscr) -> None:
    for i in range(config.screen_y_size + 1):
        stdscr.addstr(i, 0, "|")
        stdscr.addstr(i, config.screen_x_size, "|")
    for i in range(config.screen_x_size + 1):
        stdscr.addstr(0, i, "-")
        stdscr.addstr(config.screen_y_size, i, "-")

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(config.screen_y_size // 2, config.screen_x_size // 2, "Snake Game! Press any key to start")
    stdscr.getch()
    stdscr.clear()

    player = Snake()
    apple = Apple()
    stdscr.timeout(1000)
    while True:
        generate_screen_border(stdscr)
        stdscr.addstr(apple.position[1], apple.position[0], "A")

        for i in player.position_before_head:
            stdscr.addstr(i[1], i[0], "D")
        stdscr.addstr(player.head[1], player.head[0], "D")
        
        stdscr.refresh()

        player.next_direction(stdscr.getch())
        is_eaten = player.check_if_apple_is_eaten(apple)

        if is_eaten:
            apple.eaten_apple()

        if player.check_screen_collision() or player.check_self_collision():
            break 

        player.move(is_eaten)
        stdscr.clear()
        
    stdscr.refresh()
    stdscr.clear()
    stdscr.addstr(config.screen_y_size // 2, config.screen_x_size // 2, f"Game OVER, Apples eaten: {apple.counter}")
    stdscr.timeout(10000)
    stdscr.getch()


curses.wrapper(main)
print("test commit")
