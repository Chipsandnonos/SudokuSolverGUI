import tile
from graphics import *


class Block():

    def __init__(self,win,point,scale):
        self.px = point.getX()
        self.py = point.getY()
        self.scale = scale
        self.win = win
        self.tiles = []

        for y in range (3):
            for x in range (3):
                t = tile.Tile(self.win, Point(x*scale + self.px, y*scale + self.py), Point((x+1)*scale + self.px, (y+1)*scale + self.py))
                self.tiles.append(t)

    def draw(self):
        for i in range(len(self.tiles)):
            self.tiles[i].draw()





