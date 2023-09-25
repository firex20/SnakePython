import turtle
import time
import random

delay = 0.1
body_segments = []

wn = turtle.Screen()

# Title
wn.title("Juego Snake")
# Window size
wn.setup(width=600, height=600)
# Background color
wn.bgcolor("light blue")

# Head settings

# Turtle obj
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food config
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)

def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"

wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")


while True:
    wn.update()

    if head.distance(food) <= 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        body_segments.append(new_segment)

    totalSeg = len(body_segments)

    #for i in range(totalSeg - 1, 0, -1)


    mov()
    time.sleep(delay)

turtle.done()
