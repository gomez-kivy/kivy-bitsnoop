
 # Copyright (c) 2014 Gomez.
 # All rights reserved.

 # Redistribution and use in source and binary forms are permitted
 # provided that the above copyright notice and this paragraph are
 # duplicated in all such forms and that any documentation,
 # advertising materials, and other materials related to such
 # distribution and use acknowledge that the software was developed
 # by the silverhawk.  The name of the
 # silverhawk may not be used to endorse or promote products derived
 # from this software without specific prior written permission.
 # THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
 # IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
 # WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import kivy
kivy.require('1.0.8')
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import *
from kivy.uix.boxlayout import *
from kivy.uix.label import *
from kivy.app import App
from kivy.core.image import Image 
from kivy.graphics import Rectangle

class ImageWidget(Widget):

    def on_touch_down(self, touch): 
        print("Displaying ImageWidget...")
        self.image = Image('./pics/rogue-48x48.png', keep_data=True)
        self.texture = self.image.texture
        self.pos = (0,0)
        ### self.label = super(Label, Label(text='Hello World')).__init__(**self.args)
        ### self.canvas.add(Label(text='Hello World')
        ### Label(text='Hello World'))
        self.button1 = Button(background_color=[88,88,0,40])
        self.button1.bind(on_press=self.callback1)
        self.button1.width = 100
        self.button2 = Button(background_color=[0,88,0,40])
        self.button2.bind(on_press=self.callback2)
        with self.canvas:
            self.box = BoxLayout(orientation='horizontal')
            self.box.width = 400
            self.box.add_widget(self.button1)
            self.box.add_widget(self.button2)
            Rectangle(texture=self.texture, pos=self.pos, size=(48,48))
           
    def callback1(instance):
        print("button _<%S> is pressed" % instance.text)

    def callback2(instance):
        print("button _<%S> is pressed" % instance.text)
