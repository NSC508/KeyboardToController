from pynput import keyboard, mouse

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
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    pass

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

# Collect events until released
key_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
key_listener.start()
    
with mouse.Listener(on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    try:
        listener.join()
    except e:
        print('Done'.format(e.args[0]))
