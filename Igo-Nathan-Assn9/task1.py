import turtle
class Face:
    # Constructor:
    def __init__(self, tr, emotion, mouth, eyes):
        self.tr = tr
        self.emotion = emotion
        self.mouth = mouth
        self.eyes = eyes
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
    # Initial canvas function:
    def draw_face(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
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
        if self.__happy():
            return True
        else:
            return False
    def isDarkEyes(self):
        if self.__darkEyes():
            return True
        else:
            return False
    ################################################
    # Change functions:
    def changeMouth(self):
        if self.mouth == "smile":
            self.__smile = False
            self.draw_face()
        else:
            self.__smile = True
            self.draw_face()
    def changeEmotion(self):
        if self.emotion == "happy":
            self.__happy = False
            self.draw_face()
        else:
            self.__happy = True
            self.draw_face()

        self.draw_face()
    def changeEyes(self):
        if self.eyes == "Black":
            self.__darkEyes == False
            self.draw_face()
        else:
            self.__darkEyes == True
            self.draw_face()

        self.draw_face()
    ##################################################
    # drawing methods for draw_face
    '''
    I wonder if having an if else statement is really necessary here.
    '''
    def __drawHead(self):
        if self.__happy:
            self.tr.goto(-100, -100)
            self.tr.fillcolor("yellow")
            self.tr.pendown()
            self.tr.begin_fill()
            self.tr.circle(100)
            self.tr.end_fill()
            self.tr.penup()
        else:
            self.tr.goto(-100, -100)
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

        #self.tr.goto(-130, 50)
        for i in range(2):
            self.tr.goto(-130 + (i * 80), 40)
            self.tr.pendown()
            self.tr.begin_fill()
            self.tr.circle(10)
            self.tr.end_fill()
            self.tr.penup()


        # Draw mouth checks if moody should frown or smile.
        # Boolean values changed by changeMouth.
    def __drawMouth(self):
        self.tr.pensize(7)
        if self.__smile:
            self.tr.goto(-175, -10)
            self.tr.setheading(270)
            self.tr.pendown()
            self.tr.circle(75, 180)
            self.tr.penup()
        else:
            self.tr.goto(-100, -100)
            self.tr.setheading(90)
            self.tr.pendown()
            self.tr.circle(75, 180)
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