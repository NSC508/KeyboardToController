'''All constants used throughout the codebase'''
from pynput import keyboard
import pyvjoy

QUIT_KEY = keyboard.Key.esc
MAX_VJOY = 32767
JOYSTICK = pyvjoy.VJoyDevice(1)
