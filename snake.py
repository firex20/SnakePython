import turtle
import time
import random

delay = 0.1
body_segments = []
score = 0
high_score = 0

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
head.shape("square")
head.shapesize(1.2, 1.2)
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

# Score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write(f'Score 0        High Score: 0', align="center", font=("ComicSans", 24))

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
        head.tiltangle(90)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
        head.tiltangle(270)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
        head.tiltangle(0)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)
        head.tiltangle(180)

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

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        wn.tracer(0)
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        body_segments = []
        wn.clearscreen()
        wn.bgcolor("light blue")
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.shapesize(1.2, 1.2)
        head.color("green")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"
        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0, 100)
        wn.listen()
        wn.onkeypress(dirUp, "Up")
        wn.onkeypress(dirDown, "Down")
        wn.onkeypress(dirRight, "Right")
        wn.onkeypress(dirLeft, "Left")
        score = 0
        text = turtle.Turtle()
        text.speed(0)
        text.color("white")
        text.penup()
        text.hideturtle()
        text.goto(0,260)
        text.write(f'Score 0        High Score: {high_score}', align="center", font=("ComicSans", 24))
        wn.update()

    if head.distance(food) <= 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        wn.tracer(0)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        body_segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f'Score {score}        High Score: {high_score}', align="center", font=("ComicSans", 24))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x,y)

    wn.update()

    mov()

    for segment in body_segments:
        if segment.distance(head) < 10:
            wn.tracer(0)
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            body_segments = []
            wn.clearscreen()
            wn.bgcolor("light blue")
            head = turtle.Turtle()
            head.speed(0)
            head.shape("square")
            head.shapesize(1.2, 1.2)
            head.color("green")
            head.penup()
            head.goto(0, 0)
            head.direction = "stop"
            food = turtle.Turtle()
            food.speed(0)
            food.shape("circle")
            food.color("red")
            food.penup()
            food.goto(0, 100)
            wn.listen()
            wn.onkeypress(dirUp, "Up")
            wn.onkeypress(dirDown, "Down")
            wn.onkeypress(dirRight, "Right")
            wn.onkeypress(dirLeft, "Left")
            score = 0
            text = turtle.Turtle()
            text.speed(0)
            text.color("white")
            text.penup()
            text.hideturtle()
            text.goto(0,260)
            text.write(f'Score 0        High Score: {high_score}', align="center", font=("ComicSans", 24))
            wn.update()

    time.sleep(delay)

turtle.done()
