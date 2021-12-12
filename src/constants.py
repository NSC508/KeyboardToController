'''All constants used throughout the codebase'''
from pynput import keyboard
import pyvjoy

QUIT_KEY = keyboard.Key.esc
MAX_VJOY = 32767
JOYSTICK = pyvjoy.VJoyDevice(1)
FORWARD_KEY = keyboard.KeyCode.from_char('w')
LEFT_KEY = keyboard.KeyCode.from_char('a')
DOWN_KEY = keyboard.KeyCode.from_char('s')
RIGHT_KEY = keyboard.KeyCode.from_char('d')
