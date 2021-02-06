# Simple Snake Game in Python 3 
# By Chimbook 
# Part:1 Getting started 

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

#Set up the screen
wn = turtle.Screen()
wn.turtle("Snake Game by @Chimbook")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segements = []

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score", align="center", font=("Courier", 24, "normal"))

# Function
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
       y = head.ycor()
       head.sety(y + 20)

    if head.direction == "down":
       y = head.ycor()
       head.sety(y - 20)

    if head.direction == "left":
       x = head.xcor()
       head.setx(x - 20)

    if head.direction == "right":
       x = head.xcor()
       head.setx(x + 20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
# Main gmae loop
while True:
    wn.update() 


    # Check for a collision with the border 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # Hide the segments
        for segment in segements:
            segements.goto(1000, 1000)

        # Clear the segments list
        segements.clear()

        # Reset the score 
        score = 0

        # Reset the score 
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

        # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a ramdom spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment  = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segements.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))



    # Move the end segments first in reverse order
    for index in range(len(segements)-1, 0, -1):
        x = segements[index-1].xcor()
        y = segements[index-1].ycor()
        segements[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segements) > 0:
        x = head.xcor()
        y = head.ycor()
        segements[0].goto(x.y) 
         
    move()


    
    # Check for head collision with the body segments
    for segment in segements:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
         
            #Hide the segments
            for segment in segements:
                segment.goto(1000, 1000)

            # Clear the segments 
            segment.clear()
         
         # Reset the score 
        score = 0

        # Reset the delay
        delay = 0.1

        # Update the score display   
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

         


    time.sleep(delay)

wn.mainloop()

