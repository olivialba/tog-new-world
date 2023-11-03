from gamemodes.togScript import startScript

continue_buttons = {
    'Power Level': 'imgs/adventure/power_level_ok.png',
    'Challenge': 'imgs/chaos_trial/challenge.png',
    'Enter Battle': 'imgs/adventure/enter_battle.png',
    'Next Trial': 'imgs/chaos_trial/next_trial.png',
    'Level up': 'imgs/adventure/levelup_close.png', 
    'Unlock': 'imgs/adventure/continue.png', 
    }
       
def startChaosTrialScript(region):
    '''
    Start the script.
    
    MAKE SURE that you are on the team building screen of adventure with the red "Enter Battle" button on the bottom right.
    '''
    input("Go into the Trial Area- Trial of Chaos, and then press Enter to continue..")
    startScript(region, continue_buttons)