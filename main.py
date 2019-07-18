import pyglet

window = pyglet.window.Window(visible=False)

context = window.context
config = context.config

x = 1280
y = 720

window.set_minimum_size(x, y)
window.set_size(x, y)
window.set_caption('police-game')
window.set_visible()

pyglet.app.run()