# FinalProjectUsefulCodeRepo
Example code and snippets to help developing your final projects.

### Remember: You can only have 20% of your final code as borrowed code. Please site all code modified or borrowed from the links below.

### Links:
Below are a list of useful links to help you with specific problems
- Flocking example (boids). Written in JAVASCRIPT, but useful math! https://eater.net/boids
- Turning a gif animation into an image stack (use with: animated backgrounds): https://stackoverflow.com/questions/9988517/resize-gif-animation-pil-imagemagick-python?rq=1
*Requires installation of images2gif. In your commandline enter: pip install images2gif then use the script!*
- How to draw a petal: https://pythonturtle.academy/tutorial-drawing-a-flower-petal-or-a-leaf-with-python-turtle/
- Easiest way to make naturalistic shapes like ISLANDS, RIVERS, and MOUNTIAN RIDGELINES is to use **Perlin noise** (examples: https://medium.com/quick-code/generating-random-3d-terrain-with-python-c344ae16e5c1/) I recommend using the perlin-noise module which can be downloaded using:
    `pip install perlin-noise`
    And can be imported using: `from perlin_noise import perlinNoise`. Example code is below.
- Random track/maze generation (no interaction): https://trinket.io/python/2d45f43e73
- Random track/maze generation (no interaction): https://pythonturtle.academy/random-maze-generator/
- How to open a webpage in a browser from a button in python: http://net-informations.com/python/net/browser.htm (*example code coming soon*)

### Example Code:
There's also code in this repo for solutions/tools many of you will find useful.
- **soundFix.py** - YOU MUST FIRST INSTALL PYGAME by typing: `pip install pygame` in the command console of Spyder. Then, you can run the code to hear music and click to play sound effects. You MUST initialize the mixer to get sound to play. This is the 3rd line of code: `mixer.init()`
- **dragBubbles.py** - example function to use for dragging. YOU MUST use the format shown in the function definition (`ondrag(None)` `...` `ondrag(func)`)
- **setImage.py** - how to set the Screen and/or turtle as an imported image.
- **img2gif.py** - converts images into a compatible filetype (.gif). [FIXED! It now allows shrinking (0.25, 0.5 scale values)]
- **collisionBubbles.py** - getting turtles to bump into each other and change direction. Uses center positions, so collisions involve a little crossover of images. You'll have to tweak it to get it to bounce at shape edges.
- **turtleTextbox.py** - creates a clickable text box that writes, deletes and stores text entered into the box. Some editing is required to get it to work for all letters. Instructions are stated at the top of the script.
- **islandMountains.py** - Example uses **perlin-noise library** to create islands with snowy peaks, and a naturalistic line that can be used to make rivers, hillsides and mountain scapes. *NOTE: This code is SLOW to run!*

### Libraries:
Download these and import them into your files! **These files have to be in the same folder as the .py file that's importing them.** To see a demo, download the file and run it. To look at example code, check out what's written in the `if __name__=='__main__'` code block.
- **timer.py** - This library has methods for making a countdown timer bar that ticks down across the page, and a numerical countdown timer.
- **boundary.py** - This library has methods that allows for screen edge interaction, and how to draw and collide with walls.
