class chessboard:
    def __init__(self, xPos, yPos, width, height, color, tr):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.color = color
        self.tr = tr
    def drawRectangle(self, width, height):
        self.tr.pendown()
        self.tr.begin_fill()
        for i in range(2):
            self.tr.forward(width)
            self.tr.left(90)
            self.tr.forward(height)
            self.tr.left(90)
        self.tr.end_fill()
        self.tr.penup()
    def drawChessboard(self):
        self.tr.penup()
        self.tr.goto(self.xPos, self.yPos)
        self.tr.fillcolor("white")
        self.drawRectangle(self.width, self.height)
        self.tr.penup()
        self.drawAllRectangles()

    def drawAllRectangles(self):
        self.tr.fillcolor(self.color)
        for i in range(8):
            self.tr.goto(self.xPos, self.yPos + i * self.height / 8)
            if i % 2 == 1:
                self.tr.forward(self.width / 8)
            for j in range(4):
                self.drawRectangle(self.width / 8, self.height / 8)
                self.tr.forward(self.width / 4)