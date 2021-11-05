import turtle
class Face:
    # Constructor:
    def __init__(self, tr, emotion, mouth, eyes):
        self.tr = tr
        self.tr.speed(0)
        self.emotion = emotion
        self.mouth = mouth
        self.eyes = eyes
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
    # Initial canvas function:
    def draw_face(self):
        self.tr.reset()
        self.tr.penup()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()
    # Boolean return statements for the display:
    def isSmile(self):
        if self.__smile:
            return True
        else:
            return False
    def isHappy(self):
        if self.__happy:
            return True
        else:
            return False
    def isDarkEyes(self):
        if self.__darkEyes:
            return True
        else:
            return False
    ################################################
    # Change functions:
    def changeMouth(self):
        if self.__smile == True:
            self.__smile = False
            self.draw_face()
        else:
            self.__smile = True
            self.draw_face()
    def changeEmotion(self):
        if self.__happy == True:
            self.__happy = False
            self.draw_face()
        else:
            self.__happy = True
            self.draw_face()

    def changeEyes(self):
        if self.__darkEyes == True:
            self.__darkEyes = False
            self.draw_face()
        else:
            self.__darkEyes = True
            self.draw_face()


    ##################################################
    # drawing methods for draw_face

    def __drawHead(self):
        self.tr.goto(-100, -100)
        if self.__happy:
            self.tr.fillcolor("yellow")
            self.tr.pendown()
            self.tr.begin_fill()
            self.tr.circle(100)
            self.tr.end_fill()
            self.tr.penup()
        else:
            self.tr.fillcolor("red")
            self.tr.pendown()
            self.tr.begin_fill()
            self.tr.circle(100)
            self.tr.end_fill()
            self.tr.penup()

    def __drawEyes(self):
        if self.__darkEyes:
            self.tr.fillcolor("black")
        else:
            self.tr.fillcolor("blue")

        for i in range(2):
            self.tr.goto(-140 + (i * 80), 37)
            self.tr.pendown()
            self.tr.begin_fill()
            self.tr.circle(10)
            self.tr.end_fill()
            self.tr.penup()


        # Draw mouth checks if moody should frown or smile.
        # Boolean values changed by changeMouth.
    def __drawMouth(self):
        self.tr.pensize(9)
        if self.__smile == True:
            self.tr.goto(-175, 0)
            self.tr.setheading(270)
            self.tr.pendown()
            self.tr.circle(75, 180)
            self.tr.penup()
        elif self.__smile == False:
            self.tr.goto(-30, -50)
            self.tr.setheading(90)
            self.tr.pendown()
            self.tr.circle(70, 180)
            self.tr.penup()
        self.tr.pensize(1)
##########################################################

def main():
    # Turtle object:
    tr = turtle.Turtle()
    tr.penup()
    ###################
    # face object instantiation:
    face = Face(tr, "happy", "smile", "black")
    face.draw_face()
    ############################
    done = False
    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")
        menu = eval(input("Enter a selection: "))
        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break
    print("Thanks for Playing")
    turtle.hideturtle()
    turtle.done()
main()