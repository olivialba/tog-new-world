from adventure import startAdventureScript
from chaos_trial import startChaosTrialScript
from detect_game import detectGame

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
    region = detectGame(windowTitle)
    if region:
        print()
        function(region)
    else:
        print("Phone window not found.")
        
        
if __name__ == '__main__':
    choiches = input("\n1 - Auto Adventure\n2 - Trial of Chaos\nPlease input your choiche: ")
    found = False
    for key in scripts:
        if key == choiches:
            found = True
            windowTitle = input("Please input the title of the game window: ")
            startScript(scripts[key], windowTitle)
    if found is False:
        print('Invalid selection.')