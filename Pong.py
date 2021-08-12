# Jacob McClure
# Python program to create a simple game of pong
print("READY TO PLAY PONG?\nYour goal is to try to score on your opponent by getting a ball "
      "past your opponent to the other side.\nThe Red player on top moves with the left with "
      "the 'a' key and right the 'd' key.\nThe Blue player on bottom moves with the 'left' and "
      "'right' arrow keys.\nIf you score on your opponent, you will get a point and the ball "
      "will reset.\nIf your opponent scores on you, they will get a point and the ball will "
      "reset.\nIt will reset quickly in the opposite direction so be ready! First one to 10 wins!!")

import turtle
import time
time.sleep(15)                    # wait 15 seconds for game to start so players can read instructions
wn = turtle.Screen()              # open a turtle graphics window
wn.setup(width=600, height=600)   # screen size
wn.title("Pong")                  # title of the game displayed
x_ball = 0                        # x position of the ball
y_ball = 0                        # y position of the ball
scorePlayerA = 0                  # blue player score
scorePlayerB = 0                  # red player score
x_limit, y_limit = 300, 300       # x and y screen limits
x_move, y_move = 5, 5


class Entity(turtle.Turtle):
    """define the entities ball and platform"""
    def __init__(self, x, y):
        super().__init__()
        self.speed(10)
        self.up()
        self.goto(x, y)


class Platform(Entity):
    """bounces the ball upward"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape("square")      # creates a square platform
        self.shapesize(.5, 3)     # changes it to a rectangle

    def rights(self):
        self.forward(20)          # how fast platform moves

    def lefts(self):
        self.back(20)             # how fast platform moves

    def checkposition(self):      # don't allow for it to run off the screen
        if self.xcor() >= 270:
            self.goto(270, self.ycor())
        if self.xcor() <= -270:
            self.goto(-270, self.ycor())


class Ball(Entity):
    """The ball to bounce in the screen"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shape("circle")
        self.left(100)

    def move(self):
        # allows use of global variables
        global x_ball, y_ball, x_move, y_move, x_limit, y_limit, scorePlayerA, scorePlayerB
        x_ball = x_ball + x_move  # change in x position of ball
        y_ball = y_ball + y_move  # change in y position of ball

        # blue scores a point
        if y_limit +60 <= y_ball:
            scorePlayerA += 1
            print("The Blue Player: ", scorePlayerA)
            print("The Red Player: ", scorePlayerB)

            # blue player wins and the game exits if blue score = 10
            if scorePlayerA == 10:
                print("Game Over! Blue wins!")
                exit()

            # reset ball
            else:
                x_ball = 0
                y_ball = 0
                x_move = -x_move       # reverse x direction
                y_move = -y_move       # reverse y direction
                time.sleep(1.5)        # wait 1.5 seconds for the ball to reset

        # red scores a point
        if y_ball <= -y_limit -60:
            scorePlayerB += 1
            print("The Blue Player: ", scorePlayerA)
            print("The Red Player: ", scorePlayerB)

            # red player wins and the game exits if red score = 10
            if scorePlayerB == 10:
                print("Game Over! Red wins!")
                exit()

            # reset ball
            else:
                y_ball = 0
                x_move = -x_move       # reverse x direction
                y_move = -y_move       # reverse y direction
                time.sleep(1.5)        # wait 1.5 seconds for the ball to reset

        # bounce off the sides of the screen
        if not -x_limit < x_ball < x_limit:
            x_move = -x_move           # reverse direction on x-plane
        self.goto(x_ball,y_ball)       # move to new position


BallA = Ball(0, 0)    # generate Ball A
PlatformA = Platform(-240, -240)       # generate platform A on bottom
PlatformA.color("blue")                # bottom player is blue
PlatformB = Platform(240, 240)         # generate platform B on top
PlatformB.color("red")                 # top player is red
wn.onkey(PlatformA.rights, "Right")    # respond to right key input
wn.onkey(PlatformA.lefts, "Left")      # respond to left key input
wn.onkey(PlatformB.rights,"d" or "D")  # respond to d key input
wn.onkey(PlatformB.lefts,"a" or "A")   # respond to a key input
wn.listen()


def movingball():
    """"makes the BallA.move go on a timer"""
    global y_move

    # if ball hits bounds of platform, it will bounce back in the y direction
    if PlatformA.xcor()-40 <= BallA.xcor() <= PlatformA.xcor()+40 and BallA.ycor() == PlatformA.ycor() + 15:
        y_move = -y_move

    # if ball hits bounds of platform, it will bounce back in the y direction
    if PlatformB.xcor()-40 <= BallA.xcor() <= PlatformB.xcor()+40 and BallA.ycor() == PlatformB.ycor() - 15:
        y_move = -y_move

    wn.ontimer(BallA.move(), 1)
    wn.update()
    wn.ontimer(movingball, 1)
    PlatformA.checkposition()
    PlatformB.checkposition()

wn.update()
wn.ontimer(movingball, 1)
wn.mainloop()
