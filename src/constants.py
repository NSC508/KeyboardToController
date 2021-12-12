'''All constants used throughout the codebase'''
from pynput import keyboard, mouse
import pyvjoy

QUIT_KEY = keyboard.Key.esc
MAX_VJOY = 32767
JOYSTICK = pyvjoy.VJoyDevice(1)

FORWARD_KEY = keyboard.KeyCode.from_char('w')
LEFT_KEY = keyboard.KeyCode.from_char('a')
DOWN_KEY = keyboard.KeyCode.from_char('s')
RIGHT_KEY = keyboard.KeyCode.from_char('d')
LEFT_STICK_BUTTONS = {
    FORWARD_KEY: [0, 1, 0, 0],
    DOWN_KEY: [0, -1, 0, 0],
    LEFT_KEY: [-1, 0, 0, 0],
    RIGHT_KEY: [1, 0, 0, 0]
}
LEFT_TRIGGER = mouse.Button.right
RIGHT_TRIGGER = mouse.Button.left
TRIGGERS = {
    LEFT_TRIGGER: 1,
    RIGHT_TRIGGER: 2
}
DPAD_UP = keyboard.Key.up
DPAD_DOWN = keyboard.Key.down
DPAD_RIGHT = keyboard.Key.right
DPAD_LEFT = keyboard.Key.left
DPAD = {
    DPAD_UP: 3,
    DPAD_DOWN: 4,
    DPAD_RIGHT: 5,
    DPAD_LEFT: 6
}
