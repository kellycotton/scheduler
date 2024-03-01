#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri Mar  1 08:16:56 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'cyberball'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kellycotton/Dropbox/Research/N3/cyberball_lastrun.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "game_start"
game_startClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In the upcoming task, we will test the effects of practicing mental visualization on task performance. Thus, we need you to practice your mental visualization skills. We have found that the best way to do this is to have you play an on-line ball tossing game with other participants who are logged on to the system at the same time.\n\nIn a few moments, you will be playing a ball-tossing game with other students over our network. Several universities in the state of New York are taking part in a collaborative investigation of the effects of mental visualization on task performance, with people participating at several different universities around the state of New York.\n\nPress SPACE to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "instruct_2"
instruct_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='The game is very simple. When the ball is tossed to you, simply press either the "2" key (pointer finger) to throw to the player on your left or the "3" key (middle finger) for to throw to the player on your right. When the game is over, the experimenter will give you additional instructions.\n\nWhat is important is not your ball tossing performance, but that you MENTALLY VISUALIZE the entire experience. Imagine what the others look like. What sort of people are they? Where are you playing? Is it warm and sunny or cold and rainy? Create in your mind a complete mental picture of what might be going on if you were playing this game in real life.\n\nPress SPACE to start.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "practice_start"
practice_startClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text="Let's begin the practice. Remember, when it's your turn to throw, press the XXX key to throw to Player 3 and the XXX key to throw the ball to Player 3.\n\nReady?",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

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
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
key_resp_5 = keyboard.Keyboard()
text_22 = visual.TextStim(win=win, name='text_22',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "prac_cb_3"
prac_cb_3Clock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
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

# Initialize components for Routine "practice_end"
practice_endClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='You have finished the practice.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "loading"
loadingClock = core.Clock()
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
text_7 = visual.TextStim(win=win, name='text_7',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "cyberball_2"
cyberball_2Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
key_resp = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "cyberball_3"
cyberball_3Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-3.0)

# Initialize components for Routine "cyberball_4"
cyberball_4Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='Player 2',
    font='Open Sans',
    pos=(-.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='Player 3',
    font='Open Sans',
    pos=(.2, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "block_end"
block_endClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
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
        while len(choice)==0 or choice [0] not in ('2','3'):
            choice = event.getKeys(keyList=['2','3'])
        if choice[0]=='2':
            throwTo=1
        elif choice[0]=='3':
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
setupComponents = []
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

# ------Prepare to start Routine "game_start"-------
continueRoutine = True
# update component parameters for each repeat
game_i = 1
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
game_startComponents = [text, key_resp_2]
for thisComponent in game_startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
game_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "game_start"-------
while continueRoutine:
    # get current time
    t = game_startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=game_startClock)
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
    for thisComponent in game_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "game_start"-------
for thisComponent in game_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "game_start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruct_2Components = [text_2, key_resp_3]
for thisComponent in instruct_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruct_2"-------
while continueRoutine:
    # get current time
    t = instruct_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_2Clock)
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
    for thisComponent in instruct_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_2"-------
for thisComponent in instruct_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_block = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_block')
thisExp.addLoop(practice_block)  # add the loop to the experiment
thisPractice_block = practice_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
if thisPractice_block != None:
    for paramName in thisPractice_block:
        exec('{} = thisPractice_block[paramName]'.format(paramName))

for thisPractice_block in practice_block:
    currentLoop = practice_block
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
    if thisPractice_block != None:
        for paramName in thisPractice_block:
            exec('{} = thisPractice_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    block_threshold = .8
    # keep track of which components have finished
    practice_startComponents = [text_28, key_resp_6]
    for thisComponent in practice_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_start"-------
    while continueRoutine:
        # get current time
        t = practice_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_startClock)
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
        for thisComponent in practice_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_start"-------
    for thisComponent in practice_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_block.addData('text_28.started', text_28.tStartRefresh)
    practice_block.addData('text_28.stopped', text_28.tStopRefresh)
    # the Routine "practice_start" was not non-slip safe, so reset the non-slip timer
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
    practice_block.addData('start_3.started', start_3.tStartRefresh)
    practice_block.addData('start_3.stopped', start_3.tStopRefresh)
    practice_block.addData('text_20.started', text_20.tStartRefresh)
    practice_block.addData('text_20.stopped', text_20.tStopRefresh)
    practice_block.addData('text_21.started', text_21.tStartRefresh)
    practice_block.addData('text_21.stopped', text_21.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    prac_cb_trials_2 = data.TrialHandler(nReps=10.0, method='random', 
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
        image_4.setImage(player_img)
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        prac_cb_2Components = [image_4, key_resp_5, text_22, text_23]
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
                if tThisFlipGlobal > image_4.tStartRefresh + img_length-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(False)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_5.tStartRefresh + img_length-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_5.tStop = t  # not accounting for scr refresh
                    key_resp_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                    key_resp_5.status = FINISHED
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['2','3'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            
            # *text_22* updates
            if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_22.frameNStart = frameN  # exact frame index
                text_22.tStart = t  # local t and not account for scr refresh
                text_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
                text_22.setAutoDraw(True)
            if text_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_22.tStartRefresh + img_length-frameTolerance:
                    # keep track of stop time/frame for later
                    text_22.tStop = t  # not accounting for scr refresh
                    text_22.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
                    text_22.setAutoDraw(False)
            
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
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        prac_cb_trials_2.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            prac_cb_trials_2.addData('key_resp_5.rt', key_resp_5.rt)
        prac_cb_trials_2.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        prac_cb_trials_2.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        prac_cb_trials_2.addData('text_22.started', text_22.tStartRefresh)
        prac_cb_trials_2.addData('text_22.stopped', text_22.tStopRefresh)
        prac_cb_trials_2.addData('text_23.started', text_23.tStartRefresh)
        prac_cb_trials_2.addData('text_23.stopped', text_23.tStopRefresh)
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
            
            image_5.setImage(player_img)
            # keep track of which components have finished
            prac_cb_3Components = [text_24, text_25, image_5]
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
                    if tThisFlipGlobal > text_24.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        text_24.tStop = t  # not accounting for scr refresh
                        text_24.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
                        text_24.setAutoDraw(False)
                
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
                    if tThisFlipGlobal > image_5.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_5.tStop = t  # not accounting for scr refresh
                        image_5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                        image_5.setAutoDraw(False)
                
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
            prac_cb_trials.addData('text_24.started', text_24.tStartRefresh)
            prac_cb_trials.addData('text_24.stopped', text_24.tStopRefresh)
            prac_cb_trials.addData('text_25.started', text_25.tStartRefresh)
            prac_cb_trials.addData('text_25.stopped', text_25.tStopRefresh)
            prac_cb_trials.addData('image_5.started', image_5.tStartRefresh)
            prac_cb_trials.addData('image_5.stopped', image_5.tStopRefresh)
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
        prac_cb_trials_2.addData('image_6.started', image_6.tStartRefresh)
        prac_cb_trials_2.addData('image_6.stopped', image_6.tStopRefresh)
        prac_cb_trials_2.addData('text_26.started', text_26.tStartRefresh)
        prac_cb_trials_2.addData('text_26.stopped', text_26.tStopRefresh)
        prac_cb_trials_2.addData('text_27.started', text_27.tStartRefresh)
        prac_cb_trials_2.addData('text_27.stopped', text_27.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'prac_cb_trials_2'
    
    
    # ------Prepare to start Routine "practice_end"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    practice_endComponents = [text_29, key_resp_7]
    for thisComponent in practice_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_end"-------
    while continueRoutine:
        # get current time
        t = practice_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_endClock)
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
        for thisComponent in practice_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_end"-------
    for thisComponent in practice_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_block.addData('text_29.started', text_29.tStartRefresh)
    practice_block.addData('text_29.stopped', text_29.tStopRefresh)
    # the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_block'


# ------Prepare to start Routine "loading"-------
continueRoutine = True
routineTimer.add(13.000000)
# update component parameters for each repeat
# keep track of which components have finished
loadingComponents = [text_12, text_13, text_14, text_17, text_15, text_16]
for thisComponent in loadingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
loadingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "loading"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = loadingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=loadingClock)
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
    for thisComponent in loadingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "loading"-------
for thisComponent in loadingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)

# set up handler to look after randomisation of conditions etc
game_block = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('routine_conditions/cyberball.csv'),
    seed=None, name='game_block')
thisExp.addLoop(game_block)  # add the loop to the experiment
thisGame_block = game_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGame_block.rgb)
if thisGame_block != None:
    for paramName in thisGame_block:
        exec('{} = thisGame_block[paramName]'.format(paramName))

for thisGame_block in game_block:
    currentLoop = game_block
    # abbreviate parameter names if possible (e.g. rgb = thisGame_block.rgb)
    if thisGame_block != None:
        for paramName in thisGame_block:
            exec('{} = thisGame_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cyberball_1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    holder = 1
    player_img = "images/start.bmp"
    start.setImage(player_img)
    # keep track of which components have finished
    cyberball_1Components = [start, text_7, text_8]
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
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
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
    game_block.addData('start.started', start.tStartRefresh)
    game_block.addData('start.stopped', start.tStopRefresh)
    game_block.addData('text_7.started', text_7.tStartRefresh)
    game_block.addData('text_7.stopped', text_7.tStopRefresh)
    game_block.addData('text_8.started', text_8.tStartRefresh)
    game_block.addData('text_8.stopped', text_8.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    cb_trials_2 = data.TrialHandler(nReps=10.0, method='random', 
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
        image.setImage(player_img)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        cyberball_2Components = [image, key_resp, text_3, text_4]
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
            if (holder == 2) and (key_resp.keys == '2' or key_resp.keys == '3'):
                continueRoutine = False
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + img_length-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + img_length-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['2','3'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + img_length-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(False)
            
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
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        cb_trials_2.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            cb_trials_2.addData('key_resp.rt', key_resp.rt)
        cb_trials_2.addData('key_resp.started', key_resp.tStartRefresh)
        cb_trials_2.addData('key_resp.stopped', key_resp.tStopRefresh)
        cb_trials_2.addData('text_3.started', text_3.tStartRefresh)
        cb_trials_2.addData('text_3.stopped', text_3.tStopRefresh)
        cb_trials_2.addData('text_4.started', text_4.tStartRefresh)
        cb_trials_2.addData('text_4.stopped', text_4.tStopRefresh)
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
            
            image_2.setImage(player_img)
            # keep track of which components have finished
            cyberball_3Components = [text_5, text_6, image_2]
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
                    if tThisFlipGlobal > text_5.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                        text_5.setAutoDraw(False)
                
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
                    if tThisFlipGlobal > image_2.tStartRefresh + .15-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                        image_2.setAutoDraw(False)
                
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
            cb_trials.addData('text_5.started', text_5.tStartRefresh)
            cb_trials.addData('text_5.stopped', text_5.tStopRefresh)
            cb_trials.addData('text_6.started', text_6.tStartRefresh)
            cb_trials.addData('text_6.stopped', text_6.tStopRefresh)
            cb_trials.addData('image_2.started', image_2.tStartRefresh)
            cb_trials.addData('image_2.stopped', image_2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed nreps repeats of 'cb_trials'
        
        
        # ------Prepare to start Routine "cyberball_4"-------
        continueRoutine = True
        routineTimer.add(0.150000)
        # update component parameters for each repeat
        image_3.setImage(player_img)
        # keep track of which components have finished
        cyberball_4Components = [image_3, text_9, text_10]
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
                if tThisFlipGlobal > text_9.tStartRefresh + .15-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(False)
            
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
        cb_trials_2.addData('image_3.started', image_3.tStartRefresh)
        cb_trials_2.addData('image_3.stopped', image_3.tStopRefresh)
        cb_trials_2.addData('text_9.started', text_9.tStartRefresh)
        cb_trials_2.addData('text_9.stopped', text_9.tStopRefresh)
        cb_trials_2.addData('text_10.started', text_10.tStartRefresh)
        cb_trials_2.addData('text_10.stopped', text_10.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'cb_trials_2'
    
    
    # ------Prepare to start Routine "block_end"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_11.setText("You have reached the end of game " + str(game_i) + ".\n\n Press SPACE to continue.")
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    block_endComponents = [text_11, key_resp_4]
    for thisComponent in block_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_end"-------
    while continueRoutine:
        # get current time
        t = block_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        
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
        for thisComponent in block_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_end"-------
    for thisComponent in block_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    game_block.addData('text_11.started', text_11.tStartRefresh)
    game_block.addData('text_11.stopped', text_11.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    game_block.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        game_block.addData('key_resp_4.rt', key_resp_4.rt)
    game_block.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    game_block.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    game_i += 1
    # the Routine "block_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'game_block'


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
