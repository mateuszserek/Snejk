import curses
from snake import Snake
from apple import Apple 

def main(stdscr):
    stdscr.timeout(1000)
    stdscr.clear()
    stdscr.addstr(5, 5, "Snake Game! Press any key to start")
    stdscr.getch()
    stdscr.clear()

    player = Snake()
    apple = Apple()

    while True:
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
    stdscr.addstr(5, 5, f"Game OVER, Apples eaten: {apple.eaten_apple}")
    stdscr.getch()


curses.wrapper(main)
