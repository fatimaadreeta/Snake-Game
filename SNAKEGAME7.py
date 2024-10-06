import turtle
import time
import random

turtle.setup(600,600)
##Setting up the screen
s = turtle.Screen()
s.title("Snake Game 3")
s.bgcolor("beige")
s.tracer(0) #To stop update the screen

##The Snake Head
h = turtle.Turtle()
h.speed(0)
h.pensize(5)
h.shape("square")
h.shapesize(2,2,3)
h.color("thistle1", "springgreen3")
h.penup()
h.goto(0,100)
h.direction = "stop"

#The snake food
f = turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("firebrick1")
f.penup()
f.shapesize(1.5,1.5)
f.goto(0,0)
#Another Food
ff = f.clone()


#score display
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,310)


#Snake's body
segments = []
def move():
    if h.direction == "up":
        y = h.ycor() ##Y Cordinate
        h.sety(y + 20)
    elif h.direction == "down":
        y = h.ycor()
        h.sety(y - 20)
    elif h.direction == "right":
         x = h.xcor()
         h.setx(x + 20)
    elif h.direction == "left":
         x = h.xcor()
         h.setx(x - 20)

def go_up():
    if h.direction != "down":
        h.direction = "up"
def go_down():
    if h.direction != "up":
        h.direction = "down"
def go_right():
    if h.direction != "left":
        h.direction = "right"
def go_left():
    if h.direction != "right":
        h.direction = "left"

s.listen() #Everything happening on the screen, We will listen to it
s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_right, "Right")
s.onkey(go_left, "Left")
delay = 0.1

#Main Game Loop
while True:
    s.update()
    pen.clear()
    pen.write("Score : {} / High Score : {}".format(score,high_score),
              align="center",font=("Niagara Engraved", 30, "normal"))

    ##If the snake comes in contact with the food
    if h.distance(f)<20:
        score = score + 1
        if score > high_score:
            high_score = score
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        f.goto(x,y)
        

        #Add the body part
        ns = turtle.Turtle()
        ns.speed(0)
        ns.shape("square")
        ns.shapesize(1.8,1.8,2.8)
        ns.color("thistle1", "springgreen3")
        ns.penup()
        segments.append(ns)

    ##If the snake comes in contact with the duplicate food
    if h.distance(ff)<20:
        score = score + 1
        if score > high_score:
            high_score = score
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        ff.goto(x,y)
        

        #Add the body part
        ns = turtle.Turtle()
        ns.speed(0)
        ns.shape("square")
        ns.shapesize(1.8,1.8,2.8)
        ns.color("thistle1", "springgreen3")
        ns.penup()
        segments.append(ns)

    #Body follow the head
    l = len(segments)-1 
    for index in range(l,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Leader Part
    if len(segments) > 0:
        x = h.xcor()
        y = h.ycor()
        segments[0].goto(x,y)
    move()
    #Check for collision with the border
    if h.xcor()> 660 or h.xcor()< -660 or h.ycor()> 320 or h.ycor()< -320:
        time.sleep(1)
        h.goto(0,0)
        h.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #Remove all body part
        segments.clear()

        #Resetting Score
        score = 0
        pen.clear()
        pen.write("Score : {} / High Score : {}".format(score,high_score),
                  align="center",font=("Niagara Engraved", 30, "normal"))

    time.sleep(delay)





 
