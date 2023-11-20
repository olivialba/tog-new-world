from pynput.mouse._win32 import Button, Controller
import pyautogui
import time, cv2

mouse = Controller()
    
def detect_button(region, selection, start_time):
    '''
    Detects buttons on the phone window to continue advancing; has 5 seconds interval.
    
    Can also handles level up, unlocks, and advancing a floor.
    '''
    elapsed_time = getElapsedTime(start_time)
    if elapsed_time > 400:
        return 'ERROR'
    for name, img in selection.items():
        try:
            button = pyautogui.locateOnScreen(img, confidence=0.8, region=region)
            if button: 
                print(f'{name} found!')
                clickCenter(button)
                return True
        except:
            return False
    return False


def clickCenter(button):
    '''
    Move the mouse to the center of a box and clicks it.
    '''
    X = button.left + (button.width / 2)
    Y = button.top + (button.height / 2)
    dx = (X - mouse.position[0])
    dy = (Y - mouse.position[1])
    mouse.move(dx, dy)
    time.sleep(0.25)
    mouse.click(Button.left)


def getElapsedTime(start_time):
    '''
    Get the timer's elapsed time.
    '''
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time   