
 # Copyright (c) 2014 silverhawk software.
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
from kivy.app import App
from kivy.core.image import Image 

from imagewidget import *

class BitSnoopKivyApp(App):
     def __init__(self, **kwargs):
        App.__init__(self)
        self.args = kwargs
        self.icon = './pics/rogue-48x48.png'

     def build(self):
        self.button = super(Button, Button()).__init__(**self.args)
        self.title = "Kivy - Rogue"
        self.imagewidget= ImageWidget()
        self.keyblistener = super(MyKeyboardListener, MyKeyboardListener(self.imagewidget)).__init__(**self.args)
        return self.imagewidget
 
class MyKeyboardListener(Widget):

    def __init__(self, imagewidget, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self.x = 0
        self.y = 0 
        self.imagewidget = imagewidget
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.args = kwargs

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

        if text == 'l':
            self.x += 1
            self.pos = self.imagewidget.pos
            self.pos = (self.x, self.y) 

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

if __name__ == '__main__':
     BitSnoopKivyApp().run()


    ###from kivy.base import runTouchApp
    ###runTouchApp(MyKeyboardListener())
