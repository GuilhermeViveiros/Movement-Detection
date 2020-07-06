import sys
import wx #pip install wxPython
from pyautogui import hotkey #pip install PyAutoGUI
from pynput.keyboard import Key, Controller as KeyboardController #pip install pynput
from pynput.mouse import Controller as MouseController #pip install pynput


keyboard = KeyboardController()
mouse = MouseController()


def scale(key):
    first_key = Key.ctrl

    if sys.platform == "darwin":
        first_key = Key.cmd

    try:
        keyboard.press(first_key)
        keyboard.press(key)
    finally:
        keyboard.release(first_key)
        keyboard.release(key)


def swipe(key):
    app = wx.App(False)
    width, height = wx.GetDisplaySize()
    
    width = int(width/2)
    height = int(height/2)
    
    if sys.platform == "darwin":
        hotkey('ctrl', key)
        mouse.position = (width, height)

    elif sys.platform == "win32":
        win_key = Key.right

        if key == 'left':
            win_key = Key.left
        
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

    elif sys.platform == "win32":
        keyboard.press(Key.alt)
        keyboard.press(Key.space)

        keyboard.release(Key.alt)
        keyboard.release(Key.space)

        keyboard.press('n')
        keyboard.release('n')


os_type = sys.platform

# scale('+')
# scale('-')
# minimize()
# swipe('right')
# swipe('left')
