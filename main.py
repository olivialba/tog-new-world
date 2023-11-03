from gamemodes.adventure import *
from gamemodes.chaos_trial import *
from gameutils.detect_game import *
from gamemodes.togScript import *

scripts = {
    '1' : startAdventureScript,
    '2' : startChaosTrialScript
}

def startScript(function, windowTitle):
    '''
    Detect the game window and start the script
    '''
    if not windowTitle:
        windowTitle = "POCO F3"
    try:
        region = detectGame(windowTitle)
        if region:
            print()
            function(region)
        else:
            input('Region not available')
    except Exception as e:
        print(e)
        input('\nEncountered Error. Press Enter to close..')
        
        
choiches = input("\n1 - Auto Adventure\n2 - Trial of Chaos\nPlease input your choiche: ")
found = False
for key in scripts:
    if key == choiches:
        found = True
        windowTitle = input("Please input the title of the game window: ")
        startScript(scripts[key], windowTitle)
if found is False:
    input('Invalid selection. Press Enter to close..')