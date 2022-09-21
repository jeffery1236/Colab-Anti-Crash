import pyautogui
import time
from datetime import datetime

from typing import Tuple

def get_clicking_pos() -> Tuple[float, float]:
    print('Type Y, move cursor to clicking position and press enter')
    _ = input()

    mouse_x, mouse_y = pyautogui.position()
    return mouse_x, mouse_y


print('Enter interval between clicks(sec): ')
interval_sec = float(input())
print('Enter number of clicks(int): ')
num_clicks = int(input())

mouse_x, mouse_y = get_clicking_pos()


for i in range(num_clicks):
    print(f'Clicking at {mouse_x, mouse_y}, {datetime.now()}')
    pyautogui.click(x=mouse_x, y=mouse_y,
                    clicks=1, button='left')

    time.sleep(interval_sec)
