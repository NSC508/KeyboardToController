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
A_BUTTON = keyboard.Key.space
B_BUTTON = keyboard.KeyCode.from_char('1')
X_BUTTON = keyboard.KeyCode.from_char('r')
Y_BUTTON = keyboard.KeyCode.from_char('q')
LEFT_STICK_BUTTON = keyboard.Key.shift_l
RIGHT_STICK_BUTTON = keyboard.Key.shift_r
RIGHT_BUMPER = keyboard.KeyCode.from_char('c')
LEFT_BUMPER = keyboard.KeyCode.from_char('z')
START = keyboard.KeyCode.from_char('y')
BACK = keyboard.KeyCode.from_char('t')
GUIDE = keyboard.KeyCode.from_char('u')
KEY_BINDINGS = {
    DPAD_UP: 3,
    DPAD_DOWN: 4,
    DPAD_RIGHT: 5,
    DPAD_LEFT: 6,
    A_BUTTON: 7,
    B_BUTTON: 8,
    X_BUTTON: 9,
    Y_BUTTON: 10,
    LEFT_STICK_BUTTON: 11,
    RIGHT_STICK_BUTTON: 12,
    RIGHT_BUMPER: 13,
    LEFT_BUMPER: 14,
    START: 15,
    BACK: 16,
    GUIDE: 17
}
