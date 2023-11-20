import tkinter as tk
from gamemodes.detectButton import detect_button
import time

class ScriptTab():
    def __init__(self, tab_frame, region):
        self.frame = tab_frame
        self.windowRegion = region
        self.stop = False
        self.MODE = None
        self.createButtonsDict()
        
        # PARENT FRAME
        self.left_frame = tk.Frame(self.frame, bd=1, width=150, height=130, relief='sunken')
        self.right_frame = tk.Frame(self.frame, width=150, height=100)
        # RIGHT FRAME
        self.mode_label = tk.Label(self.right_frame, text="Mode selected: N/A")
        self.start_button = tk.Button(self.right_frame, width=7, text='Start', state='normal', command=self.start_script)
        self.stop_button = tk.Button(self.right_frame, width=7, text='Stop', state='disabled', command=self.stop_script)
        self.log_entry = tk.Text(self.right_frame, width=21, height=8, state='disabled', wrap='word')
        # LEFT FRAME
        self.select_label = tk.Label(self.left_frame, text='Select mode:')
        self.menu_option = tk.StringVar()
        self.menu_option.trace('w', self.mode_selected)
        self.menu_option.set('Select Mode')
        self.menu_folder = tk.OptionMenu(self.left_frame, self.menu_option, *['Adventure', 'Trial of Chaos', 'Guardian Test'])
        self.speed_label = tk.Label(self.left_frame, text='Delay in seconds:')
        self.speed_scale = tk.Scale(self.left_frame, from_=1.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.speed_scale.bind("<ButtonRelease-1>", self.setSpeed)
        self.speed_scale.set(4.5)
        self.script_speed = 4500
        self.check_state = tk.IntVar()
        self.check_retry = tk.Checkbutton(self.left_frame, text='Infinite retries', variable=self.check_state, command=self.infiniteRetries)
        
        self.grid_setting()
        
    def grid_setting(self):
        # PARENT FRAME
        self.left_frame.grid(row=0, column=0, padx=15, pady=25, sticky='n')
        self.right_frame.grid(row=0, column=1, padx=15, pady=30, sticky='n')
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.speed_scale.grid(row=1, column=0)
        # RIGHT FRAME
        self.mode_label.grid(row=0, column=0, columnspan=2)
        self.start_button.grid(row=1, column=0, padx=(0,15), pady=15)
        self.stop_button.grid(row=1, column=1, padx=(15,0))
        self.log_entry.grid(row=2, column=0, columnspan=2)  
        # LEFT FRAME
        self.select_label.grid(row=0, column=0, padx=35, pady=15)
        self.menu_folder.grid(row=1, column=0)
        self.speed_label.grid(row=2, column=0, pady=(20,0))
        self.speed_scale.grid(row=3, column=0)
        self.check_retry.grid(row=4, column=0, pady=(20,10))
        
    def loopScript(self, MODE):
        if self.stop or self.MODE is None:
            return
        elif not self.stop:
            result = detect_button(self.windowRegion, MODE, self.start_time)
            if result == 'ERROR':
                self.update_log('* Error found')
                self.stop_script()
                return
            elif result:
                self.update_log('Button found!')
                self.resetStartTime()
            elif not result:
                self.update_log('Waiting...')
            self.frame.after(self.script_speed, self.loopScript, self.MODE)
    
    def start_script(self):
        self.stop = False
        mode = self.menu_option.get()
        match(mode):
            case 'Adventure':
                self.MODE = self.ADVENTURE_BUTTONS
            case 'Trial of Chaos':
                self.MODE = self.CHAOS_TRIAL_BUTTONS
            case 'Guardian Test':
                self.MODE = self.GUARDIAN_TEST_BUTTONS
            case _:
                return
        if str(self.start_button['state']) == 'normal':
            self.start_button.configure(state='disabled')
            self.stop_button.configure(state='normal')
            self.menu_folder.configure(state='disabled')
            self.update_log('\nStarting..')
            self.resetStartTime()
            self.frame.after(self.script_speed, self.loopScript, self.MODE)

    def stop_script(self):
        self.stop = True
        if str(self.stop_button['state']) == 'normal':
            self.stop_button.configure(state='disabled')
            self.start_button.configure(state='normal')
            self.menu_folder.configure(state='normal')
            self.update_log('Stopped')

    def update_log(self, text):
        self.log_entry.config(state='normal')
        self.log_entry.insert(tk.END, f'{text}\n')
        self.log_entry.see(tk.END)
        self.log_entry.config(state='disabled')
         
    def resetStartTime(self):
        self.start_time = time.time()
    
    def setSpeed(self, event):
        self.script_speed = int(self.speed_scale.get() * 1000)
    
    def mode_selected(self, *args):
        if self.menu_option.get() != 'Select Mode':
            self.mode_label.configure(text=f'Mode selected: {self.menu_option.get()}')
    
    def infiniteRetries(self):
        if self.check_state:
            self.ADVENTURE_BUTTONS['Retry'] = 'imgs/adventure/retry.png'
            self.CHAOS_TRIAL_BUTTONS['Retry'] = 'imgs/adventure/retry.png'
            self.GUARDIAN_TEST_BUTTONS['Retry'] = 'imgs/adventure/retry.png'
        else:
            del self.ADVENTURE_BUTTONS['Retry']
            del self.CHAOS_TRIAL_BUTTONS['Retry']
            del self.GUARDIAN_TEST_BUTTONS['Retry']
        mode = self.menu_option.get()
        match(mode):
            case 'Adventure':
                self.MODE = self.ADVENTURE_BUTTONS
            case 'Trial of Chaos':
                self.MODE = self.CHAOS_TRIAL_BUTTONS
            case 'Guardian Test':
                self.MODE = self.GUARDIAN_TEST_BUTTONS
            case _:
                return
    
    def createButtonsDict(self):
        self.ADVENTURE_BUTTONS = {
            'Power Level': 'imgs/adventure/power_level_ok.png',
            'Enter Battle': 'imgs/adventure/enter_battle.png',
            'Adventure': 'imgs/adventure/adventure.png',
            'Proceed': 'imgs/adventure/proceed.png',
            'Level up': 'imgs/adventure/levelup_close.png', 
            'Unlock': 'imgs/adventure/continue.png', 
            'Next floor': 'imgs/adventure/next_floor.png'
            }
        
        self.CHAOS_TRIAL_BUTTONS = {
            'Power Level': 'imgs/adventure/power_level_ok.png',
            'Challenge': 'imgs/chaos_trial/challenge.png',
            'Enter Battle': 'imgs/adventure/enter_battle.png',
            'Next Trial': 'imgs/chaos_trial/next_trial.png',
            'Level up': 'imgs/adventure/levelup_close.png', 
            'Unlock': 'imgs/adventure/continue.png', 
            }
        
        self.GUARDIAN_TEST_BUTTONS = {
            'Enter Battle': 'imgs/adventure/enter_battle.png',
            'Challenge' : 'imgs/guardian_test/challenge.png',
            'Next Test' : 'imgs/guardian_test/next_test.png',
            'Stars' : 'imgs/guardian_test/stars.png',
            }
        