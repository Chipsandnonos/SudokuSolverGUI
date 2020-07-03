from graphics import *

class Tile():

    def __init__(self,  window, pointx, pointy):
        self.px = pointx
        self.py = pointy
        self.win = window
        self.tile = Rectangle(self.px,self.py)
        self.tile.setFill("white")
        self.val = Text(self.tile.getCenter(), "")
        self.val.setFill("black")

    def draw (self):
        self.tile.draw(self.win)
        self.val.draw(self.win)
    def undraw (self):
        self.undraw()

