from pynput import keyboard, mouse
import pyvjoy
from constants import QUIT_KEY, MAX_VJOY, JOYSTICK


def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    # print('Key released: {0}'.format(
    #     key))
    if key == QUIT_KEY:
        # Stop listener
        return False

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

def play_function(x, y, z, x_rot):
    '''Takes in t'''
    JOYSTICK.data.wAxisX = int(x * MAX_VJOY)
    JOYSTICK.data.wAxisY = int(y * MAX_VJOY)
    JOYSTICK.data.wAxisZ = int(z * MAX_VJOY)
    JOYSTICK.data.wAxisXRot = int(x_rot * MAX_VJOY)
    JOYSTICK.update()
