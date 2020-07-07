import sys
import wx  # pip install wxPython
from pyautogui import hotkey  # pip install PyAutoGUI
from pynput.keyboard import Key, Controller as KeyboardController  # pip install pynput

keyboard = KeyboardController()


def scale(key):
    first_key = Key.ctrl

    if "darwin" in sys.platform:
        first_key = Key.cmd

    try:
        keyboard.press(first_key)
        keyboard.press(key)
    finally:
        keyboard.release(first_key)
        keyboard.release(key)


def swipe(key):
    # app = wx.App(False)
    # width, height = wx.GetDisplaySize()

    # width = int(width / 2)
    # height = int(height / 2)

    os_type = sys.platform

    if "darwin" in os_type:
        hotkey('ctrl', key)
    elif "win" in os_type:
        hotkey('win', 'ctrl', key)

    # click(width, height)


def minimize():
    os_type = sys.platform

    if "darwin" in os_type:
        hotkey('command', 'm')
    elif "win" in os_type:
        hotkey('alt', 'space', 'n')

# scale('+')
# scale('-')
# minimize()
# swipe('right')
# swipe('left')
