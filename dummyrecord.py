import keyboard, time
from inputs import get_gamepad


def dummy_record():
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == 'button_record' and event.state == int(1):
                print('Dummy record')
                recorded = keyboard.record(until='button_record')
        if event.code == 'button_play' and event.state == int(1):
            print('Dummy play in 3 seconds')
            time.sleep(3)
            keyboard.play(recorded)


dummy_record()