import sys
from pyautogui import hotkey
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
keyboard = KeyboardController()


def scale(key):
    if sys.platform == "darwin":
        first_key = Key.cmd

    if sys.platform == "win32":
        first_key = Key.ctrl

    try:
        keyboard.press(first_key)
        keyboard.press(key)
    finally:
        keyboard.release(first_key)
        keyboard.release(key)

def swipe(key):
    if sys.platform == "darwin":
        hotkey('ctrl', key)

    if sys.platform == "win32":
        if key == 'left':
            win_key = Key.left
        else:
            win_key = Key.right
        
        try:
            keyboard.press(Key.cmd)
            keyboard.press(Key.ctrl)
            keyboard.press(win_key)
        finally:
            keyboard.release(Key.cmd)
            keyboard.release(Key.ctrl)
            keyboard.release(win_key)


def minimize():
    if sys.platform == "darwin":
        keyboard.press(Key.cmd)
        keyboard.press('m')

        keyboard.release(Key.cmd)
        keyboard.release('m')

    if sys.platform == "win32":
        keyboard.press(Key.alt)
        keyboard.press(Key.space)

        keyboard.release(Key.alt)
        keyboard.release(Key.space)

        keyboard.press('n')
        keyboard.release('n')


os_type = sys.platform

#scale('+')
#scale('-')
#minimize()
#swipe(Key.right)
#swipe('right')
