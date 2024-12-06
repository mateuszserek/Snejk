import curses
from snake import Snake

def main(stdscr):
    stdscr.timeout(1000)
    stdscr.clear()
    stdscr.addstr(5, 5, "Snake Game! Press any key to start")
    stdscr.getch()
    stdscr.clear()
    player = Snake()

    while True:
        for i in player.position_before_head:
            stdscr.addstr(i[1], i[0], "D")
        stdscr.addstr(player.head[1], player.head[0], "D")
        
        stdscr.refresh()

        player.next_direction(stdscr.getch())
        player.move()
        stdscr.clear()



curses.wrapper(main)
