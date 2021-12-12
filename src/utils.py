'''All miscellaneouss methods that don't require their own files'''
from constants import *


def on_press(key):
    '''Defines gamepad behavior on key press'''
    print(f'You pressed {key}')
    if key == FORWARD_KEY:
        play_function(1/2, 1, 1/2, 1/2)
    if key == DOWN_KEY:
        play_function(1/2, 0, 1/2, 1/2)
    if key == LEFT_KEY:
        play_function(0, 1/2, 1/2, 1/2)
    if key == RIGHT_KEY:
        play_function(1, 1/2, 1/2, 1/2)


def on_release(key):
    '''Defines gamepad behavior on key release'''
    play_function(1/2, 1/2, 1/2, 1/2)
    if key == QUIT_KEY:
        # Stop listener
        return False

def on_move(x_val, y_val):
    '''Defines gamepad behavior on mouse movement'''
    print('Pointer moved to {0}'.format(
        (x_val, y_val)))

def on_click(x_val, y_val, button, pressed):
    '''Defines gamepad behavior on mouse click'''
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x_val, y_val)))

def on_scroll(x_val, y_val, change_in_x, change_in_y):
    '''Defines gampad behavior when mouse is scrolled'''
    print('Scrolled {0} at {1}'.format(
        'down' if change_in_y < 0 else 'up',
        (x_val, y_val)))

def play_function(x_val, y_val, z_val, x_rot):
    '''Sets gamepad to the given values'''
    JOYSTICK.data.wAxisX = int(x_val * MAX_VJOY)
    JOYSTICK.data.wAxisY = int(y_val * MAX_VJOY)
    JOYSTICK.data.wAxisZ = int(z_val * MAX_VJOY)
    JOYSTICK.data.wAxisXRot = int(x_rot * MAX_VJOY)
    JOYSTICK.update()
