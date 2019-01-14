import pyautogui
import keyboard
import time
from inputs import get_gamepad

pyautogui.PAUSE = 0


# Passage joueur 2
def p1_to_p2():
    while True:
        events = get_gamepad()
        for event in events:
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


# Module record
def dummy_record():
    while True:
        for event in get_gamepad():
            if event.code == 'button_record' and event.state == int(1):
                print('Dummy record')
                recorded = keyboard.record(until='button_record')
        if event.code == 'button_play' and event.state == int(1):
            print('Dummy replay in 3 seconds')
            time.sleep(3)
            keyboard.play(recorded)
            print('fin du replay')


# Lancement outil
while True:
    for event in get_gamepad():
        if event.code == 'BTN_TR' and event.state == int(1):
            print('P2 START')
            p1_to_p2()
            dummy_record()