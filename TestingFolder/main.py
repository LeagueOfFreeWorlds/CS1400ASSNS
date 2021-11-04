from modules.chessboard import chessboard
import turtle
def main():
    tr = turtle.Turtle()
    tr.speed(0)
    cb1 = chessboard(100, -50, 75, 100, "blue", tr)
    cb1.drawChessboard()

    turtle.done()
main()
