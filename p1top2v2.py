import pyautogui
from inputs import get_gamepad

pyautogui.PAUSE = 0

def p1top2():
    while True:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            # direction vers le bas
            if event.code == 'ABS_HAT0Y' and event.state == 1:
                pyautogui.keyDown('s')
            else:
                pyautogui.keyUp('s')
            # direction vers le haut
            if event.code == 'ABS_HAT0Y' and event.state == int(-1):
                pyautogui.keyDown('z')
            else:
                pyautogui.keyUp('z')
            # direction vers la gauche
            if event.code == 'ABS_HAT0X' and event.state == int(-1):
                pyautogui.keyDown('q')
            else:
                pyautogui.keyUp('q')
            # direction vers la droite
            if event.code == 'ABS_HAT0X' and event.state == int(1):
                pyautogui.keyDown('d')
            else:
                pyautogui.keyUp('d')


p1top2()