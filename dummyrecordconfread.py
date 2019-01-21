#! python3

import pyautogui
import keyboard
import time
import configparser as cp
from inputs import get_gamepad
pyautogui.PAUSE = 0

# Lecture fichier de conf
config = cp.ConfigParser()
config.read('neomapconf.ini')
record = config.get('record controls', 'record')
stop = config.get('record controls', 'stop')
play = config.get('record controls', 'play')


# Fonction record
def dummy_record():
    while True:
        for event in get_gamepad():
            try:
                if event.code == record and event.state == int(1):
                    print('Enregistrement P2')
                    print("Presser la touche 'a' pour quitter l'enregistrement")
                    recorded = keyboard.record(until=stop)
                    print('Enregistrement terminé')
                elif event.code == play and event.state == int(255):
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