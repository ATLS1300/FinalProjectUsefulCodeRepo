#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:13:54 2020

@author: Dr. Z

Assigning images to SCREEN and TURTLE. Requires example image files (galaxy.gif
    and rocket.gif)

Turtle ONLY works with .gif format images. To convert you MUST use img2gif.py
Saving files and changing extentions won't work. Sometimes saving files as
.gif from Adobe Photoshop/Illustrator is also problematic. img2gif is surefire.

"""
import turtle

panel = turtle.Screen()

# use variable names for images
galaxyBG = 'Circinus_Galaxy.gif'
rocket = 'rocket.gif'

# import images to panel
panel.addshape(galaxyBG)
panel.addshape(rocket)

# Set image as background (you will have to change the size of your image OR panel
# to get it to look nice. You can resize images using img2gif.py)
panel.bgpic(galaxyBG)

rocketTurt = turtle.Turtle()
rocketTurt.shape(rocket)

turtle.done()