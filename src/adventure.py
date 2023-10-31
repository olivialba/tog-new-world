from src.togScript import startScript

continue_buttons = {
    'Power Level': 'imgs/adventure/power_level_ok.png',
    'Enter Battle': 'imgs/adventure/enter_battle.png',
    'Adventure': 'imgs/adventure/adventure.png',
    'Proceed': 'imgs/adventure/proceed.png',
    'Level up': 'imgs/adventure/levelup_close.png', 
    'Unlock': 'imgs/adventure/continue.png', 
    'Next floor': 'imgs/adventure/next_floor.png'
    }
       
def startAdventureScript(region):
    '''
    Start the script.
    
    MAKE SURE that you are on the team building screen of adventure with the red "Enter Battle" button on the bottom right.
    '''
    input("Go into adventure mode and then press Enter to continue..")
    startScript(region, continue_buttons)    