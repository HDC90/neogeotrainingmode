import pyautogui
from inputs import get_gamepad

pyautogui.PAUSE = 0

def p1top2():
    while True:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
            # direction vers le bas
            if event.code == 'ABS_HAT0Y' and event.state == 0:
                pyautogui.keyDown('s')
                pyautogui.press('s')
                pyautogui.keyUp('s')
            # direction vers le haut
            if event.code == 'ABS_HAT0Y' and event.state == int(-1):
                pyautogui.keyDown('z')
                pyautogui.keyUp('z')
            # direction vers la gauche
            if event.code == 'ABS_HAT0X' and event.state == int(-1):
                pyautogui.keyDown('q')
                pyautogui.keyUp('q')
            # direction vers la droite
            if event.code == 'ABS_HAT0X' and event.state == int(1):
                pyautogui.keyDown('d')
                pyautogui.keyUp('d')
            # bouton A
            if event.code == 'BTN_WEST' and event.state == int(1):
                pyautogui.keyDown('i')
                pyautogui.keyUp('i')
            # bouton B
            if event.code == 'BTN_SOUTH' and event.state == int(1):
                pyautogui.keyDown('k')
                pyautogui.keyUp('k')
            # bouton A
            if event.code == 'BTN_NORTH' and event.state == int(1):
                pyautogui.keyDown('o')
                pyautogui.keyUp('o')
            # bouton A
            if event.code == 'BTN_EAST' and event.state == int(1):
                pyautogui.keyDown('l')
                pyautogui.keyUp('l')
p1top2()