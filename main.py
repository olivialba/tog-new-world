import tkinter as tk
import pygetwindow
from tkinter import ttk
from gamemodes.scriptTab import ScriptTab

class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.minsize(400, 300)
        self.root.maxsize(500, 400)
        self.root.title('ToG New World Script')
        
        self.notebook = ttk.Notebook(self.root)
        self.main_frame = tk.Frame(self.notebook)
        self.notebook.add(self.main_frame, text='Main')
        self.notebook.pack(fill="both", expand=True)
        
        self.tabs = []
        self.window_rect = None
        self.createWidgets()
        self.setWidgets()
        self.root.mainloop()
        
    def createWidgets(self):
        self.window_rect = None
        self.instruction_label = tk.Label(self.main_frame, text='Make sure you have your game window open')
        self.entry_label = tk.Label(self.main_frame, text='Game Window Title:')
        self.title_entry = tk.Entry(self.main_frame, width=30)
        self.find_window_button = tk.Button(self.main_frame, command=self.findGameWindow, text='Find', width=8)
        self.result_find_label = tk.Label(self.main_frame, text="Couldn't find game window..")
        
    def setWidgets(self):
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.instruction_label.grid(row=0, column=0, pady=(30,13))
        self.entry_label.grid(row=1, column=0, pady=(20,7))
        self.title_entry.grid(row=2, column=0, pady=(0,13), ipady=1)
        self.find_window_button.grid(row=3, column=0, pady=10, ipady=3)
        self.result_find_label.grid(row=4, column=0, pady=(30,0))
        self.result_find_label.grid_remove()
        
    def findGameWindow(self):
        title = (self.title_entry.get()).strip()
        if title:
            try:
                windows = [window.lower() for window in pygetwindow.getAllTitles()]
                app_window = None
                if title.lower() in windows:
                    app_window = pygetwindow.getWindowsWithTitle(title)
                    self.window_rect = (
                        app_window[0].left, 
                        app_window[0].top, 
                        app_window[0].width, 
                        app_window[0].height
                        )
            except:
                self.result_find_label.config(text="Error while finding game window")
            if app_window and self.window_rect is not None:
                self.result_find_label.config(text=f"Window '{title}' found!")
                self.createTab()
        else:
            self.result_find_label.config(text="Please input the game window title")
        self.result_find_label.grid()
        
    def createTab(self):
        for tab in self.tabs:
            tab.destroy()
        self.script_tab = tk.Frame(self.notebook)    
        self.notebook.add(self.script_tab, text='Script')     
        self.tabs.append(self.script_tab)   
        ScriptTab(self.script_tab, self.window_rect)
        
        
start_script = Main()