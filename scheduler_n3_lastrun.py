#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri Mar  1 10:41:51 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import ast


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'Scheduler'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'scheduler csv': 'block_scheduler.csv',
    'output folder': 'Results/',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'%s/%s_%s_%s' % (expInfo['output folder'], expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kellycotton/Dropbox/Research/N3/scheduler_n3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "setup"
setupClock = core.Clock()
#import tkinter as tk       
import threading
#import tkinter.font as tkFont
#import tkinter.ttk as ttk
#import ttk
#from tkinter.ttk import *
print("made it here")
import asyncio
import websockets
from psychopy.hardware import keyboard
from psychopy import core
import pandas as pd

# create shared lock
current_selection = 0
force_end_routine = False
pause_routine = True
lock = threading.Lock()
timer = None

scheduler_csv_data = pd.read_csv(expInfo['scheduler csv'])
sched_header = list(scheduler_csv_data.columns)
sched_list = scheduler_csv_data.values.tolist()

class MainApplication(tk.Frame):              
    def __init__(self, parent, current_selection, pause_routine, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)   
        self.parent = parent
        #setting title
        parent.title("Experiment Scheduler")
        #setting window size
        self.started = False # turned on after start
        width=800
        height=500
        #width=1000
        #height=800
        self.width = width
        self.height = height
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        #alignstr = '%dx%d+%d+%d' % (width, height, -screenwidth/2, (screenheight - height) / 2 + 40)
        alignstr = '%dx%d+%d+%d' % (width, height, screenwidth/2, (screenheight - height) / 2)
        parent.geometry(alignstr)
        parent.resizable(width=False, height=False)
        
        self.selection = current_selection
        self.pause_routine = pause_routine
        self.countdown_params = None

        self.counter = tk.Label(self,font=(None, 15),bg= "gray90")
        self.counter.place(x=width//30,y=height//3.5,width=width//8.6,height=height//20)
        self.countdown(5,method='up',selection=current_selection)
        
        self.UpButton=tk.Button(self,state='disabled')
        self.UpButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.UpButton["font"] = ft
        self.UpButton["fg"] = "#000000"
        self.UpButton["justify"] = "center"
        self.UpButton["text"] = "Previous"
        self.UpButton.place(x=width//30,y=height//2.5,width=width//8.6,height=height//20)
        self.UpButton["command"] = self.UpButton_command

        self.DownButton=tk.Button(self,state='disabled')
        self.DownButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.DownButton["font"] = ft
        self.DownButton["fg"] = "#000000"
        self.DownButton["justify"] = "center"
        self.DownButton["text"] = "Next"
        self.DownButton.place(x=width//30,y=height//2.08,width=width//8.6,height=height//20)
        self.DownButton["command"] = self.DownButton_command

        self.StartButton=tk.Button(self)
        self.StartButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.StartButton["font"] = ft
        self.StartButton["fg"] = "#000000"
        self.StartButton["justify"] = "center"
        self.StartButton["text"] = "Start"
        self.StartButton.place(x=width//4.5,y=height//5.56,width=width//8.6,height=height//20)
        self.StartButton["command"] = self.StartButton_command

        self.PauseButton=tk.Button(self)
        self.PauseButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.PauseButton["font"] = ft
        self.PauseButton["fg"] = "#000000"
        self.PauseButton["justify"] = "center"
        self.PauseButton["text"] = "Pause"
        self.PauseButton.place(x=width//1.5,y=height//5.56,width=width//8.6,height=height//20)
        self.PauseButton["command"] = self.PauseButton_command
        
        self.tree = None
        self._setup_widgets()
        self._build_tree()
        
        
        self.tree.focus_set()
        self.children = self.tree.get_children()
        if self.children:
            self.tree.focus(self.children[self.selection])
            self.tree.selection_set(self.children[self.selection])

        thd_as = threading.Thread(target=self.run_asyncio_server)   # gui thread
        thd_as.daemon = True  # background thread will exit if main thread exits
        thd_as.start()  # start tk loop
    
    def countdown(self, count, selection, method='down',set_color=True):
        # ensure we need to continue counting
        if self.pause_routine:
            self.counter['text'] = 'PAUSED'
            return
        if selection != self.selection:
            return
        # change text in label        
        self.counter['text'] = "{:.2f}".format(count)
        if method=='down' and count > 0:
            if set_color:
                self.counter.config(fg="red")
            # call countdown again after 10ms
            self.parent.after(10, self.countdown, round(count-.01,2), selection, method,False)
        elif method=='up':
            if set_color:
                self.counter.config(fg="blue")
            # call countdown again after 10ms
            self.parent.after(10, self.countdown, round(count+.01,2), selection, method,False)
            
    def run_asyncio_server(self):
        async def handler(websocket, path):
            data = await websocket.recv()
            if data=='next':
                self.move_focus_down()
            elif data=='last':
                self.move_focus_up()
            reply = f"Data recieved bro as:  {data} selection {self.selection}!"
            await websocket.send(reply)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(handler, "localhost", 8000)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        
    def move_focus_down(self):
        if len(self.children)-1 == self.selection: # reset
            return
        last_selection = self.selection
        self.selection += 1
        if self.children and len(self.children) > self.selection:
            self.tree.focus(self.children[self.selection])
            self.tree.selection_set(self.children[self.selection])
        
        this_child = self.tree.item(self.children[self.selection])["values"]
        method = 'up' if float(this_child[2]) == 0 else 'down'
        self.countdown_params = (float(this_child[2]), self.selection, method)
        self.countdown(float(this_child[2]),selection=self.selection,method=method)
        global current_selection, force_end_routine, pause_routine
        with lock:
            if last_selection != self.selection:
                force_end_routine = True
            current_selection = self.selection
            
    def move_focus_up(self):
        if self.selection == 0: # if we hit the start
            return
            
        last_selection = self.selection
        self.selection -= 1
        if self.children and self.selection >= 0:
            self.tree.focus(self.children[self.selection])
            self.tree.selection_set(self.children[self.selection])
        #if self.selection == -1: # reset
            # self.selection = len(self.children)-1
        this_child = self.tree.item(self.children[self.selection])["values"]
        method = 'up' if float(this_child[2]) == 0 else 'down'
        self.countdown_params = (float(this_child[2]), self.selection, method)
        self.countdown(float(this_child[2]),selection=self.selection,method=method)
        global current_selection, force_end_routine, pause_routine
        with lock:
            if last_selection != self.selection:
                force_end_routine = True
            current_selection = self.selection

    def _setup_widgets(self):
        s = """\click on header to sort by that column
            to change width of column drag boundary
            """
        # msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
        #    padding=(10, 2, 10, 6), text=s)
        #msg.pack(fill='x')
        container = ttk.Frame()
        # container.pack(fill='both', expand=True)
        container.place(x=self.width//4.6,y=self.height//3.57,width=self.width//1.4,height=self.height//1.5)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=sched_header, show="headings", selectmode='none')
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in sched_header:
            self.tree.heading(col, text=col.title())
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in sched_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(sched_header[ix],width=None)<col_w:
                    self.tree.column(sched_header[ix], width=col_w)

    def UpButton_command(self):
        if self.started:
            self.move_focus_up()


    def DownButton_command(self):
        if self.started:
            self.move_focus_down()


    def StartButton_command(self):
        if not self.started:
            self.started = True
            self.UpButton['state'] = 'normal'
            self.DownButton['state'] = 'normal'
            self.StartButton['state'] = 'disabled'
            this_child = self.tree.item(self.children[self.selection])["values"]
            method = 'up' if float(this_child[2]) == 0 else 'down'
            self.countdown_params = (float(this_child[2]), self.selection, method)
        global current_selection, force_end_routine, pause_routine
        with lock:
            if self.pause_routine:
                self.pause_routine = False
                self.PauseButton['state'] = 'normal'
                self.StartButton['state'] = 'disabled'
                self.countdown(self.countdown_params[0],selection=self.countdown_params[1],method=self.countdown_params[2])
            pause_routine = self.pause_routine


    def PauseButton_command(self):
        global current_selection, force_end_routine, pause_routine
        with lock:
            if not self.pause_routine:                
                self.pause_routine = True
                force_end_routine = True # this may be changed depending on preferred pause behavior
                self.StartButton['state'] = 'normal'
                self.PauseButton['state'] = 'disabled'
            pause_routine = self.pause_routine

def runtk(current_selection, pause_routine):  # runs in background thread
    root = tk.Tk()
    MainApplication(root, current_selection, pause_routine).pack(side="top", fill="both", expand=True)
    root.mainloop()

thd = threading.Thread(target=runtk, args=(current_selection,pause_routine,))   # gui thread
thd.daemon = True  # background thread will exit if main thread exits
thd.start()  # start tk loop
from psychopy.hardware import keyboard
from psychopy import core
import time


setup_waiter = visual.TextStim(win=win, name='setup_waiter',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "parse_scheduler_row"
parse_scheduler_rowClock = core.Clock()
parse_waiter = visual.TextStim(win=win, name='parse_waiter',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "acquisition_start"
acquisition_startClock = core.Clock()
acq_start_text = visual.TextStim(win=win, name='acq_start_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "acquisition_end"
acquisition_endClock = core.Clock()
acquisition_end_text = visual.TextStim(win=win, name='acquisition_end_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "end_experiment"
end_experimentClock = core.Clock()

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "wait"
waitClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='Waiting for experimenter',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "begin_timer"
begin_timerClock = core.Clock()

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "stillface_trial"
stillface_trialClock = core.Clock()
trial_text = visual.TextStim(win=win, name='trial_text',
    text=None,
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "setup_face"
setup_faceClock = core.Clock()
import random 

total_time = task_parameters['total_time'] # seconds
facepresent_time = task_parameters['facepresent_time']  # seconds
num_faces = total_time/facepresent_time # has to be a round number

# Initialize components for Routine "begin_timer"
begin_timerClock = core.Clock()

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "fixation_face"
fixation_faceClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='* * * *',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "face_present"
face_presentClock = core.Clock()
raceface_image = visual.ImageStim(
    win=win,
    name='raceface_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "setup_cb"
setup_cbClock = core.Clock()

# Initialize components for Routine "begin_timer"
begin_timerClock = core.Clock()

# Initialize components for Routine "cb_instruct_1"
cb_instruct_1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='In the upcoming task, we will test the effects of practicing mental visualization on task performance. Thus, we need you to practice your mental visualization skills. We have found that the best way to do this is to have you play an on-line ball tossing game with other participants who are logged on to the system at the same time.\n\nIn a few moments, you will be playing a ball-tossing game with other players over our network. Several universities in the state of New York are taking part in a collaborative investigation of the effects of mental visualization on task performance, with people participating at several different universities around the state of New York.\n\nPress SPACE to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "cb_instruct_2"
cb_instruct_2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='The game is very simple. When the ball is tossed to you, simply press either the "red" button to throw to the player on your left or the "blue" button to throw to the player on your right. When the game is over, the experimenter will give you additional instructions.\n\nWhat is important is not your ball tossing performance, but that you MENTALLY VISUALIZE the entire experience. Imagine what the others look like. What sort of people are they? Where are you playing? Is it warm and sunny or cold and rainy? Create in your mind a complete mental picture of what might be going on if you were playing this game in real life.\n\nGet ready to start.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "cb_practice_start"
cb_practice_startClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text="Let's begin the practice. Remember, when it's your turn to throw, press the red button to throw to Player 2 and the blue button to throw the ball to Player 3.\n\nReady?",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "prac_cb_1"
prac_cb_1Clock = core.Clock()
start_3 = visual.ImageStim(
    win=win,
    name='start_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
text_20 = visual.TextStim(win=win, name='text_20',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "prac_cb_2"
prac_cb_2Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
key_resp_12 = keyboard.Keyboard()
text_23 = visual.TextStim(win=win, name='text_23',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "prac_cb_3"
prac_cb_3Clock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-3.0)

# Initialize components for Routine "prac_cb_4"
prac_cb_4Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
text_26 = visual.TextStim(win=win, name='text_26',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "cb_practice_end"
cb_practice_endClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='You have finished the practice.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "setup_cb"
setup_cbClock = core.Clock()

# Initialize components for Routine "cb_loading"
cb_loadingClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Loading...',
    font='Open Sans',
    pos=(0, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='Finding other players...',
    font='Open Sans',
    pos=(0, .1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='Player 1: You',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Player 2 found!',
    font='Open Sans',
    pos=(0, -.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='Player 3 found!',
    font='Open Sans',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='Get ready to begin!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "begin_timer"
begin_timerClock = core.Clock()

# Initialize components for Routine "start_routine_trigger"
start_routine_triggerClock = core.Clock()

# Initialize components for Routine "cyberball_1"
cyberball_1Clock = core.Clock()
start = visual.ImageStim(
    win=win,
    name='start', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "cyberball_2"
cyberball_2Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
cb_key_resp = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "cyberball_3"
cyberball_3Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-3.0)

# Initialize components for Routine "cyberball_4"
cyberball_4Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "cb_game_end"
cb_game_endClock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "end_routine_trigger"
end_routine_triggerClock = core.Clock()

# Initialize components for Routine "increment_selection"
increment_selectionClock = core.Clock()

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='You have reached the end of the experiment. Thank you! \n\nPress SPACE to end.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = [setup_waiter]
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if not pause_routine:
        continueRoutine=False
    
    # *setup_waiter* updates
    if setup_waiter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setup_waiter.frameNStart = frameN  # exact frame index
        setup_waiter.tStart = t  # local t and not account for scr refresh
        setup_waiter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setup_waiter, 'tStartRefresh')  # time at next scr refresh
        setup_waiter.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=999.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(expInfo['scheduler csv']),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "parse_scheduler_row"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    parse_scheduler_rowComponents = [parse_waiter]
    for thisComponent in parse_scheduler_rowComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    parse_scheduler_rowClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "parse_scheduler_row"-------
    while continueRoutine:
        # get current time
        t = parse_scheduler_rowClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=parse_scheduler_rowClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if not pause_routine:
            continueRoutine=False
        
        # *parse_waiter* updates
        if parse_waiter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            parse_waiter.frameNStart = frameN  # exact frame index
            parse_waiter.tStart = t  # local t and not account for scr refresh
            parse_waiter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(parse_waiter, 'tStartRefresh')  # time at next scr refresh
            parse_waiter.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in parse_scheduler_rowComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "parse_scheduler_row"-------
    for thisComponent in parse_scheduler_rowComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    force_end_routine = False
    
    for key,val in scheduler_csv_data.iloc[current_selection].items():
            exec(key + '=val')
            
    if str(task_parameters) != 'nan':
        task_parameters = ast.literal_eval(task_parameters)
    else:
        task_parameters = {}
    # the Routine "parse_scheduler_row" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    acq_start = data.TrialHandler(nReps=sum([task_type=='acq_start']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='acq_start')
    thisExp.addLoop(acq_start)  # add the loop to the experiment
    thisAcq_start = acq_start.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAcq_start.rgb)
    if thisAcq_start != None:
        for paramName in thisAcq_start:
            exec('{} = thisAcq_start[paramName]'.format(paramName))
    
    for thisAcq_start in acq_start:
        currentLoop = acq_start
        # abbreviate parameter names if possible (e.g. rgb = thisAcq_start.rgb)
        if thisAcq_start != None:
            for paramName in thisAcq_start:
                exec('{} = thisAcq_start[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "acquisition_start"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        
        # keep track of which components have finished
        acquisition_startComponents = [acq_start_text]
        for thisComponent in acquisition_startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        acquisition_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "acquisition_start"-------
        while continueRoutine:
            # get current time
            t = acquisition_startClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=acquisition_startClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if force_end_routine or timer.getTime() <= 0:
                continueRoutine=False
                acq_start.finished=True
            
            # *acq_start_text* updates
            if acq_start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                acq_start_text.frameNStart = frameN  # exact frame index
                acq_start_text.tStart = t  # local t and not account for scr refresh
                acq_start_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(acq_start_text, 'tStartRefresh')  # time at next scr refresh
                acq_start_text.setAutoDraw(True)
            if acq_start_text.status == STARTED:  # only update if drawing
                acq_start_text.setText(str(round(timer.getTime(),2)) + '\n' + "Acquisition starting", log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in acquisition_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "acquisition_start"-------
        for thisComponent in acquisition_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "acquisition_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='acq_start']) repeats of 'acq_start'
    
    
    # set up handler to look after randomisation of conditions etc
    acq_end = data.TrialHandler(nReps=sum([task_type=='acq_end']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='acq_end')
    thisExp.addLoop(acq_end)  # add the loop to the experiment
    thisAcq_end = acq_end.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAcq_end.rgb)
    if thisAcq_end != None:
        for paramName in thisAcq_end:
            exec('{} = thisAcq_end[paramName]'.format(paramName))
    
    for thisAcq_end in acq_end:
        currentLoop = acq_end
        # abbreviate parameter names if possible (e.g. rgb = thisAcq_end.rgb)
        if thisAcq_end != None:
            for paramName in thisAcq_end:
                exec('{} = thisAcq_end[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "acquisition_end"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        
        # keep track of which components have finished
        acquisition_endComponents = [acquisition_end_text]
        for thisComponent in acquisition_endComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        acquisition_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "acquisition_end"-------
        while continueRoutine:
            # get current time
            t = acquisition_endClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=acquisition_endClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if force_end_routine or timer.getTime() <= 0:
                continueRoutine=False
                acq_end.finished=True
            
            # *acquisition_end_text* updates
            if acquisition_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                acquisition_end_text.frameNStart = frameN  # exact frame index
                acquisition_end_text.tStart = t  # local t and not account for scr refresh
                acquisition_end_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(acquisition_end_text, 'tStartRefresh')  # time at next scr refresh
                acquisition_end_text.setAutoDraw(True)
            if acquisition_end_text.status == STARTED:
                if bool(timer.getTime() <= -.01):
                    # keep track of stop time/frame for later
                    acquisition_end_text.tStop = t  # not accounting for scr refresh
                    acquisition_end_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(acquisition_end_text, 'tStopRefresh')  # time at next scr refresh
                    acquisition_end_text.setAutoDraw(False)
            if acquisition_end_text.status == STARTED:  # only update if drawing
                acquisition_end_text.setText(str(round(timer.getTime(),2)) + '\n' + "Acquisition ending", log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in acquisition_endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "acquisition_end"-------
        for thisComponent in acquisition_endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        acq_end.addData('acquisition_end_text.started', acquisition_end_text.tStartRefresh)
        acq_end.addData('acquisition_end_text.stopped', acquisition_end_text.tStopRefresh)
        # the Routine "acquisition_end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "end_experiment"-------
        continueRoutine = True
        # update component parameters for each repeat
        core.quit()
        # keep track of which components have finished
        end_experimentComponents = []
        for thisComponent in end_experimentComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_experiment"-------
        while continueRoutine:
            # get current time
            t = end_experimentClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_experimentClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_experimentComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_experiment"-------
        for thisComponent in end_experimentComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_experiment" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='acq_end']) repeats of 'acq_end'
    
    
    # set up handler to look after randomisation of conditions etc
    wait_block = data.TrialHandler(nReps=sum([task_type=='wait']), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='wait_block')
    thisExp.addLoop(wait_block)  # add the loop to the experiment
    thisWait_block = wait_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWait_block.rgb)
    if thisWait_block != None:
        for paramName in thisWait_block:
            exec('{} = thisWait_block[paramName]'.format(paramName))
    
    for thisWait_block in wait_block:
        currentLoop = wait_block
        # abbreviate parameter names if possible (e.g. rgb = thisWait_block.rgb)
        if thisWait_block != None:
            for paramName in thisWait_block:
                exec('{} = thisWait_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "wait"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        waitComponents = [wait_text]
        for thisComponent in waitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "wait"-------
        while continueRoutine:
            # get current time
            t = waitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=waitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if force_end_routine and duration==0:
                continueRoutine=False
                wait_block.finished=True
            elif duration > 0 and (force_end_routine or timer.getTime() <= 0):
                continueRoutine=False
                wait_block.finished=True
            
            # *wait_text* updates
            if wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_text.frameNStart = frameN  # exact frame index
                wait_text.tStart = t  # local t and not account for scr refresh
                wait_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_text, 'tStartRefresh')  # time at next scr refresh
                wait_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in waitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "wait"-------
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "wait" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='wait']) repeats of 'wait_block'
    
    
    # set up handler to look after randomisation of conditions etc
    stillface = data.TrialHandler(nReps=sum([task_type=='stillface']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='stillface')
    thisExp.addLoop(stillface)  # add the loop to the experiment
    thisStillface = stillface.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStillface.rgb)
    if thisStillface != None:
        for paramName in thisStillface:
            exec('{} = thisStillface[paramName]'.format(paramName))
    
    for thisStillface in stillface:
        currentLoop = stillface
        # abbreviate parameter names if possible (e.g. rgb = thisStillface.rgb)
        if thisStillface != None:
            for paramName in thisStillface:
                exec('{} = thisStillface[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "begin_timer"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        begin_timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "begin_timer"-------
        while continueRoutine:
            # get current time
            t = begin_timerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=begin_timerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "begin_timer"-------
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        stillface_trials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='stillface_trials')
        thisExp.addLoop(stillface_trials)  # add the loop to the experiment
        thisStillface_trial = stillface_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisStillface_trial.rgb)
        if thisStillface_trial != None:
            for paramName in thisStillface_trial:
                exec('{} = thisStillface_trial[paramName]'.format(paramName))
        
        for thisStillface_trial in stillface_trials:
            currentLoop = stillface_trials
            # abbreviate parameter names if possible (e.g. rgb = thisStillface_trial.rgb)
            if thisStillface_trial != None:
                for paramName in thisStillface_trial:
                    exec('{} = thisStillface_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "stillface_trial"-------
            continueRoutine = True
            # update component parameters for each repeat
            win.setColor('white') 
            stillface_time = task_parameters['stillface_time']
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # keep track of which components have finished
            stillface_trialComponents = [trial_text, key_resp_4]
            for thisComponent in stillface_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            stillface_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "stillface_trial"-------
            while continueRoutine:
                # get current time
                t = stillface_trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=stillface_trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    stillface_trials.finished=True
                
                # *trial_text* updates
                if trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    trial_text.frameNStart = frameN  # exact frame index
                    trial_text.tStart = t  # local t and not account for scr refresh
                    trial_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
                    trial_text.setAutoDraw(True)
                if trial_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > trial_text.tStartRefresh + stillface_time-frameTolerance:
                        # keep track of stop time/frame for later
                        trial_text.tStop = t  # not accounting for scr refresh
                        trial_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(trial_text, 'tStopRefresh')  # time at next scr refresh
                        trial_text.setAutoDraw(False)
                
                # *key_resp_4* updates
                waitOnFlip = False
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + stillface_time-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                        key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stillface_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "stillface_trial"-------
            for thisComponent in stillface_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "stillface_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'stillface_trials'
        
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='stillface']) repeats of 'stillface'
    
    
    # set up handler to look after randomisation of conditions etc
    raceface_trials = data.TrialHandler(nReps=sum([task_type=='raceface']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='raceface_trials')
    thisExp.addLoop(raceface_trials)  # add the loop to the experiment
    thisRaceface_trial = raceface_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRaceface_trial.rgb)
    if thisRaceface_trial != None:
        for paramName in thisRaceface_trial:
            exec('{} = thisRaceface_trial[paramName]'.format(paramName))
    
    for thisRaceface_trial in raceface_trials:
        currentLoop = raceface_trials
        # abbreviate parameter names if possible (e.g. rgb = thisRaceface_trial.rgb)
        if thisRaceface_trial != None:
            for paramName in thisRaceface_trial:
                exec('{} = thisRaceface_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "setup_face"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        setup_faceComponents = []
        for thisComponent in setup_faceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        setup_faceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "setup_face"-------
        while continueRoutine:
            # get current time
            t = setup_faceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=setup_faceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in setup_faceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "setup_face"-------
        for thisComponent in setup_faceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "setup_face" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "begin_timer"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        begin_timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "begin_timer"-------
        while continueRoutine:
            # get current time
            t = begin_timerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=begin_timerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "begin_timer"-------
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixation_face"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        trial_n = 0
        n_files = task_parameters['n_files']
        face_n = list(range(0,n_files))
        random.shuffle(face_n)
        # keep track of which components have finished
        fixation_faceComponents = [text]
        for thisComponent in fixation_faceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixation_faceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation_face"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixation_faceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixation_faceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_faceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation_face"-------
        for thisComponent in fixation_faceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=num_faces, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    exec('{} = thisTrial_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "face_present"-------
            continueRoutine = True
            # update component parameters for each repeat
            race_condition = task_parameters['race_condition']
            
            image_present = "face_stim/" + race_condition + str(face_n[trial_n]) + ".jpg"
            
            raceface_image.setImage(image_present)
            # keep track of which components have finished
            face_presentComponents = [raceface_image]
            for thisComponent in face_presentComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            face_presentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "face_present"-------
            while continueRoutine:
                # get current time
                t = face_presentClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=face_presentClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    raceface_trials.finished=True
                
                # *raceface_image* updates
                if raceface_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    raceface_image.frameNStart = frameN  # exact frame index
                    raceface_image.tStart = t  # local t and not account for scr refresh
                    raceface_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(raceface_image, 'tStartRefresh')  # time at next scr refresh
                    raceface_image.setAutoDraw(True)
                if raceface_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > raceface_image.tStartRefresh + facepresent_time-frameTolerance:
                        # keep track of stop time/frame for later
                        raceface_image.tStop = t  # not accounting for scr refresh
                        raceface_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(raceface_image, 'tStopRefresh')  # time at next scr refresh
                        raceface_image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in face_presentComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "face_present"-------
            for thisComponent in face_presentComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trial_n += 1
            trials_3.addData('raceface_image.started', raceface_image.tStartRefresh)
            trials_3.addData('raceface_image.stopped', raceface_image.tStopRefresh)
            # the Routine "face_present" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed num_faces repeats of 'trials_3'
        
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='raceface']) repeats of 'raceface_trials'
    
    
    # set up handler to look after randomisation of conditions etc
    cyberball_practice = data.TrialHandler(nReps=sum([task_type=='cyberball_practice']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cyberball_practice')
    thisExp.addLoop(cyberball_practice)  # add the loop to the experiment
    thisCyberball_practice = cyberball_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCyberball_practice.rgb)
    if thisCyberball_practice != None:
        for paramName in thisCyberball_practice:
            exec('{} = thisCyberball_practice[paramName]'.format(paramName))
    
    for thisCyberball_practice in cyberball_practice:
        currentLoop = cyberball_practice
        # abbreviate parameter names if possible (e.g. rgb = thisCyberball_practice.rgb)
        if thisCyberball_practice != None:
            for paramName in thisCyberball_practice:
                exec('{} = thisCyberball_practice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "setup_cb"-------
        continueRoutine = True
        # update component parameters for each repeat
        import sys
        import random
        import serial
        import os
        import time
        
        paths = [d for d in os.listdir('images') if d[1:3]=='to']
        throw={}
        for p in paths:
            imgs = [f for f in os.listdir('images/%s' % p) if f.endswith('.bmp')]
            # sort image filenames to get correct sequence of throw steps
            throw[p]= sorted(imgs)
            
        def select_player_image(fromP, toP, s):
            key = "%ito%i" % (fromP,toP)
                
            player_img = ('images/%s/%s-%s.bmp' % (key, key, s))
            return player_img
        
        def select_throw(holder, block_threshold):
            if holder==2:
                #got_ball_time = trialClock.getTime()
                
                choice=[]
                while len(choice)==0 or choice [0] not in ('num_4','num_add'):
                    choice = event.getKeys(keyList=['num_4','num_add'])
                if choice[0]=='num_4':
                    throwTo=1
                elif choice[0]=='num_add':
                    throwTo=3
                    
            else:    
                throwChoice = random.random()
                if throwChoice > block_threshold:
                    if holder==1:
                        throwTo=3
                    else:
                        throwTo=1
                else:
                    throwTo=2
            
            return holder, throwTo
        # keep track of which components have finished
        setup_cbComponents = []
        for thisComponent in setup_cbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        setup_cbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "setup_cb"-------
        while continueRoutine:
            # get current time
            t = setup_cbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=setup_cbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in setup_cbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "setup_cb"-------
        for thisComponent in setup_cbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "setup_cb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "begin_timer"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        begin_timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "begin_timer"-------
        while continueRoutine:
            # get current time
            t = begin_timerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=begin_timerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "begin_timer"-------
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cb_instruct_1"-------
        continueRoutine = True
        # update component parameters for each repeat
        game_i = 1
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        cb_instruct_1Components = [text_2, key_resp_2]
        for thisComponent in cb_instruct_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cb_instruct_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cb_instruct_1"-------
        while continueRoutine:
            # get current time
            t = cb_instruct_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cb_instruct_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cb_instruct_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cb_instruct_1"-------
        for thisComponent in cb_instruct_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "cb_instruct_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cb_instruct_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        cb_instruct_2Components = [text_3, key_resp_6]
        for thisComponent in cb_instruct_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cb_instruct_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cb_instruct_2"-------
        while continueRoutine:
            # get current time
            t = cb_instruct_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cb_instruct_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # *key_resp_6* updates
            waitOnFlip = False
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cb_instruct_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cb_instruct_2"-------
        for thisComponent in cb_instruct_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "cb_instruct_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cb_practice_start"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        block_threshold = task_parameters['block_threshold']
        # keep track of which components have finished
        cb_practice_startComponents = [text_28, key_resp_7]
        for thisComponent in cb_practice_startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cb_practice_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cb_practice_start"-------
        while continueRoutine:
            # get current time
            t = cb_practice_startClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cb_practice_startClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_28* updates
            if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_28.frameNStart = frameN  # exact frame index
                text_28.tStart = t  # local t and not account for scr refresh
                text_28.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
                text_28.setAutoDraw(True)
            
            # *key_resp_7* updates
            waitOnFlip = False
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cb_practice_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cb_practice_start"-------
        for thisComponent in cb_practice_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "cb_practice_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "prac_cb_1"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        holder = 1
        player_img = "images/start.bmp"
        start_3.setImage(player_img)
        # keep track of which components have finished
        prac_cb_1Components = [start_3, text_20, text_21]
        for thisComponent in prac_cb_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prac_cb_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac_cb_1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prac_cb_1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prac_cb_1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if force_end_routine or timer.getTime() <= 0:
                continueRoutine=False
                cyberball_practice.finished=True
            
            # *start_3* updates
            if start_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_3.frameNStart = frameN  # exact frame index
                start_3.tStart = t  # local t and not account for scr refresh
                start_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_3, 'tStartRefresh')  # time at next scr refresh
                start_3.setAutoDraw(True)
            if start_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > start_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    start_3.tStop = t  # not accounting for scr refresh
                    start_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(start_3, 'tStopRefresh')  # time at next scr refresh
                    start_3.setAutoDraw(False)
            
            # *text_20* updates
            if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_20.frameNStart = frameN  # exact frame index
                text_20.tStart = t  # local t and not account for scr refresh
                text_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
                text_20.setAutoDraw(True)
            if text_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_20.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_20.tStop = t  # not accounting for scr refresh
                    text_20.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
                    text_20.setAutoDraw(False)
            
            # *text_21* updates
            if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_21.frameNStart = frameN  # exact frame index
                text_21.tStart = t  # local t and not account for scr refresh
                text_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
                text_21.setAutoDraw(True)
            if text_21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_21.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_21.tStop = t  # not accounting for scr refresh
                    text_21.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
                    text_21.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_cb_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_cb_1"-------
        for thisComponent in prac_cb_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # set up handler to look after randomisation of conditions etc
        prac_cb_trials_2 = data.TrialHandler(nReps=task_parameters['cb_throws'], method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='prac_cb_trials_2')
        thisExp.addLoop(prac_cb_trials_2)  # add the loop to the experiment
        thisPrac_cb_trial_2 = prac_cb_trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_cb_trial_2.rgb)
        if thisPrac_cb_trial_2 != None:
            for paramName in thisPrac_cb_trial_2:
                exec('{} = thisPrac_cb_trial_2[paramName]'.format(paramName))
        
        for thisPrac_cb_trial_2 in prac_cb_trials_2:
            currentLoop = prac_cb_trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_cb_trial_2.rgb)
            if thisPrac_cb_trial_2 != None:
                for paramName in thisPrac_cb_trial_2:
                    exec('{} = thisPrac_cb_trial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "prac_cb_2"-------
            continueRoutine = True
            # update component parameters for each repeat
            
            s = 1
            img_length = 3
            
            if holder == 2:
                core.wait(0.01)
            else:
                core.wait(random.randint(500, 3500)/1000)
                img_length = .2
            
            player = select_throw(holder, block_threshold)
            holder = player[0]
            next_holder = player[1]
            
            player_img = select_player_image(holder, next_holder, s)
            
            nreps = len(throw["%ito%i" % (holder,next_holder)])
            
            #print("current holder: ", holder, "next_holder: ", next_holder, "Key: ", "%ito%i" % (holder,next_holder), "nreps:", nreps)
            image_5.setImage(player_img)
            key_resp_12.keys = []
            key_resp_12.rt = []
            _key_resp_12_allKeys = []
            # keep track of which components have finished
            prac_cb_2Components = [image_5, key_resp_12, text_23, text_24]
            for thisComponent in prac_cb_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            prac_cb_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "prac_cb_2"-------
            while continueRoutine:
                # get current time
                t = prac_cb_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=prac_cb_2Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if (holder == 2) and (key_resp.keys == '2' or key_resp.keys == '3'):
                    continueRoutine = False
                
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    cyberball_practice.finished=True
                
                # *image_5* updates
                if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_5.frameNStart = frameN  # exact frame index
                    image_5.tStart = t  # local t and not account for scr refresh
                    image_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(True)
                if image_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_5.tStartRefresh + img_length-frameTolerance:
                        # keep track of stop time/frame for later
                        image_5.tStop = t  # not accounting for scr refresh
                        image_5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                        image_5.setAutoDraw(False)
                
                # *key_resp_12* updates
                waitOnFlip = False
                if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_12.frameNStart = frameN  # exact frame index
                    key_resp_12.tStart = t  # local t and not account for scr refresh
                    key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                    key_resp_12.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_12.tStartRefresh + img_length-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_12.tStop = t  # not accounting for scr refresh
                        key_resp_12.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_12, 'tStopRefresh')  # time at next scr refresh
                        key_resp_12.status = FINISHED
                if key_resp_12.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_12.getKeys(keyList=['2','3'], waitRelease=False)
                    _key_resp_12_allKeys.extend(theseKeys)
                    if len(_key_resp_12_allKeys):
                        key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                        key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                
                # *text_23* updates
                if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_23.frameNStart = frameN  # exact frame index
                    text_23.tStart = t  # local t and not account for scr refresh
                    text_23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
                    text_23.setAutoDraw(True)
                if text_23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_23.tStartRefresh + img_length-frameTolerance:
                        # keep track of stop time/frame for later
                        text_23.tStop = t  # not accounting for scr refresh
                        text_23.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
                        text_23.setAutoDraw(False)
                
                # *text_24* updates
                if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_24.frameNStart = frameN  # exact frame index
                    text_24.tStart = t  # local t and not account for scr refresh
                    text_24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
                    text_24.setAutoDraw(True)
                if text_24.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_24.tStartRefresh + img_length-frameTolerance:
                        # keep track of stop time/frame for later
                        text_24.tStop = t  # not accounting for scr refresh
                        text_24.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
                        text_24.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in prac_cb_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "prac_cb_2"-------
            for thisComponent in prac_cb_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_12.keys in ['', [], None]:  # No response was made
                key_resp_12.keys = None
            prac_cb_trials_2.addData('key_resp_12.keys',key_resp_12.keys)
            if key_resp_12.keys != None:  # we had a response
                prac_cb_trials_2.addData('key_resp_12.rt', key_resp_12.rt)
            # the Routine "prac_cb_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            prac_cb_trials = data.TrialHandler(nReps=nreps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='prac_cb_trials')
            thisExp.addLoop(prac_cb_trials)  # add the loop to the experiment
            thisPrac_cb_trial = prac_cb_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisPrac_cb_trial.rgb)
            if thisPrac_cb_trial != None:
                for paramName in thisPrac_cb_trial:
                    exec('{} = thisPrac_cb_trial[paramName]'.format(paramName))
            
            for thisPrac_cb_trial in prac_cb_trials:
                currentLoop = prac_cb_trials
                # abbreviate parameter names if possible (e.g. rgb = thisPrac_cb_trial.rgb)
                if thisPrac_cb_trial != None:
                    for paramName in thisPrac_cb_trial:
                        exec('{} = thisPrac_cb_trial[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "prac_cb_3"-------
                continueRoutine = True
                routineTimer.add(0.150000)
                # update component parameters for each repeat
                player_img = select_player_image(holder, next_holder, s)
                
                image_7.setImage(player_img)
                # keep track of which components have finished
                prac_cb_3Components = [text_25, text_30, image_7]
                for thisComponent in prac_cb_3Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                prac_cb_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "prac_cb_3"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = prac_cb_3Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=prac_cb_3Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    if force_end_routine or timer.getTime() <= 0:
                        continueRoutine=False
                        cyberball_practice.finished=True
                    
                    # *text_25* updates
                    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_25.frameNStart = frameN  # exact frame index
                        text_25.tStart = t  # local t and not account for scr refresh
                        text_25.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
                        text_25.setAutoDraw(True)
                    if text_25.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_25.tStartRefresh + .15-frameTolerance:
                            # keep track of stop time/frame for later
                            text_25.tStop = t  # not accounting for scr refresh
                            text_25.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
                            text_25.setAutoDraw(False)
                    
                    # *text_30* updates
                    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_30.frameNStart = frameN  # exact frame index
                        text_30.tStart = t  # local t and not account for scr refresh
                        text_30.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
                        text_30.setAutoDraw(True)
                    if text_30.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_30.tStartRefresh + .15-frameTolerance:
                            # keep track of stop time/frame for later
                            text_30.tStop = t  # not accounting for scr refresh
                            text_30.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
                            text_30.setAutoDraw(False)
                    
                    # *image_7* updates
                    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_7.frameNStart = frameN  # exact frame index
                        image_7.tStart = t  # local t and not account for scr refresh
                        image_7.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                        image_7.setAutoDraw(True)
                    if image_7.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_7.tStartRefresh + .15-frameTolerance:
                            # keep track of stop time/frame for later
                            image_7.tStop = t  # not accounting for scr refresh
                            image_7.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
                            image_7.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in prac_cb_3Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "prac_cb_3"-------
                for thisComponent in prac_cb_3Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                s+=1
                thisExp.nextEntry()
                
            # completed nreps repeats of 'prac_cb_trials'
            
            
            # ------Prepare to start Routine "prac_cb_4"-------
            continueRoutine = True
            routineTimer.add(0.150000)
            # update component parameters for each repeat
            image_6.setImage(player_img)
            # keep track of which components have finished
            prac_cb_4Components = [image_6, text_26, text_27]
            for thisComponent in prac_cb_4Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            prac_cb_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "prac_cb_4"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = prac_cb_4Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=prac_cb_4Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    cyberball_practice.finished=True
                
                # *image_6* updates
                if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_6.frameNStart = frameN  # exact frame index
                    image_6.tStart = t  # local t and not account for scr refresh
                    image_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                    image_6.setAutoDraw(True)
                if image_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_6.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_6.tStop = t  # not accounting for scr refresh
                        image_6.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
                        image_6.setAutoDraw(False)
                
                # *text_26* updates
                if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_26.frameNStart = frameN  # exact frame index
                    text_26.tStart = t  # local t and not account for scr refresh
                    text_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
                    text_26.setAutoDraw(True)
                if text_26.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_26.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        text_26.tStop = t  # not accounting for scr refresh
                        text_26.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_26, 'tStopRefresh')  # time at next scr refresh
                        text_26.setAutoDraw(False)
                
                # *text_27* updates
                if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_27.frameNStart = frameN  # exact frame index
                    text_27.tStart = t  # local t and not account for scr refresh
                    text_27.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
                    text_27.setAutoDraw(True)
                if text_27.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_27.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        text_27.tStop = t  # not accounting for scr refresh
                        text_27.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_27, 'tStopRefresh')  # time at next scr refresh
                        text_27.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in prac_cb_4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "prac_cb_4"-------
            for thisComponent in prac_cb_4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            holder = next_holder
            s = 1
            thisExp.nextEntry()
            
        # completed task_parameters['cb_throws'] repeats of 'prac_cb_trials_2'
        
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cb_practice_end"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # keep track of which components have finished
        cb_practice_endComponents = [text_29, key_resp_8]
        for thisComponent in cb_practice_endComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cb_practice_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cb_practice_end"-------
        while continueRoutine:
            # get current time
            t = cb_practice_endClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cb_practice_endClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_29* updates
            if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_29.frameNStart = frameN  # exact frame index
                text_29.tStart = t  # local t and not account for scr refresh
                text_29.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
                text_29.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cb_practice_endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cb_practice_end"-------
        for thisComponent in cb_practice_endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "cb_practice_end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='cyberball_practice']) repeats of 'cyberball_practice'
    
    
    # set up handler to look after randomisation of conditions etc
    cyberball_trials = data.TrialHandler(nReps=sum([task_type=='cyberball_practice']), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='cyberball_trials')
    thisExp.addLoop(cyberball_trials)  # add the loop to the experiment
    thisCyberball_trial = cyberball_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCyberball_trial.rgb)
    if thisCyberball_trial != None:
        for paramName in thisCyberball_trial:
            exec('{} = thisCyberball_trial[paramName]'.format(paramName))
    
    for thisCyberball_trial in cyberball_trials:
        currentLoop = cyberball_trials
        # abbreviate parameter names if possible (e.g. rgb = thisCyberball_trial.rgb)
        if thisCyberball_trial != None:
            for paramName in thisCyberball_trial:
                exec('{} = thisCyberball_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "setup_cb"-------
        continueRoutine = True
        # update component parameters for each repeat
        import sys
        import random
        import serial
        import os
        import time
        
        paths = [d for d in os.listdir('images') if d[1:3]=='to']
        throw={}
        for p in paths:
            imgs = [f for f in os.listdir('images/%s' % p) if f.endswith('.bmp')]
            # sort image filenames to get correct sequence of throw steps
            throw[p]= sorted(imgs)
            
        def select_player_image(fromP, toP, s):
            key = "%ito%i" % (fromP,toP)
                
            player_img = ('images/%s/%s-%s.bmp' % (key, key, s))
            return player_img
        
        def select_throw(holder, block_threshold):
            if holder==2:
                #got_ball_time = trialClock.getTime()
                
                choice=[]
                while len(choice)==0 or choice [0] not in ('num_4','num_add'):
                    choice = event.getKeys(keyList=['num_4','num_add'])
                if choice[0]=='num_4':
                    throwTo=1
                elif choice[0]=='num_add':
                    throwTo=3
                    
            else:    
                throwChoice = random.random()
                if throwChoice > block_threshold:
                    if holder==1:
                        throwTo=3
                    else:
                        throwTo=1
                else:
                    throwTo=2
            
            return holder, throwTo
        # keep track of which components have finished
        setup_cbComponents = []
        for thisComponent in setup_cbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        setup_cbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "setup_cb"-------
        while continueRoutine:
            # get current time
            t = setup_cbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=setup_cbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in setup_cbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "setup_cb"-------
        for thisComponent in setup_cbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "setup_cb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "cb_loading"-------
        continueRoutine = True
        routineTimer.add(13.000000)
        # update component parameters for each repeat
        block_threshold = task_parameters['block_threshold']
        # keep track of which components have finished
        cb_loadingComponents = [text_12, text_13, text_14, text_17, text_15, text_16]
        for thisComponent in cb_loadingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        cb_loadingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "cb_loading"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cb_loadingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=cb_loadingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_12* updates
            if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                text_12.setAutoDraw(True)
            if text_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_12.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    text_12.tStop = t  # not accounting for scr refresh
                    text_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                    text_12.setAutoDraw(False)
            
            # *text_13* updates
            if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_13.frameNStart = frameN  # exact frame index
                text_13.tStart = t  # local t and not account for scr refresh
                text_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                text_13.setAutoDraw(True)
            if text_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_13.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_13.tStop = t  # not accounting for scr refresh
                    text_13.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
                    text_13.setAutoDraw(False)
            
            # *text_14* updates
            if text_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)
            if text_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_14.tStartRefresh + 8-frameTolerance:
                    # keep track of stop time/frame for later
                    text_14.tStop = t  # not accounting for scr refresh
                    text_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                    text_14.setAutoDraw(False)
            
            # *text_17* updates
            if text_17.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                text_17.setAutoDraw(True)
            if text_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_17.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_17.tStop = t  # not accounting for scr refresh
                    text_17.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                    text_17.setAutoDraw(False)
            
            # *text_15* updates
            if text_15.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                text_15.setAutoDraw(True)
            if text_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_15.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text_15.tStop = t  # not accounting for scr refresh
                    text_15.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
                    text_15.setAutoDraw(False)
            
            # *text_16* updates
            if text_16.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
                # keep track of start time/frame for later
                text_16.frameNStart = frameN  # exact frame index
                text_16.tStart = t  # local t and not account for scr refresh
                text_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
                text_16.setAutoDraw(True)
            if text_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_16.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_16.tStop = t  # not accounting for scr refresh
                    text_16.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                    text_16.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cb_loadingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cb_loading"-------
        for thisComponent in cb_loadingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "begin_timer"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer = core.CountdownTimer(duration)
        # keep track of which components have finished
        begin_timerComponents = []
        for thisComponent in begin_timerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        begin_timerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "begin_timer"-------
        while continueRoutine:
            # get current time
            t = begin_timerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=begin_timerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in begin_timerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "begin_timer"-------
        for thisComponent in begin_timerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "begin_timer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "start_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        start_routine_triggerComponents = []
        for thisComponent in start_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = start_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_routine_trigger"-------
        for thisComponent in start_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "start_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        cb_game_block = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='cb_game_block')
        thisExp.addLoop(cb_game_block)  # add the loop to the experiment
        thisCb_game_block = cb_game_block.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCb_game_block.rgb)
        if thisCb_game_block != None:
            for paramName in thisCb_game_block:
                exec('{} = thisCb_game_block[paramName]'.format(paramName))
        
        for thisCb_game_block in cb_game_block:
            currentLoop = cb_game_block
            # abbreviate parameter names if possible (e.g. rgb = thisCb_game_block.rgb)
            if thisCb_game_block != None:
                for paramName in thisCb_game_block:
                    exec('{} = thisCb_game_block[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "cyberball_1"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            holder = 1
            player_img = "images/start.bmp"
            start.setImage(player_img)
            # keep track of which components have finished
            cyberball_1Components = [start, text_8, text_9]
            for thisComponent in cyberball_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cyberball_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cyberball_1"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cyberball_1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cyberball_1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if force_end_routine or timer.getTime() <= 0:
                    continueRoutine=False
                    cyberball_trials.finished=True
                
                # *start* updates
                if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    start.frameNStart = frameN  # exact frame index
                    start.tStart = t  # local t and not account for scr refresh
                    start.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
                    start.setAutoDraw(True)
                if start.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > start.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        start.tStop = t  # not accounting for scr refresh
                        start.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(start, 'tStopRefresh')  # time at next scr refresh
                        start.setAutoDraw(False)
                
                # *text_8* updates
                if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_8.frameNStart = frameN  # exact frame index
                    text_8.tStart = t  # local t and not account for scr refresh
                    text_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(True)
                if text_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_8.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_8.tStop = t  # not accounting for scr refresh
                        text_8.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                        text_8.setAutoDraw(False)
                
                # *text_9* updates
                if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_9.frameNStart = frameN  # exact frame index
                    text_9.tStart = t  # local t and not account for scr refresh
                    text_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(True)
                if text_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_9.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_9.tStop = t  # not accounting for scr refresh
                        text_9.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                        text_9.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cyberball_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cyberball_1"-------
            for thisComponent in cyberball_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # set up handler to look after randomisation of conditions etc
            cb_trials_2 = data.TrialHandler(nReps=task_parameters['cb_throws'], method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='cb_trials_2')
            thisExp.addLoop(cb_trials_2)  # add the loop to the experiment
            thisCb_trial_2 = cb_trials_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisCb_trial_2.rgb)
            if thisCb_trial_2 != None:
                for paramName in thisCb_trial_2:
                    exec('{} = thisCb_trial_2[paramName]'.format(paramName))
            
            for thisCb_trial_2 in cb_trials_2:
                currentLoop = cb_trials_2
                # abbreviate parameter names if possible (e.g. rgb = thisCb_trial_2.rgb)
                if thisCb_trial_2 != None:
                    for paramName in thisCb_trial_2:
                        exec('{} = thisCb_trial_2[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "cyberball_2"-------
                continueRoutine = True
                # update component parameters for each repeat
                
                s = 1
                img_length = 3
                
                if holder == 2:
                    core.wait(0.01)
                else:
                    core.wait(random.randint(500, 3500)/1000)
                    img_length = .2
                
                player = select_throw(holder, block_threshold)
                holder = player[0]
                next_holder = player[1]
                
                player_img = select_player_image(holder, next_holder, s)
                
                nreps = len(throw["%ito%i" % (holder,next_holder)])
                
                #print("current holder: ", holder, "next_holder: ", next_holder, "Key: ", "%ito%i" % (holder,next_holder), "nreps:", nreps)
                image_2.setImage(player_img)
                cb_key_resp.keys = []
                cb_key_resp.rt = []
                _cb_key_resp_allKeys = []
                # keep track of which components have finished
                cyberball_2Components = [image_2, cb_key_resp, text_4, text_5]
                for thisComponent in cyberball_2Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                cyberball_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "cyberball_2"-------
                while continueRoutine:
                    # get current time
                    t = cyberball_2Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=cyberball_2Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    if (holder == 2) and (key_resp.keys == 'num_4' or key_resp.keys == 'num_add'):
                        continueRoutine = False
                        
                    if force_end_routine or timer.getTime() <= 0:
                        continueRoutine=False
                        cyberball_trials.finished=True
                    
                    # *image_2* updates
                    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_2.frameNStart = frameN  # exact frame index
                        image_2.tStart = t  # local t and not account for scr refresh
                        image_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                        image_2.setAutoDraw(True)
                    if image_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_2.tStartRefresh + img_length-frameTolerance:
                            # keep track of stop time/frame for later
                            image_2.tStop = t  # not accounting for scr refresh
                            image_2.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                            image_2.setAutoDraw(False)
                    
                    # *cb_key_resp* updates
                    waitOnFlip = False
                    if cb_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cb_key_resp.frameNStart = frameN  # exact frame index
                        cb_key_resp.tStart = t  # local t and not account for scr refresh
                        cb_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cb_key_resp, 'tStartRefresh')  # time at next scr refresh
                        cb_key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(cb_key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(cb_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if cb_key_resp.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > cb_key_resp.tStartRefresh + img_length-frameTolerance:
                            # keep track of stop time/frame for later
                            cb_key_resp.tStop = t  # not accounting for scr refresh
                            cb_key_resp.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(cb_key_resp, 'tStopRefresh')  # time at next scr refresh
                            cb_key_resp.status = FINISHED
                    if cb_key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = cb_key_resp.getKeys(keyList=['2','3'], waitRelease=False)
                        _cb_key_resp_allKeys.extend(theseKeys)
                        if len(_cb_key_resp_allKeys):
                            cb_key_resp.keys = _cb_key_resp_allKeys[-1].name  # just the last key pressed
                            cb_key_resp.rt = _cb_key_resp_allKeys[-1].rt
                    
                    # *text_4* updates
                    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_4.frameNStart = frameN  # exact frame index
                        text_4.tStart = t  # local t and not account for scr refresh
                        text_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                        text_4.setAutoDraw(True)
                    if text_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_4.tStartRefresh + img_length-frameTolerance:
                            # keep track of stop time/frame for later
                            text_4.tStop = t  # not accounting for scr refresh
                            text_4.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                            text_4.setAutoDraw(False)
                    
                    # *text_5* updates
                    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_5.frameNStart = frameN  # exact frame index
                        text_5.tStart = t  # local t and not account for scr refresh
                        text_5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                        text_5.setAutoDraw(True)
                    if text_5.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_5.tStartRefresh + img_length-frameTolerance:
                            # keep track of stop time/frame for later
                            text_5.tStop = t  # not accounting for scr refresh
                            text_5.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                            text_5.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in cyberball_2Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "cyberball_2"-------
                for thisComponent in cyberball_2Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if cb_key_resp.keys in ['', [], None]:  # No response was made
                    cb_key_resp.keys = None
                cb_trials_2.addData('cb_key_resp.keys',cb_key_resp.keys)
                if cb_key_resp.keys != None:  # we had a response
                    cb_trials_2.addData('cb_key_resp.rt', cb_key_resp.rt)
                # the Routine "cyberball_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                cb_trials = data.TrialHandler(nReps=nreps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='cb_trials')
                thisExp.addLoop(cb_trials)  # add the loop to the experiment
                thisCb_trial = cb_trials.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisCb_trial.rgb)
                if thisCb_trial != None:
                    for paramName in thisCb_trial:
                        exec('{} = thisCb_trial[paramName]'.format(paramName))
                
                for thisCb_trial in cb_trials:
                    currentLoop = cb_trials
                    # abbreviate parameter names if possible (e.g. rgb = thisCb_trial.rgb)
                    if thisCb_trial != None:
                        for paramName in thisCb_trial:
                            exec('{} = thisCb_trial[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "cyberball_3"-------
                    continueRoutine = True
                    routineTimer.add(0.150000)
                    # update component parameters for each repeat
                    player_img = select_player_image(holder, next_holder, s)
                    
                    image_3.setImage(player_img)
                    # keep track of which components have finished
                    cyberball_3Components = [text_6, text_10, image_3]
                    for thisComponent in cyberball_3Components:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    cyberball_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    
                    # -------Run Routine "cyberball_3"-------
                    while continueRoutine and routineTimer.getTime() > 0:
                        # get current time
                        t = cyberball_3Clock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=cyberball_3Clock)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        if force_end_routine or timer.getTime() <= 0:
                            continueRoutine=False
                            cyberball_trials.finished=True
                        
                        # *text_6* updates
                        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_6.frameNStart = frameN  # exact frame index
                            text_6.tStart = t  # local t and not account for scr refresh
                            text_6.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                            text_6.setAutoDraw(True)
                        if text_6.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_6.tStartRefresh + .15-frameTolerance:
                                # keep track of stop time/frame for later
                                text_6.tStop = t  # not accounting for scr refresh
                                text_6.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                                text_6.setAutoDraw(False)
                        
                        # *text_10* updates
                        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_10.frameNStart = frameN  # exact frame index
                            text_10.tStart = t  # local t and not account for scr refresh
                            text_10.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                            text_10.setAutoDraw(True)
                        if text_10.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > text_10.tStartRefresh + .15-frameTolerance:
                                # keep track of stop time/frame for later
                                text_10.tStop = t  # not accounting for scr refresh
                                text_10.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                                text_10.setAutoDraw(False)
                        
                        # *image_3* updates
                        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            image_3.frameNStart = frameN  # exact frame index
                            image_3.tStart = t  # local t and not account for scr refresh
                            image_3.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                            image_3.setAutoDraw(True)
                        if image_3.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > image_3.tStartRefresh + .15-frameTolerance:
                                # keep track of stop time/frame for later
                                image_3.tStop = t  # not accounting for scr refresh
                                image_3.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                                image_3.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in cyberball_3Components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "cyberball_3"-------
                    for thisComponent in cyberball_3Components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    s+=1
                    thisExp.nextEntry()
                    
                # completed nreps repeats of 'cb_trials'
                
                
                # ------Prepare to start Routine "cyberball_4"-------
                continueRoutine = True
                routineTimer.add(0.150000)
                # update component parameters for each repeat
                image_4.setImage(player_img)
                # keep track of which components have finished
                cyberball_4Components = [image_4, text_11, text_18]
                for thisComponent in cyberball_4Components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                cyberball_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "cyberball_4"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = cyberball_4Clock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=cyberball_4Clock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    if force_end_routine or timer.getTime() <= 0:
                        continueRoutine=False
                        cyberball_trials.finished=True
                    
                    # *image_4* updates
                    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_4.frameNStart = frameN  # exact frame index
                        image_4.tStart = t  # local t and not account for scr refresh
                        image_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                        image_4.setAutoDraw(True)
                    if image_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_4.tStartRefresh + .15-frameTolerance:
                            # keep track of stop time/frame for later
                            image_4.tStop = t  # not accounting for scr refresh
                            image_4.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                            image_4.setAutoDraw(False)
                    
                    # *text_11* updates
                    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_11.frameNStart = frameN  # exact frame index
                        text_11.tStart = t  # local t and not account for scr refresh
                        text_11.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                        text_11.setAutoDraw(True)
                    if text_11.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_11.tStartRefresh + .15-frameTolerance:
                            # keep track of stop time/frame for later
                            text_11.tStop = t  # not accounting for scr refresh
                            text_11.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                            text_11.setAutoDraw(False)
                    
                    # *text_18* updates
                    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_18.frameNStart = frameN  # exact frame index
                        text_18.tStart = t  # local t and not account for scr refresh
                        text_18.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
                        text_18.setAutoDraw(True)
                    if text_18.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_18.tStartRefresh + .15-frameTolerance:
                            # keep track of stop time/frame for later
                            text_18.tStop = t  # not accounting for scr refresh
                            text_18.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
                            text_18.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in cyberball_4Components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "cyberball_4"-------
                for thisComponent in cyberball_4Components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                holder = next_holder
                s = 1
                thisExp.nextEntry()
                
            # completed task_parameters['cb_throws'] repeats of 'cb_trials_2'
            
            
            # ------Prepare to start Routine "cb_game_end"-------
            continueRoutine = True
            # update component parameters for each repeat
            text_19.setText("You have reached the end of game " + str(game_i) + ".\n\n Press SPACE to continue.")
            key_resp_10.keys = []
            key_resp_10.rt = []
            _key_resp_10_allKeys = []
            # keep track of which components have finished
            cb_game_endComponents = [text_19, key_resp_10]
            for thisComponent in cb_game_endComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            cb_game_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "cb_game_end"-------
            while continueRoutine:
                # get current time
                t = cb_game_endClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=cb_game_endClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_19* updates
                if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_19.frameNStart = frameN  # exact frame index
                    text_19.tStart = t  # local t and not account for scr refresh
                    text_19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
                    text_19.setAutoDraw(True)
                
                # *key_resp_10* updates
                waitOnFlip = False
                if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_10.frameNStart = frameN  # exact frame index
                    key_resp_10.tStart = t  # local t and not account for scr refresh
                    key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                    key_resp_10.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_10.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_10_allKeys.extend(theseKeys)
                    if len(_key_resp_10_allKeys):
                        key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                        key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cb_game_endComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "cb_game_end"-------
            for thisComponent in cb_game_endComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            game_i += 1
            # the Routine "cb_game_end" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'cb_game_block'
        
        
        # ------Prepare to start Routine "end_routine_trigger"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        end_routine_triggerComponents = []
        for thisComponent in end_routine_triggerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_routine_triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_routine_trigger"-------
        while continueRoutine:
            # get current time
            t = end_routine_triggerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_routine_triggerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_routine_triggerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_routine_trigger"-------
        for thisComponent in end_routine_triggerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "end_routine_trigger" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed sum([task_type=='cyberball_practice']) repeats of 'cyberball_trials'
    
    
    # ------Prepare to start Routine "increment_selection"-------
    continueRoutine = True
    # update component parameters for each repeat
    import asyncio
    import websockets
     
    async def increment():
        async with websockets.connect('ws://localhost:8000') as websocket:
            await websocket.send("next")
            response = await websocket.recv()
            print(response)
    if not force_end_routine and not pause_routine: # if user didn't give input
        asyncio.get_event_loop().run_until_complete(increment())
    # keep track of which components have finished
    increment_selectionComponents = []
    for thisComponent in increment_selectionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    increment_selectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "increment_selection"-------
    while continueRoutine:
        # get current time
        t = increment_selectionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=increment_selectionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in increment_selectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "increment_selection"-------
    for thisComponent in increment_selectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "increment_selection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999.0 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
endComponents = [end_text, key_resp_3]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
