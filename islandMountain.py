"""
Created on Sat Dec  5 19:39:14 2020

@author: Dr. Z

Using the perlin-noise library, creates Map (2D) and 
then a mountain ridgeline (1D).

                              STOP!

You must FIRST install the PERLIN_NOISE LIBRARY by typing the following
into the command line on the right:
    pip install perlin-noise
    
Note it is a dash not underscore to install, but an underscore to import. (eyeroll)

Note this is NOT OOP, or organized into functions. You will have to do that...

For islands:
    PerlinNoise arguments:
        dimensions = 2 (default)
        octaves = any number between 1 and 12 (less than 10 is "natural")
    Break up values between -0.25 and 0.25. Play around with ranges until you get your desired result
    
For lines:
    PerlinNoise arguments:
        dimensions = 1 
        octaves = any number between 1 and 10.
    Use a for loop to make the constant path (horizontal or vertical), then use
    the noise object to make the other dimenstion (veritcal or horizontal, respectively).
"""

from perlin_noise import PerlinNoise
import turtle

turtle.tracer(0)

panel = turtle.Screen()
w = 500
h = 500
panel.setup()
panel.bgcolor('skyblue')


# drawing a naturalistic line
def naturaLine(octaves=9, y=200,scale=60):
    '''Makes a HORIZONTAL naturalistic line, like a mountain range or river
    using perlin nosie. For more riverlike look, increase the number of octaves.)'''
    
    noise = PerlinNoise(octaves=octaves)
    x_pix = w # width of line
    
    outline = turtle.Turtle()
    outline.up()
    outline.color('gray40')
    outline.goto(-int(w/2),y-30) # start lower to fill in below the peaks
    
    outline.begin_fill()
    outline.goto(-int(w/2),y)
    
    
    for i in range(w):
        yval = noise(i/int(x_pix))
        outline.goto(i-int(w/2),yval*scale+y)
        outline.down()
        panel.update() # animates the line being drawn.
        
    outline.goto(int(w/2),y-30) # move down to fill in below the peaks
    outline.end_fill()
    outline.ht()
    panel.update()

# drawing Map/Islands

def islands(octaves=4,x_pix=200,y_pix=200):
    '''Draws islands using perlin noise. 
    Octave - increasing this will increases "peakiness" of islands.
    x_pix - width (pixels) inside which ilsands are drawn
    y_pix - height (pixels) inside which islands are drawn
    
    THERE ARE INTENIONAL BAD VARIABLE NAMES USED.
    '''
    noise = PerlinNoise(octaves=octaves)
    
    Map = turtle.Turtle(shape='circle')
    Map.up()
    
    color1 = 'sienna' # this is a bad name..what are you using this to color in your image?
    color2 = 'darkgreen'
    color3 = 'aliceblue'
    
    # This loop can be a bit slow. Be patient!
    for j in range(x_pix):
        for i in range(y_pix):
            
            val = noise([i/int(w/2), j/int(h/2)]) # returns values between -.2 and +.2
            
            # print(val)
            Map.goto(i-int(x_pix/2),j-int(y_pix/2))
            if 0.25 <= val:
                Map.color(color3) # "mountain"
                Map.stamp()
            elif 0.01 <= val < 0.2:
                Map.color(color2) # "grass"
                Map.stamp()
            elif 0 < val < 0.01: # increase these numbers to make smaller "islands"
                Map.color(color1) # "ground"
                Map.stamp()
                
    Map.ht()        
    panel.update()
    
naturaLine()   
islands()

turtle.done()