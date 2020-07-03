import block
from graphics import *
import math


class Board(): #make a game class, and put board in there

    def __init__(self, window, point, scale):
        self.win = window
        self.px = point.getX()
        self.py = point.getY()
        self.scale = scale
        self.blocks = []
        self.tiles = []
        self.numboard = []
        # PBOARD

        for y in range (3):
            for x in range (3):
                b = block.Block(self.win, Point(self.px + 150*x,self.py + 150*y),self.scale)
                self.blocks.append(b)

        for by in range(3):
            b1 = self.blocks[0 + by*3]
            b2 = self.blocks[1 + by*3]
            b3 = self.blocks[2 + by*3]
            for ty in range (3):
                row = []
                row.append(b1.tiles[0 + ty*3])
                row.append(b1.tiles[1 + ty * 3])
                row.append(b1.tiles[2 + ty * 3])

                row.append(b2.tiles[0 + ty * 3])
                row.append(b2.tiles[1+ ty * 3])
                row.append(b2.tiles[2 + ty * 3])

                row.append(b3.tiles[0 + ty * 3])
                row.append(b3.tiles[1 + ty * 3])
                row.append(b3.tiles[2 + ty * 3])
                self.tiles.append(row)

        for y in range (9):
            row = []
            for x in range (9):
                row.append(None)
            self.numboard.append(row)


    def drawboard (self):
        for i in range (len(self.blocks)):
            self.blocks[i].draw()
        line1d = Line(Point(self.px+ 150,self.py),Point(self.px+ 150, self.py+150*3))
        line2d = Line(Point(self.px + 300, self.py), Point(self.px + 300, self.py + 150 * 3))
        line1s = Line(Point(self.px , self.py + 150), Point(self.px + 450, self.py + 150 ))
        line2s = Line(Point(self.px, self.py + 300), Point(self.px + 450, self.py + 300))
        line1d.setWidth(5)
        line2d.setWidth(5)
        line1s.setWidth(5)
        line2s.setWidth(5)
        line1d.draw(self.win)
        line2d.draw(self.win)
        line1s.draw(self.win)
        line2s.draw(self.win)

    def wasclicked (self,point):
        x = point.getX()
        y = point.getY()

        if ((x >= self.px and x <= self.px + 9*self.scale) and (y >= self.py and y <= self.py + 9*self.scale)):
            return True
        else:
            return False

    def clicked (self, point):
        x = point.getX()
        y = point.getY()
        tx = math.floor((x - self.px)/self.scale)
        ty = math.floor((y - self.py) / self.scale)
        oldval = self.numboard[ty][tx]
        inp = self.win.getKey()
        add = False
        try:
            inp = int(inp)
            add = True
        except ValueError:
            if (inp == "BackSpace"):
                self.tiles[ty][tx].val.setText("")  # make it only back space, others will send a error msg
                self.numboard[ty][tx] = None
        if (add == True):
            self.numboard[ty][tx] = inp
            if(self.potential(ty,tx) == True): #Make an error msg if impossible input
                self.tiles[ty][tx].val.setText(inp)
            else:
                self.numboard[ty][tx] = oldval

    def potential(self, y,x):
        value = self.numboard[y][x]
        for column in range(9):
            if (column != y):
                if (self.numboard[column][x] == value):
                    return False
        for row in range(9):
            if (row != x):
                if (self.numboard[y][row] == value):
                    return False
        blockx = math.floor(x / 3)
        blocky = math.floor(y / 3)

        for column in range(3):
            for row in range(3):
                if not (blocky * 3 + column == y and blockx * 3 + row == x):
                    if (self.numboard[blocky * 3 + column][blockx * 3 + row] == value):
                        return False
        return True

    def reset (self):
        for y in range(9):
            for x in range(9):
                self.numboard[y][x] = None
                self.tiles[y][x].val.setText("")






