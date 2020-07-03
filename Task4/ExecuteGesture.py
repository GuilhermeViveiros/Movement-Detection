import sys
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController, Listener

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
        try:
            keyboard.press(Key.ctrl)
            keyboard.press(key)
        finally:
            keyboard.release(Key.ctrl)
            keyboard.release(key)

    if sys.platform == "win32":
        try:
            keyboard.press(Key.cmd)
            keyboard.press(Key.ctrl)
            keyboard.press(key)
        finally:
            keyboard.release(Key.cmd)
            keyboard.release(Key.ctrl)
            keyboard.release(key)


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


def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    if key == Key.esc:
        # Stop Listenning for Keys
        return False
    elif key == KeyCode.from_char("q"):
        scale('-')
    elif key == KeyCode.from_char("w"):
        scale('+')
    elif key == KeyCode.from_char("a"):
        swipe(Key.left)
    elif key == KeyCode.from_char("s"):
        swipe(Key.right)
    elif key == Key.ctrl_r:
        minimize()


os_type = sys.platform

print(os_type)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

