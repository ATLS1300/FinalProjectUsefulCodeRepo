#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:49:02 2020

@author: sazamore

1. install pygame by typing the following in the command console -->
pip install pygame

2. then run this code for an example of sound playing.
    
"""
import turtle
import pygame.mixer as mixer
mixer.init() # start the mixer in order to get sound to play


panel = turtle.Screen()
panel.setup()

oofTurt = turtle.Turtle(visible=False)
oofTurt.up()
oofTurt.goto(-200,0)
oofTurt.write('oof!',font=('Courier',40))

boingTurt = turtle.Turtle(visible=False)
boingTurt.up()
boingTurt.goto(100,0)
boingTurt.write('boing!',font=('Courier',40))

# FOR BACKGROUND MUSIC or SINGLE SOUND FX

# Load music using file name (.mp3 or .wav are fine!)
soundfile = "tech.wav" # change to your file
mixer.music.load(soundfile)

# Play the song
mixer.music.play()

# Stop the song
#mixer.music.stop()


# FOR MULTIPLE SOUND FX or MULTIPLE SOUND TRACKS
oof = "oof.wav"
bounce = "boing.wav"

def playFX(x,y):
    if x<0:
     mixer.Channel(0).play(mixer.Sound(oof))
    else:
     mixer.Channel(1).play(mixer.Sound(bounce))
     
panel.onclick(playFX)

panel.mainloop()
turtle.done()