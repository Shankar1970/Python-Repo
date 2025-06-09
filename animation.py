import curses
import time

def animate_name(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.nodelay(True)  # Make getch() non-blocking
    stdscr.timeout(100)  # Set refresh speed

    height, width = stdscr.getmaxyx()
    name = "YourName"
    x = 0
    direction = 1  # Moving direction: 1 for right, -1 for left

    while True:
        stdscr.clear()
        stdscr.addstr(height // 2, x, name)
        stdscr.refresh()

        x += direction
        if x + len(name) >= width or x <= 0:
            direction *= -1  # Reverse direction

        time.sleep(0.1)

        key = stdscr.getch()
        if key == ord('q'):
            break  # Exit when 'q' is pressed

curses.wrapper(animate_name)