import pyautogui



def crouchBlock():
    while True:
        pyautogui.keyDown('s')
        pyautogui.keyDown('q')


crouchBlock()