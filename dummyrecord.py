#! python3

import pyautogui
import keyboard
import time
from inputs import get_gamepad
pyautogui.PAUSE = 0


def dummy_record():
    while True:
        for event in get_gamepad():
            try:
                if event.code == 'BTN_TL' and event.state == int(1):
                    print('Dummy record')
                    recorded = keyboard.record(until='p')
                    print('record ended')
                elif event.code == 'ABS_Z' and event.state == int(255):
                    print('Dummy replay in 3 seconds')
                    time.sleep(3)
                    keyboard.play(recorded)
                    print('fin du replay')
            except:
                print("oups rien d'enregitreé")
                pass

dummy_record()