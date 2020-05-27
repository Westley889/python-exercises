import turtle
import time
import random
from test import myround

delay = 0.075

# Score
score = 0
high_score = 0

#Screen setup
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=620, height=620)
wn.tracer(0)

#Snake head setup
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#food setup
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(myround(random.randint(-280, 280)), myround(random.randint(-280, 280)))

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 275)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 18, "normal"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for head collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 250 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0) 
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear the list
        segments.clear()

        # Reset Score
        score = 0

        # Reset score
        delay = 0.1

        # Update the score display
        pen.clear()
        pen.write("Score: %d  High Score: %d" % (score, high_score), align = "center", font = ("Courier", 18, "normal"))

    #Check for food collision
    if head.distance(food) < 20:
        # Move food to a random location
        food.goto(myround(random.randint(-280, 280)), myround(random.randint(-280, 280)))

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay time
        delay -= 0.005
        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: %d  High Score: %d" % (score, high_score), align = "center", font = ("Courier", 18, "normal"))

    # Move the end segments first
    for index in range(len(segments)-1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())

    # Move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the list
            segments.clear()
                    # Reset Score
            score = 0

            # reset the delay
            delay = 0.1
            # Update the score display
            pen.clear()
            pen.write("Score: %d  High Score: %d" % (score, high_score), align = "center", font = ("Courier", 18, "normal"))

    time.sleep(delay)

wn.mainloop()