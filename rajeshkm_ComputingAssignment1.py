

import turtle
import math
import time
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Hide and Seek"


turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
t = turtle.Turtle()

# Start of your code
# Start of your code

# ------------------

screen.tracer(0)

## snowflake
def bigsnowflake():
    for i in range(8):
        t.pencolor("white")

        t.fd(20)
        t.backward(5)
        t.right(30)
        t.fd(10)
        t.backward(10)
        t.left(60)
        t.fd(10)
        t.backward(10)
        t.right(30)
        #second

        t.backward(7.5)
        t.right(30)
        t.fd(8)
        t.backward(8)
        t.left(60)
        t.fd(8)
        t.backward(8)
        t.right(30)
        t.backward(7.5)
        t.fd(25)
        t.backward(25)
        t.right(45)

def smallsnowflake():
    for i in range(8):
        t.pencolor(0.95,0.92,1)

        t.fd(12)
        t.backward(2)
        t.backward(5/2)
        t.right(30)
        t.fd(10/2)
        t.backward(10/2)
        t.left(60)
        t.fd(10/2)
        t.backward(10/2)
        t.right(30)
        #second

        t.backward(7.5/2)
        t.right(30)
        t.fd(8/2)
        t.backward(8/2)
        t.left(60)
        t.fd(8/2)
        t.backward(8/2)
        t.right(30)
        t.backward(7.5/2)
        t.fd(14)
        t.backward(14)
        t.right(45)

##splash screen
screen.bgcolor(0.058,0.0039, 0.301)
t.color("white")
t.write("CODE AND SEEK (WINTER THEME!!)", align="center", font=("Courier", 25, "bold"))
t.penup()
t.goto(0,-40)
t.pendown()
t.write("1.Allow Player 1 to choose a secret location for the target while Player 2 looks away ", align="center", font=("Courier", 12, "italic"))
t.penup()
t.goto(0,-60)
t.pendown()
t.write(" 2.Player 2 has 4 tries to guess the coordinate", align="center", font=("Courier", 12, "italic"))
a=random.randint(-450,450)
b=random.randint(-225,225)

def snowflakes_splash(a,b):
    for i in range (100):

        t.penup()
        t.goto(a,b)
        t.pendown()
        t.pensize(2.4)
        bigsnowflake()
        a+=60

snowflakes_splash(-450,-150)
snowflakes_splash(-450,150)


screen.update()

time.sleep(2)

##background gradient

x=0.15
t.penup()
t.goto(-450,222)
t.pendown()


for i in range(12):

    t.fillcolor(0, 0, x)
    t.pencolor(0,0,x)
    t.begin_fill()
    #rectangle for fill
    for j in range(2):
        t.forward(900)
        t.right(90)
        t.fd(30)
        t.right(90)
    t.end_fill()


    t.right(90)
    t.forward(30)
    t.left(90)
    x = x + 0.035

##Snow on ground
t.pencolor(0.97,0.96,0.93 )
t.fillcolor(0.97,0.96,0.93 )
t.begin_fill()
t.goto(-1125,-1100)
t.right(90)
t.circle(1040)
t.end_fill()

t.penup()
t.goto(825,-605)
t.left(180)
t.pendown()
t.fillcolor(0.97,0.96,0.93 )
t.begin_fill()
t.circle(540)
t.end_fill()






##snowflake
for i in range (40):
    a=random.randrange(-450,450)
    b=random.randrange(-50,225)
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.pensize(1)

    smallsnowflake()



##snowman
def snowman():
    t.pencolor("white")
    t.right(90)
    t.penup()

    t.pendown()
    t.dot(50)
    t.left(90)
    t.fd(45)
    t.dot(40)
    t.fd(15)
    t.left(90)
    t.backward(16)
    #scarf
    for j in range(2):
        t.pencolor("darkorchid4")
        t.fillcolor("darkorchid4")
        t.begin_fill()
        t.fd(32)
        t.right(90)
        t.fd(8)
        t.right(90)
        t.end_fill()
    t.penup()
    t.pencolor("white")
    t.fd(16)
    t.right(90)
    t.fd(20)

    t.dot(30)
    t.penup()
    t.backward(60)
    t.pendown()
    t.pencolor("black")
    t.penup()
    t.fd(8)
    t.pendown()

    #snowman accessories
    #button
    for i in range(3):
        t.penup()
        t.fd(10)
        t.dot(5)
        t.pendown()
    #nose and eyes
    t.penup()
    t.fd(20)
    t.pendown()
    t.pencolor("orange")
    t.dot(5)

    t.penup()
    t.right(45)
    t.fd(10)
    t.pendown()
    t.pencolor("black")
    t.dot(5)
    t.left(135)
    t.penup()
    t.fd(12)
    t.pendown()
    t.dot(5)

    t.pensize(1)
    #hat
    t.penup()
    t.right(90)
    t.fd(10)
    t.pendown()
    t.right(90)
    t.fd(20)
    t.backward(28)
    t.left(90)
    t.color("black")
    t.begin_fill()
    for i in range(2):
        t.fd(4)
        t.right(90)
        t.fd(28)
        t.right(90)

    t.fd(4)
    t.right(90)
    t.fd(7)
    t.left(90)
    for i in range(4):
        t.fd(15)
        t.right(90)


    t.end_fill()

    t.penup()


#snowman location
def snowmanlocation(a,b):
    for i in range (9):
        d=(200)
        t.penup()
        t.goto(a,b)
        t.pendown()
        snowman()
        a+=d
snowmanlocation(-400,-90)
snowmanlocation(-300,-200)




##location finding
x=turtle.numinput("Hiding loaction", "x coordinate")
y=turtle.numinput("Hiding loaction", "y coordinate")
highestscore=0
for i in range(4):
    a=turtle.numinput(" Guess hiding loaction", "x coordinate guess")
    b=turtle.numinput("Guess hiding loaction", "y coordinate guess")
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.pencolor("red")
    distance=round(((x-a)**2 + (y-b)**2)**(1/2),2)
    score1=max(0,((200-distance)**2)/4000)
    score=round(score1,2)
    highestscore = max(highestscore, score)
    t.dot(15)
    t.write(f"location {i+1}, distance= {distance}, {score}", font=("courier", 10, "bold"))
    screen.update()





time.sleep(5)
screen.clearscreen()




##display score

screen.bgcolor(0.058,0.0039, 0.301)
t.color("white")

t.goto(-400,0)
t.write(f"   YOUR HIGHEST SCORE IS {highestscore}!!!", font=("courier", 25, "bold"))
t.penup()
t.goto(270,10)
t.pendown()
bigsnowflake()

screen.update()








# TO DO Need to make change for clear exit without crash



# ------------------
# End of your code here

# Make a clean exit
screen.exitonclick()