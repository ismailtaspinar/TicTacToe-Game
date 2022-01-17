from graphics import *
from random import choice

def tictac():
    win=GraphWin("19290331",300,350)
    win.setCoords(0.0,0.0,3.0,3.5)

    square={}

    sq1=Rectangle(Point(0.0,2.5),Point(1.0,3.5))
    sq1.draw(win)
    box1=None
    square.update({sq1:box1})

    sq2 = Rectangle(Point(1.0, 2.5), Point(2.0, 3.5))
    sq2.draw(win)
    box2 = None
    square.update({sq2: box2})

    sq3 = Rectangle(Point(2.0, 2.5), Point(3.0, 3.5))
    sq3.draw(win)
    box3 = None
    square.update({sq3: box3})

    sq4 = Rectangle(Point(0.0, 1.5), Point(1.0, 2.5))
    sq4.draw(win)
    box4 = None
    square.update({sq4: box4})

    sq5 = Rectangle(Point(1.0, 1.5), Point(2.0, 2.5))
    sq5.draw(win)
    box5 = None
    square.update({sq5: box5})

    sq6 = Rectangle(Point(2.0, 1.5), Point(3.0, 2.5))
    sq6.draw(win)
    box6 = None
    square.update({sq6: box6})

    sq7 = Rectangle(Point(0.0, 0.5), Point(1.0, 1.5))
    sq7.draw(win)
    box7 = None
    square.update({sq7: box7})

    sq8 = Rectangle(Point(1.0, 0.5), Point(2.0, 1.5))
    sq8.draw(win)
    box8 = None
    square.update({sq8: box8})

    sq9 = Rectangle(Point(2.0, 0.5), Point(3.0, 1.5))
    sq9.draw(win)
    box9 = None
    square.update({sq9: box9})

    messagebox=Rectangle(Point(0.0,0.0),Point(3.0,0.5))
    messagebox.draw(win)

    message=Text(messagebox.getCenter(),None).draw(win)

    count=0
    syc=False

    while True:
        try:
            p = win.getMouse()
        except GraphicsError:
            win.close()
            break

        for i in square.keys():
            if p.getX() >= i.getP1().getX() and p.getX() <= i.getP2().getX() and p.getY() >= i.getP1().getY() and p.getY() <= i.getP2().getY():
                click = i
        if square[click]==1 or square[click]==0:
            message.setText("You cannot click the filled squares!")
            continue
        else:
            Text(click.getCenter(),"x").draw(win)
            message.undraw()
            message = Text(messagebox.getCenter(), None).draw(win)
            square[click] = 1


        count += 1

        if list(square.values())[0] == 1 and list(square.values())[1] == 1 and list(square.values())[2] == 1:
            message.setText("X wins")
            break
        if list(square.values())[3] == 1 and list(square.values())[4] == 1 and list(square.values())[5] == 1:
            message.setText("X wins")
            break

        if list(square.values())[6] == 1 and list(square.values())[7] == 1 and list(square.values())[8] == 1:
            message.setText("X wins")
            break

        if list(square.values())[0] == 1 and list(square.values())[3] == 1 and list(square.values())[6] == 1:
            message.setText("X wins")
            break

        if list(square.values())[1] == 1 and list(square.values())[4] == 1 and list(square.values())[7] == 1:
            message.setText("X wins")
            break

        if list(square.values())[2] == 1 and list(square.values())[5] == 1 and list(square.values())[8] == 1:
            message.setText("X wins")
            break

        if list(square.values())[0] == 1 and list(square.values())[4] == 1 and list(square.values())[8] == 1:
            message.setText("X wins")
            break

        if list(square.values())[2] == 1 and list(square.values())[4] == 1 and list(square.values())[6] == 1:
            message.setText("X wins")
            break

        if list(square.values())[0] == 0 and list(square.values())[1] == 0 and list(square.values())[2] == 0:
            message.setText("O wins")
            break

        if list(square.values())[3] == 0 and list(square.values())[4] == 0 and list(square.values())[5] == 0:
            message.setText("O wins")
            break

        if list(square.values())[6] == 0 and list(square.values())[7] == 0 and list(square.values())[8] == 0:
            message.setText("O wins")
            break

        if list(square.values())[0] == 0 and list(square.values())[3] == 0 and list(square.values())[6] == 0:
            message.setText("O wins")
            break

        if list(square.values())[1] == 0 and list(square.values())[4] == 0 and list(square.values())[7] == 0:
            message.setText("O wins")
            break

        if list(square.values())[2] == 0 and list(square.values())[5] == 0 and list(square.values())[8] == 0:
            message.setText("O wins")
            break

        if list(square.values())[0] == 0 and list(square.values())[4] == 0 and list(square.values())[8] == 0:
            message.setText("O wins")
            break

        if list(square.values())[2] == 0 and list(square.values())[4] == 0 and list(square.values())[6] == 0:
            message.setText("O wins")
            break

        if count == 5:
            message.setText("Draw!")
            break

        while count < 5:
            ran = choice(list(square.keys()))
            if square[ran]==0 or square[ran]==1:
                continue
            else:
                Text(ran.getCenter(), "O").draw(win)
                square[ran]=0
                break

        if list(square.values())[0] == 1 and list(square.values())[1] == 1 and list(square.values())[2] == 1:
            message.setText("X wins")
            break
        if list(square.values())[3] == 1 and list(square.values())[4] == 1 and list(square.values())[5] == 1:
            message.setText("X wins")
            break

        if list(square.values())[6] == 1 and list(square.values())[7] == 1 and list(square.values())[8] == 1:
            message.setText("X wins")
            break

        if list(square.values())[0] == 1 and list(square.values())[3] == 1 and list(square.values())[6] == 1:
            message.setText("X wins")
            break

        if list(square.values())[2] == 1 and list(square.values())[5] == 1 and list(square.values())[8] == 1:
            message.setText("X wins")
            break

        if list(square.values())[1] == 1 and list(square.values())[4] == 1 and list(square.values())[7] == 1:
            message.setText("X wins")
            break

        if list(square.values())[0] == 1 and list(square.values())[4] == 1 and list(square.values())[8] == 1:
            message.setText("X wins")
            break

        if list(square.values())[2] == 1 and list(square.values())[4] == 1 and list(square.values())[6] == 1:
            message.setText("X wins")
            break

        if list(square.values())[0] == 0 and list(square.values())[1] == 0 and list(square.values())[2] == 0:
            message.setText("O wins")
            break

        if list(square.values())[3] == 0 and list(square.values())[4] == 0 and list(square.values())[5] == 0:
            message.setText("O wins")
            break

        if list(square.values())[6] == 0 and list(square.values())[7] == 0 and list(square.values())[8] == 0:
            message.setText("O wins")
            break

        if list(square.values())[0] == 0 and list(square.values())[3] == 0 and list(square.values())[6] == 0:
            message.setText("O wins")
            break

        if list(square.values())[2] == 0 and list(square.values())[5] == 0 and list(square.values())[8] == 0:
            message.setText("O wins")
            break

        if list(square.values())[1] == 0 and list(square.values())[4] == 0 and list(square.values())[7] == 0:
            message.setText("O wins")
            break

        if list(square.values())[0] == 0 and list(square.values())[4] == 0 and list(square.values())[8] == 0:
            message.setText("O wins")
            break

        if list(square.values())[2] == 0 and list(square.values())[4] == 0 and list(square.values())[6] == 0:
            message.setText("O wins")
            break

        if count == 5:
            message.setText("Draw!")
            break
    q=None
    try:
        q = win.getKey()

    except GraphicsError:
        win.close()


    if q == "q":
        win.close()


if __name__ == "__main__":
    tictac()





