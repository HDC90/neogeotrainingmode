import PySimpleGUI as sg
import subprocess


def ExecuteCommandSubprocess(command, *args):
    try:
        sp = subprocess.Popen([command, *args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        pass


layout = [
    [sg.Text('THE CHALLENGER', size=(35, 1), background_color='#ffffff', justification='center')],
    [sg.Output(size=(40, 30))],
    [sg.Text('Action', size=(5, 1), background_color='#ffffff'), sg.InputCombo(['Human', 'Jump', 'Crouch']),
     sg.Text('Guard', size=(5, 1), background_color='#ffffff'), sg.InputCombo(['No Guard', 'Guard-P1', 'Guard-P2'])],
    [sg.Button('Training', size=(10, 1)), sg.Button('Test', size=(10, 1)), sg.Button('EXIT', size=(10, 1))]
]

window = sg.Window('NEO GEO TRAINING TOOL', background_color='#ffffff', button_color=('white', '#2c2c2c'), border_depth=None, keep_on_top=True).Layout(layout)


while True:
    (event, value) = window.Read()
    if event == 'EXIT' or event is None:
        break  # exit button clicked
    if event == 'Training':
        ExecuteCommandSubprocess('run.bat')
    elif event == 'Test':
        ExecuteCommandSubprocess('testinput.bat')