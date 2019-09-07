# https://docs.python.org/3/howto/curses.html
import curses

# wrapper used to restore window after crash
main_wrapper = curses.wrapper


def init_engine(main_window):
    curses.noecho()  # disable direct typing to screen
    curses.cbreak()  # turn off buffered mode
    main_window.keypad(True)  # enable special keycode like arrow keys etc.

    return main_window


def kill_engine(main_window):
    # undo changes to terminal
    curses.echo()
    curses.nocbreak()
    main_window.keypad(False)

    curses.endwin()


"""
Display Popup in the center of the screen
"""
def display_popup(msg, height, width):
    print(msg)


def run_test(main_window):
    main_window.clear()

    main_window.addstr(0, 0, "THIS IS A TEST! :D")

    main_window.refresh()
    main_window.getkey()

    kill_engine(main_window)


if __name__ == '__main__':
    curses.wrapper(run_test)
