from pynput.mouse import Button, Controller
import pygetwindow
import pyautogui
import time

mouse = Controller()
possible_errors = ['imgs/levelup_close.png', 'imgs/continue.png', 'imgs/next_floor.png']
outofsync = ['imgs/enter_battle.png', 'imgs/proceed.png']
start_time = 0

def detectGame(name):
    appTitle = name
    try:
        app_window = pygetwindow.getWindowsWithTitle(appTitle)
        window_rect = (
            app_window[0].left, 
            app_window[0].top, 
            app_window[0].width, 
            app_window[0].height
            )
        return window_rect
    except:
        return None

def mouse_click(X, Y):
    dx = (X - mouse.position[0])
    dy = (Y - mouse.position[1])
    mouse.move(dx, dy)
    mouse.click(Button.left)


def detect_button(region, img, name, sleep):
    while True:
        button = pyautogui.locateOnScreen(img, confidence = 0.9, region = region)
        if button:
            x = button.left + (button.width / 2)
            y = button.top + (button.height / 2)
            print(f"{name} button found!")
            time.sleep(0.3)
            mouse_click(x, y)
            resetStartTime()
            return
        else:
            print(f"{name} button not found, waiting..")
            time.sleep(sleep)
            
            elapsed_time = getElapsedTime()
            if elapsed_time > 65 and elapsed_time < 490:
                print("THERE MAY BE AN ERROR")
                
                for errors in possible_errors:
                    error = errorHandling(errors, region)
                    if error:
                        clickCenterError(error)
                        time.sleep(5)
                        for errors in possible_errors:
                            error = errorHandling(errors, region)
                            if error:
                                clickCenterError(error)
                        return

                for sync in outofsync:
                    synchronize = errorHandling(sync, region)
                    if synchronize:
                        return
                
            elif elapsed_time > 500:
                print("Found error. Uncapable of finding a solution.\nExiting.")
                exit()
                
                
def errorHandling(img, region):
    error = pyautogui.locateOnScreen(img, confidence = 0.8, region = region)
    if error:
        return error
    else:
        return False

def clickCenterError(position):
    try:
        sx = position.left + (position.width / 2)
        sy = position.top + (position.height / 2)
        time.sleep(0.2)
        mouse_click(sx, sy)
        time.sleep(10)
        resetStartTime()
    except:
        print("Error found!")
        return

def resetStartTime():
    global start_time
    start_time = time.time()

def getElapsedTime():
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
    
    
def startAdventureScript(name):
    if not name:
        name = "POCO F3"
    region = detectGame(name)
    if region:
        resetStartTime()
        while True:
            detect_button(region, 'imgs/enter_battle.png', 'Enter battle', 7)
            time.sleep(15)
            detect_button(region, 'imgs/proceed.png', 'Proceed', 7)
            time.sleep(5)
    else:
        print("Phone window not found.")    
                
                
                