# Project-6 WPM typing test terminal based application
# it is a simple project where the user is given a text to type and the user's wpm is displayed dynamically on the terminal
# the keyboard values representations
# rewriting the wpm project once more just to see the working of the project
import curses
import random
import time
from curses import wrapper

import pyfiglet


# let's write the code from scratch
# in this function we will write the code for the overlaying text functionality and the print the wpm dynamically
def overlaying_text(stdscr, text_art, current, test, wpm=0):
    stdscr.addstr(text_art, curses.color_pair(3))
    stdscr.addstr(10, 0, test)
    stdscr.addstr(11, 1, f"WPM: {wpm}", curses.color_pair(4))
    for i, char in enumerate(current):
        if current[i] == test[i]:
            stdscr.addstr(10, i, char, curses.color_pair(2))
        else:
            if char == ' ':  # i have added this to the error coloration to indicate wrongful pos use of space
                stdscr.addstr(10, i, char, curses.color_pair(3) | curses.A_REVERSE)
            else:
                stdscr.addstr(10, i, char, curses.color_pair(3))


def random_text():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
    return random.choice(lines).strip()


def wpm_test(stdscr):
    #     in this function we will actually start the typing test
    text_art = pyfiglet.figlet_format("Start Typing!!", width=150, justify="center")
    test_text = random_text()
    # test_list = list(test_text)
    # now here we will continuously add the current text over the test_text and show a seamless typing test
    current_text = []  # this will store the current typed text by the user
    cursor_pos = 0  # this will store the x-cursor position
    wpm = 0
    stdscr.nodelay(True)
    start_time = time.time()  # it marks the initial time
    while True:
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (elapsed_time / 60)) / 5)  # this calculates the wpm
        stdscr.clear()
        overlaying_text(stdscr, text_art, current_text, test_text, wpm)
        stdscr.refresh()
        stdscr.move(10, cursor_pos)
        try:
            key = stdscr.getkey()
        except:
            continue
        # this part ensures that when the users ends up correctly typing the text
        # it ends the game and asks the user if it wants to play again in the main function.
        if "".join(current_text) == test_text:
            stdscr.nodelay(False)
            break

        if key == '\x1b':  # Escape key (ESC)
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if cursor_pos > 0:
                cursor_pos -= 1  # Move cursor back
                current_text[cursor_pos] = ''  # Remove character at cursor position

        elif key == 'KEY_LEFT':
            if cursor_pos > 0:
                cursor_pos -= 1  # Move cursor left

        elif key == 'KEY_RIGHT':
            if cursor_pos < len(current_text):
                cursor_pos += 1  # Move cursor right
        else:
            if cursor_pos == len(current_text) and len(current_text) < len(test_text):
                current_text.insert(cursor_pos, key)
            else:
                current_text[cursor_pos] = key
            cursor_pos += 1


def start_screen(stdscr):
    #     in this function we will define the starting of the program
    result = pyfiglet.figlet_format(" Typing Speed Test ", width=150, justify='center', direction='left-to-right')
    stdscr.clear()
    stdscr.addstr(result, curses.color_pair(4))
    stdscr.addstr(10, 30, 'Press any key to begin ')
    stdscr.refresh()
    stdscr.getkey()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(12, 0, "You have completed the text. Press any key to play again (esc-quit) ")
        key = stdscr.getkey()

        if key == '\x1b':  # Escape key (ESC)
            break


wrapper(main)
