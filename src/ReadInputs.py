from pynput import keyboard, mouse
from utils.py import on_press, on_release, on_move, on_click, on_scroll

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
