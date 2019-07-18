import pyglet
from pyglet.gl import *

window = pyglet.window.Window(visible=False)

context = window.context
config = context.config

x = 1280
y = 720

state = {
    'Fullscreen' : False
}

window.set_minimum_size(x, y)
window.set_size(x, y)
window.set_caption('police-game')
window.set_visible()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.F12:
        if state['Fullscreen'] == False:
            print('Switching to fullscreen mode')
            state['Fullscreen'] = True
            window.set_fullscreen(True)
        else:
            print('Switching to windowed mode')
            state['Fullscreen'] = False
            window.set_fullscreen(False)

pyglet.app.run()