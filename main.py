from graphics import *
import board
import button
import final_algorithm

#Fix the redo part

win = GraphWin("Sudoku Solver", 500, 650)
win.setBackground("black")

b = board.Board(win,Point(25,25),50)
b.drawboard()

solveb = button.Button(win, Point(25,25+450+10),Point(25 + 212.5,25+450+10+25),"pink","pink","Solve")
resetb = button.Button(win, Point(25+25+212.5,25+450+10),Point(25+25+212.5+212.5,25+450+10+25),"pink","pink","Reset Board")
quitb = button.Button(win,Point(225,620), Point(275,640), "pink", "pink", "Quit" )
solveb.draw()
resetb.draw()
quitb.draw()

namelabel = Text(Point(450,650-12.5),"By Rahul.G")
namelabel.setTextColor("pink")
namelabel.draw(win)

howlabel = Text(Point(250,525+50),"Click on cell you want to edit and type, backspace will delete current cell value")
howlabel.setSize(10)
howlabel.setTextColor("white")
howlabel.draw(win)

warnlabel = Text(Point(250,550+50),"*Due to graphics processing, computationaly difficult sudokus may take a while to solve")
warnlabel.setSize(9)
warnlabel.setTextColor("red")
warnlabel.draw(win)

solvelabel = Text(Point(250,540),"")
solvelabel.setSize(20)
solvelabel.draw(win)

quit = False
while (quit != True):
    click_point = win.getMouse()
    if (b.wasclicked(click_point) == True):
        b.clicked(click_point)
    elif (solveb.is_pressed(click_point) == True):
        solvelabel.setTextColor("yellow")
        solvelabel.setText("Solving...")
        algo = final_algorithm.Algorithm(b.numboard,b)
        algo.run()
        solvelabel.setTextColor("green")
        solvelabel.setText("Solved")
    elif (resetb.is_pressed(click_point) == True):
        b.reset()
        solvelabel.setText("")

    elif (quitb.is_pressed(click_point) == True):
        quit = True


#need to add is possible, is suceed and clean code