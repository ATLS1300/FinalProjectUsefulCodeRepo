#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:32:12 2020

@author: Dr. Z

turtle text box, great for use with interactive games, entering names, etc.
stores text entered to the attribute text.

run code to see what it does, import as module to work with it.
 
Click on the screen to activate (does not specify the box being clicked on)
type a to make demo letters, type 1 to delete  (the turtle doesn't detect the delete key.)
       
     NOTE! To get this to work for all letters, you'll have to duplicate the
     self.TypeA with different letters!!! (So make TypeB, TypeC, TypeD,...,TypeZ)                                          
                                                
"""
import turtle, string

panel=turtle.Screen()
turtle.setup(500,500)

panel.listen()
turtle.tracer(0)


class textBox:
#attributes: colors, the size, the font
#methods: pulling data, draw
    def __init__(self, size=(100, 30)):
      self.input_box = turtle.Turtle(shape='square') 
      self.textWriter = turtle.Turtle(visible=False)

      #set colors for my input box
      self.color_inactive = 'lightskyblue3'
      self.color_active = 'dodgerblue2'
      self.color = self.color_inactive # color reporter
      self.active = False # activity boolean
      self.letter = 'a'
      
      self.text = '' #default text (empty)
      self.font = ('Arial', 32)
      self.size = size
      self.text = ''
      self.rect(size[0],size[1])
      
      panel.onkeypress(self.TypeA, 'a')
      panel.onkeypress(self.delete,'1')
      panel.onclick(self.activate)
      
      
    def rect(self,w=100,h=30):
        self.input_box.color(self.color)
        for i in range(2):
            self.input_box.forward(w)
            self.input_box.left(90)
            self.input_box.forward(h)
            self.input_box.left(90)
            self.input_box.ht()
            panel.update()
    
    def activate(self,x,y):
        self.active = not self.active
        self.input_box.clear()
        if self.active:
            self.color = self.color_active
            self.rect()
        else:
            self.color = self.color_inactive
            self.rect()
            
    def TypeA(self):
        if self.active:
            print('type!')
            letter = 'a'
            self.textWriter.write(letter, align='left', font=self.font)
            self.textWriter.forward(self.font[1]/2) # TODO: scale with font size.
            self.text+=letter
            panel.update()
    
            
    def delete(self):
        print('delete!')
        # for i in range(len(self.text)):
        if self.active:
            if len(self.text)>0:
                self.textWriter.backward((self.font[1]/2)*len(self.text))
                self.text = self.text[:-1]
    
                self.textWriter.clear()
                panel.update()
                for let in self.text:
                    self.textWriter.write(let, align='left', font=self.font)
                    self.textWriter.forward(self.font[1]/2) # TODO: scale with font size.
                panel.update()
        
if __name__=='__main__':
    box = textBox()
    panel.mainloop()
    turtle.done()
            