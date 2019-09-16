#draw a square
import turtle
amy = turtle.Turtle()
amy.color("yellow")
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)

#comments
# Import the turtle module.
import turtle

# Create a new turtle named amy.
amy = turtle.Turtle()

# Set amy's color.
amy.color("yellow")

# Have amy draw a square
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)

#using variables-part 1
import turtle
mary = turtle.Turtle()
lovely_color = "purple"
mary.color(lovely_color)
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)

#using variables-part 2
color = "purple"
sides = [1, 2, 3, 4, 5]
angle = 72
distance = 100
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)

#basic loops
import turtle
juno = turtle.Turtle()
juno.color("white")

for side in [1, 2, 3]:
    juno.forward(100)
    juno.left(120)

#assign list to variables
import turtle
amy = turtle.Turtle()
amy.color("cyan")

some_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for item in some_list:
    amy.forward(50)
    amy.right(30)

#list and loops
import turtle

lengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)

#loop within loops
import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(10)
        weaver.right(60)

    # Scoot over to the next link.
    weaver.penup()
    weaver.forward(20)
    weaver.pendown()

weaver.hideturtle()

#turtle methos
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw a red line
amy.color("red")
amy.forward(50)

# Move forward without drawing anything
amy.penup()
amy.forward(50)
amy.pendown()

# Draw an orange line
amy.color("orange")
amy.forward(50)

# Move forward without drawing anything
amy.penup()
amy.forward(50)
amy.pendown()

# Draw a yellow line
amy.color("yellow")
amy.forward(50)

#more loops -1
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between
for line in [1, 2, 3]:
    amy.color("red")
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()

#nested loops
import turtle

amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for side in [1, 2, 3, 4]:
        amy.forward(50)
        amy.right(90)
    amy.penup()
    amy.forward(100)
    amy.pendown()
 
#crunching_number 1

#defining functions
import turtle

def spiral():
    t = turtle.Turtle()
    t.color("cyan")
    for n in range(100):
        t.forward(n)
        t.right(20)

spiral()

#adding one parameters
import turtle
jack = turtle.Turtle()
jack.color("yellow")

def draw_square(length):
    for side in range(4):
        jack.forward(length)
        jack.right(90)

draw_square(100)
draw_square(50)
draw_square(25)

#adding multiple parameters
import turtle
jack = turtle.Turtle()
jack.color("yellow")

def draw_square(length, color):
    for side in range(4):
        jack.color(color)
        jack.forward(length)
        jack.right(90)

draw_square(100, "cyan")
draw_square(50, "magenta")
draw_square(25, "yellow")

#draw shape
import turtle
jack = turtle.Turtle()

def draw_shape(length, color, sides):
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)

draw_shape(100, "cyan", 5)

#make my own functions
import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def triangle_boogie(color, start):
  t = turtle.Turtle()
  t.color(color)
  t.speed(0)
  t.width(5)
  t.right(start)
  for shape in range(6):
    for side in range(3):
      t.forward(100)
      t.right(120)
    t.right(15)
  t.hideturtle()

# Call the function multiple times.
triangle_boogie("red", 0)
triangle_boogie("orange", 120)
triangle_boogie("blue", 240)

#indent with care
import turtle

# This code works!

def balloon(t, color):
    t.speed(0)
    t.color(color)

    # Draw balloon body.
    for side in range(30):
        t.forward(10)
        t.left(12)

    # Draw balloon knot.
    t.right(60)
    for side in range(3):
      t.forward(10)
      t.right(120)

    # Draw balloon string.
    t.color("gray")
    t.right(30)
    t.forward(100)


t = turtle.Turtle()

t.penup()
t.back(100)
t.pendown()
balloon(t, "red")

t.penup()
t.home()
t.pendown()
balloon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")

t.hideturtle()

#two turtle
import turtle
romeo = turtle.Turtle()
juliet = turtle.Turtle()

romeo.color("red")
romeo.width(5)

juliet.color("white")
juliet.width(5)

romeo.forward(150)
romeo.right(90)
romeo.forward(100)

juliet.forward(100)
juliet.right(90)
juliet.forward(100)

#more turtle
import turtle
romeo = turtle.Turtle()
montague = romeo

montague.color("red")
montague.width(5)

montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)
# romeo.color("white")
montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)

#square flower 1
import turtle

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)
for petal in range(6):
    draw_square(romeo)
    romeo.right(60)

#turtle 2
import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(8)

juliet = turtle.Turtle()
juliet.color("misty rose")
juliet.speed(8)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(romeo)
draw_flower(juliet)
