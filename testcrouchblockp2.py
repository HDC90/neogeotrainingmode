import pyautogui



def crouchBlock():
    while True:
        pyautogui.keyDown('s')
        pyautogui.keyDown('d')


crouchBlock()