'''All miscellaneouss methods that don't require their own files'''
from constants import *

left_stick_pressed = set()

def on_press(key):
    '''Defines gamepad behavior on key press'''
    print(f'You pressed {key}')
    if key in LEFT_STICK_BUTTONS:
        left_stick_pressed.add(key)
    left_stick_value_calculator()

def left_stick_value_calculator():
    '''From all the keys pressed, calculates the correct mappings of the left stick'''
    sum_left_stick_directions = [0, 0, 0, 0]
    for key_pressed in left_stick_pressed:
        sum_left_stick_directions = [x + y for x, y in zip(
            sum_left_stick_directions, LEFT_STICK_BUTTONS[key_pressed]
            )]
    for index, value in enumerate(sum_left_stick_directions):
        if value == 0:
            sum_left_stick_directions[index] = 1/2
        elif value == -1:
            sum_left_stick_directions[index] = 0
    play_function(
        sum_left_stick_directions[0],
        sum_left_stick_directions[1],
        sum_left_stick_directions[2],
        sum_left_stick_directions[3])

def on_release(key):
    '''Defines gamepad behavior on key release'''
    if key in LEFT_STICK_BUTTONS:
        left_stick_pressed.remove(key)
    left_stick_value_calculator()
    if key == QUIT_KEY:
        # Stop listener
        return False

def on_move(x_val, y_val):
    '''Defines gamepad behavior on mouse movement'''
    print('Pointer moved to {0}'.format(
        (x_val, y_val)))

def on_click(*args):
    '''Defines gamepad behavior on mouse click'''
    if args[-2] in TRIGGERS:
        trigger = TRIGGERS[args[-2]]
        if args[-1]:
            JOYSTICK.set_button(trigger, 1)
        elif not args[-1]:
            JOYSTICK.set_button(trigger, 0)

def on_scroll(*args):
    '''Defines gampad behavior when mouse is scrolled'''

def play_function(x_val, y_val, z_val, x_rot):
    '''Sets gamepad to the given values'''
    JOYSTICK.data.wAxisX = int(x_val * MAX_VJOY)
    JOYSTICK.data.wAxisY = int(y_val * MAX_VJOY)
    JOYSTICK.data.wAxisZ = int(z_val * MAX_VJOY)
    JOYSTICK.data.wAxisXRot = int(x_rot * MAX_VJOY)
    JOYSTICK.update()
