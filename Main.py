import pyglet
win= pyglet.window.Window()
import util

tile = pyglet.image.load('Legacy/PNG/terrainTile3.png')
spr = pyglet.sprite.Sprite(tile_img, x = 200 , y = 200 )

def update(dt):
    win.clear()



@win.event 
def on_draw ():
    util,pixelScale()
    spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run() 