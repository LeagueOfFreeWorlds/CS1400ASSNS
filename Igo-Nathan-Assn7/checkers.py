import turtle
continueRunning = "yes"
def validateInput(width, height, starting):
    if width=="" or height=="" or not type(int):
        print("Sorry, please reenter input and try again")
        return False
    else:
        return True
# Draws the chessboard square:
def drawChessboard(width, height):
    turtle.pendown()
    turtle.color("red")
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.penup()
    turtle.setheading(0)
#Draws a checker tile when called:
def checkers():
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.penup()
    # Function asks for user input, and also runs other checker functions:
def runCheckerDrawer(continueRunning):
    # Program will continue to run as long as the user inputs a value for continueRunning that satisfiese the while loop:
    while continueRunning == "yes" or continueRunning == "y" or continueRunning == "YES" or continueRunning == "Y" or continueRunning == "":
        # Variables are created for the program:
        blockCount = 0
        secBlockCount = 0
        xWSize = 0
        yWSize = 0
        # Asking user for input on location and size of checkerboard on display:
        startSpot = eval(input("Enter your starting location in x, y coordinates (x, y):    "))
        wSize = input("Enter the width of your checker board:   ")
        hSize = input("Enter the height of your checker board:  ")
        # Preferrably, turtle arrow is hidden
        turtle.hideturtle()
        # clear function useful for when user wants to rerun program so that the canvas is cleared every time the while loop is repeated:
        turtle.clear()
        turtle.penup()
        turtle.speed(10)
        # checks boolean output of function:
        if validateInput(wSize, hSize, startSpot) == False:
            continueRunning = ""
        else:
            # Width and height are assumed as integers if they successfully pass validation:
            wSize = abs(int(wSize))
            hSize = abs(int(hSize))
            turtle.goto(startSpot)
            drawChessboard(wSize, hSize)
            # checker length = 10 + space between checker tiles(10) = 20
            checkerSideDim = 20
            checkerArea = (checkerSideDim ** 2)
            # Get coordinates of starting point:
            x = turtle.xcor() - checkerSideDim
            xOrig = turtle.xcor() - checkerSideDim
            y = turtle.ycor()
            # For second row of checkers, take the original coordinates and increase the x and y values by the actual checker size:
            ySecCheck = turtle.ycor() + (checkerSideDim / 2)
            # Calculates number of tiles that can fit within the checkerboard:
            checkerDim = round((wSize * hSize) / checkerArea)
            # Maximum number of tiles that can fit within the range of the width:
            checkerMWidth = round((wSize) / checkerSideDim)
            # Maximum number of tiles that can fit within the range of the height:
            checkerMHeight = round((hSize) / checkerSideDim)
            # If the blockCount (number of blocks that can fit within the board) isn't satisfied, then the program will continue to print
            # more tiles to the board:
            while blockCount < checkerDim:
                if (xWSize + checkerSideDim) <= wSize and (yWSize + checkerSideDim) <= hSize:
                    x = x + checkerSideDim
                    xWSize = xWSize + checkerSideDim
                    turtle.goto(x, y)
                    checkers()
                    blockCount = blockCount + 1
                # once tiles have reached their maximum width, they have to move on to the next row and start again:
                elif (xWSize + checkerSideDim) > wSize and (yWSize + checkerSideDim) < hSize:
                    y = y + checkerSideDim
                    x = xOrig
                    xWSize = 0
                    yWSize = yWSize + checkerSideDim
                # if board is filled with the maximum number of tiles available, while loop will prematurely end:
                else:
                    blockCount = checkerDim
            turtle.penup()
            # Second while statement to print second set of checkers:
            turtle.goto(xOrig, ySecCheck)
            x = xOrig + 10
            y = ySecCheck
            xWSize = 0
            yWSize = 0
            # While loop identical to the last, just shifted to fit second set of tiles.
            while secBlockCount < (checkerDim + checkerSideDim):
                if (xWSize + checkerSideDim) <= wSize and (yWSize + checkerSideDim) <= hSize:
                    x = x + checkerSideDim
                    xWSize = xWSize + checkerSideDim
                    turtle.goto(x, ySecCheck)
                    checkers()
                    secBlockCount = secBlockCount + 1
                elif (xWSize + checkerSideDim) > wSize and (yWSize + checkerSideDim) < hSize:
                    ySecCheck = ySecCheck + checkerSideDim
                    x = xOrig + 10
                    xWSize = 0
                    yWSize = yWSize + checkerSideDim
                else:
                    secBlockCount = (checkerDim + checkerSideDim)
                # User can choose if they want to restart the program:
        continueRunning = input("Would you like to restart the program?     ")
