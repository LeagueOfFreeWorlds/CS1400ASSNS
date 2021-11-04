'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

#### Add Import Statement(s) as needed ####
import turtle
import patterns
#### End Add Import Statement(s) ####

def main():
    # Setup pattern
    patterns.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter starting coordinates (x, y):   "))
            offset = int(input("How much offset do you want?   "))
            radius = int(input("What radius should your pattern have?  "))
            width = int(input("How much width do you want your rectangles?    "))
            height = int(input("How much height do you want your rectangles?   "))
            count = int(input("What is the number of rectangles that you want in your rectangle pattern?  "))
            rotation = int(input("What rotation do you want your rectangles to be at?  "))
            #### End Add Inputs Statement(s) ####

            # Draw the rectangle pattern
            patterns.drawRectanglePattern(centerX, centerY, width, height, offset, radius, count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter starting coordinates (x, y):   "))
            offset = eval(input("How much offset do you want?   "))
            circleSize = eval(input("What size do you want your circles to be?"))
            radius = eval(input("What do you want your radius to be?"))
            count = eval(input("What is the number of rectangles that you want in your rectangle pattern?  "))
            #### End Add Inputs Statement(s) ####

            # Draw the circle pattern
            patterns.drawCirclePattern(centerX, centerY, circleSize, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            randAmount = input("Enter number of patterns:   ")
            #### End Add Inputs Statement(s) ####
            if randAmount == "":
                patterns.drawSuperPattern()
            else:
                patterns.drawSuperPattern(eval(randAmount))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))
        if response == 3:
            exit()
            # print a message saying thank you
            print("Thanks for playing!")
            patterns.done()
        else:
            #### Add Statement(s) to clear drawings and play again ####
            drawings = input("Would you like to keep drawings?  ")
            if drawings == "yes":
                turtle.penup()
                turtle.goto(0, 0)
                turtle.setheading(0)
            else:
                patterns.setup()

            #### End Add Inputs Statement(s) ####
main()
