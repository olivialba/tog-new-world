from pynput.mouse import Button, Controller
import pyautogui
import time

mouse = Controller()
start_time = 0
    
def detect_button(region, selection):
    '''
    Detects buttons on the phone window to continue advancing; has 5 seconds interval.
    
    Can also handles level up, unlocks, and advancing a floor.
    '''
    elapsed_time = getElapsedTime()
    if elapsed_time > 400:
        print('Error found. Uncapable of finding a solution.\nExiting.')
        exit()
    for name, img in selection.items():
        button = pyautogui.locateOnScreen(img, confidence = 0.8, region = region)
        if button: 
            print(f'{name} found!')
            clickCenter(button)
            resetStartTime()
            return
    print('Waiting...')


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
    

def resetStartTime():
    '''
    Reset the timer.
    '''
    global start_time
    start_time = time.time()


def getElapsedTime():
    '''
    Get the timer's elapsed time.
    '''
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
    
    
def startScript(region, selection):
    '''
    Start the script.
    
    MAKE SURE that you are on the team building screen of adventure with the red "Enter Battle" button on the bottom right.
    '''
    resetStartTime()
    while True:
        detect_button(region, selection)
        time.sleep(5.5)      