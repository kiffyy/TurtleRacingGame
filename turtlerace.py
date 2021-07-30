from turtle import *
from random import *
import turtle
import time


#WINDOW SETUP
wn =(600,500)
wn= turtle.Screen()
wn.title('TURTLE RACE')
turtle.bgcolor('seagreen')
turtle.speed(0)

#heading
penup()
goto(-190,340)
color("black")
write("TURTLE RACE", font=('courier', 30, "bold"))
speed(0)


#track
goto(-350, 250)
pendown()
color("mistyrose")
begin_fill()
for i in range (2):
    forward(700)
    right(90)
    forward(550)
    right(90)
end_fill()



# FINISH LINE
gap_size= 25
shape ("square")
penup()

# squares row 1
color("white")
for i in range (10) :
    goto (250,(195 -(i * gap_size* 2)))
    stamp()


for i in range (10) :
    goto(250 + gap_size, (240 - gap_size)-(i * gap_size * 2))
    stamp()

#adding the black squares
color("black")
for i in range(10):
    goto(251, (220 - (i * gap_size * 2)))
    stamp()

for i in range (10) :
    goto(251 + gap_size, (220 - gap_size)-(i * gap_size * 2))
    stamp()


#TURTLE ONE  RED
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.6)
red_turtle.penup()
red_turtle.goto(-320, 190)
red_turtle.pendown()

#turtle two
blue_turtle = Turtle()
blue_turtle.color("aqua")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.6)
blue_turtle.penup()
blue_turtle.goto(-320, 120)
blue_turtle.pendown()


#TURTLE 3
lime_turtle = Turtle()
lime_turtle.color("lime")
lime_turtle.shape("turtle")
lime_turtle.shapesize(1.6)
lime_turtle.penup()
lime_turtle.goto(-320, 50)
lime_turtle.pendown()



#turtle 4
indigo_turtle = Turtle()
indigo_turtle.color("indigo")
indigo_turtle.shape("turtle")
indigo_turtle.shapesize(1.6)
indigo_turtle.penup()
indigo_turtle.goto(-320,-20)
indigo_turtle.pendown()



#turtler 5
pink_turtle = Turtle()
pink_turtle.color("orchid")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.6)
pink_turtle.penup()
pink_turtle.goto(-320,-90)
pink_turtle.pendown()



#turtle 6
orange_turtle = Turtle()
orange_turtle.color("darkorange")
orange_turtle.shape("turtle")
orange_turtle.shapesize(1.6)
orange_turtle.penup()
orange_turtle.goto(-320,-160)
orange_turtle.pendown()



#turtle 7
yellow_turtle = Turtle()
yellow_turtle.color("gold")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.6)
yellow_turtle.penup()
yellow_turtle.goto(-320,-230)
yellow_turtle.pendown()

# one second pause before racing
time.sleep(1)

while red_turtle.xcor() <= 250 and blue_turtle.xcor()<= 250 and lime_turtle.xcor()<= 250 and indigo_turtle.xcor()<= 250 and pink_turtle.xcor()<= 250 and orange_turtle.xcor()<= 250  and yellow_turtle.xcor()<= 250 :
    red_turtle.forward(randint(1, 10))
    blue_turtle.forward(randint(1,10))
    lime_turtle.forward(randint(1,10))
    indigo_turtle.forward(randint(1,10))
    pink_turtle.forward(randint(1, 10))
    orange_turtle.forward(randint(1, 10))
    yellow_turtle.forward(randint(1, 10))

 #WINNERS
if red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > lime_turtle.xcor() and red_turtle.xcor() > indigo_turtle.xcor() and red_turtle.xcor() >pink_turtle.xcor() and red_turtle.xcor() >orange_turtle.xcor() and red_turtle.xcor() > yellow_turtle.xcor:
    print("Red turtle wins")
    for i in range(75):
        red_turtle.right(5)
        red_turtle.shapesize(2.6)

elif pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > lime_turtle.xcor() and pink_turtle.xcor() > indigo_turtle.xcor() and pink_turtle.xcor() >red_turtle.xcor() and pink_turtle.xcor() > orange_turtle.xcor() and pink_turtle.xcor > yellow_turtle.xcor:
    print("Pink turtle wins")
    for i in range(75):
        pink_turtle.right(5)
        pink_turtle.shapesize(2.6)

elif blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > lime_turtle.xcor() and blue_turtle.xcor() > indigo_turtle.xcor() and blue_turtle.xcor() >pink_turtle.xcor() and blue_turtle.xcor() >orange_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor():
    print("Blue Wins")
    for i in range(75):
        blue_turtle.right(5)
        blue_turtle.shapesize(2.6)

elif lime_turtle.xcor() > red_turtle.xcor() and lime_turtle.xcor() > blue_turtle.xcor() and lime_turtle.xcor() > indigo_turtle.xcor() and lime_turtle.xcor() >pink_turtle.xcor() and lime_turtle.xcor() >orange_turtle.xcor() and lime_turtle.xcor() > yellow_turtle.xcor:
    print("lime wins")
    for i in range(75):
        lime_turtle.right(5)
        lime_turtle.shapesize(2.6)

elif indigo_turtle.xcor() > red_turtle.xcor() and indigo_turtle.xcor() > lime_turtle.xcor() and indigo_turtle.xcor() > lime_turtle.xcor() and indigo_turtle.xcor() > pink_turtle.xcor() and indigo_turtle.xcor() >orange_turtle.xcor() and indigo_turtle.xcor > yellow_turtle.xcor():
    print ("Purple Turtle wins")
    for i in range(75):
        indigo_turtle.right(5)
        indigo_turtle.shapesize(2.6)

elif orange_turtle.xcor() > red_turtle.xcor() and orange_turtle.xcor() > lime_turtle.xcor() and orange_turtle.xcor() > lime_turtle.xcor() and orange_turtle.xcor() > pink_turtle.xcor() and orange_turtle.xcor() > indigo_turtle.xcor and orange_turtle.xcor() > yellow_turtle.xcor:
    print("Orange Turtle wins")
    for i in range(75):
       orange_turtle.right(5)
       orange_turtle.shapesize(2.6)

elif yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() > lime_turtle.xcor() and yellow_turtle.xcor() > lime_turtle.xcor() and yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() >indigo_turtle.xcor()  and yellow_turtle.xcor() >orange_turtle:
    print("Yellow turtle wins")
    for i in range(75):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(2.6)

turtle.mainloop()