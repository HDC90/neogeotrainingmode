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
                    print('Enregistrement P2')
                    print("Presser la touche 'a' pour quitter l'enregistrement")
                    recorded = keyboard.record(until='a')
                    print('Enregistrement terminé')
                elif event.code == 'ABS_Z' and event.state == int(255):
                    print('Dummy replay in 3')
                    time.sleep(1)
                    print('2')
                    time.sleep(1)
                    print('1')
                    time.sleep(1)
                    keyboard.play(recorded)
                    print('fin du replay')
            except:
                print("oups rien d'enregitré")
                pass

dummy_record()