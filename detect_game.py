import pygetwindow

def detectGame(windowTitle):
    '''
    Detect the game window.
    '''
    title = windowTitle
    try:
        app_window = pygetwindow.getWindowsWithTitle(title)
        window_rect = (
            app_window[0].left, 
            app_window[0].top, 
            app_window[0].width, 
            app_window[0].height
            )
        return window_rect
    except:
        return None