import pyautogui
from inputs import get_gamepad

pyautogui.PAUSE = 0


def p1top2():
    while True:
        events = get_gamepad()
        for event in events:
            # print(event.ev_type, event.code, event.state)
            # direction vers le bas
            if event.code == 'ABS_HAT0Y':
                if event.state == 1:
                    print('Crouch!')
                    pyautogui.keyDown('s')
                elif event.state == 0:
                    pyautogui.keyUp('s')
            # direction vers le haut
            if event.code == 'ABS_HAT0Y':
                if event.state == int(-1):
                    print('Jump!')
                    pyautogui.keyDown('z')
                elif event.state == int(0):
                    pyautogui.keyUp('z')
            # direction vers la gauche
            if event.code == 'ABS_HAT0X':
                if event.state == int(-1):
                    print('Gauche!')
                    pyautogui.keyDown('q')
                elif event.state == int(0):
                    pyautogui.keyUp('q')
            # direction vers la droite
            if event.code == 'ABS_HAT0X':
                if event.state == int(1):
                    print('Droite!')
                    pyautogui.keyDown('d')
                elif event.state == int(0):
                    pyautogui.keyUp('d')
            # bouton A
            if event.code == 'BTN_WEST':
                if event.state == int(1):
                    print('A!')
                    pyautogui.keyDown('i')
                elif event.state == int(0):
                    pyautogui.keyUp('i')
            # bouton B
            if event.code == 'BTN_SOUTH':
                if event.state == int(1):
                    print('B!')
                    pyautogui.keyDown('k')
                elif event.state == int(0):
                    pyautogui.keyUp('k')
            # bouton C
            if event.code == 'BTN_NORTH':
                if event.state == int(1):
                    print('C!')
                    pyautogui.keyDown('o')
                elif event.state == int(0):
                    pyautogui.keyUp('o')
            # bouton D
            if event.code == 'BTN_EAST':
                if event.state == int(1):
                    print('D!')
                    pyautogui.keyDown('l')
                elif event.state == int(0):
                    pyautogui.keyUp('l')
        # stop p1 vers p2
        if event.code == 'BTN_TR' and event.state == int(1):
            print('P2 STOP')
            # reset positions
            pyautogui.keyUp('z')
            pyautogui.keyUp('q')
            pyautogui.keyUp('s')
            pyautogui.keyUp('d')
            break


while True:
    for event in get_gamepad():
        if event.code == 'BTN_TR' and event.state == int(1):
            print('P2 START')
            p1top2()