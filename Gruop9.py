from turtle import Turtle, Screen
"""
Group 9
Group members: Mahmoud, Faizah, Yeshiwas

Faizah: Hexagon and Square
Mahmoud: Circle and SetPos
Yeshiwas: Pattern and Main"""

def hexagon(turta, hexa_color, border_color):
    """def hexagon: applies commands to draw and color the hexagon."""
    turta.pencolor(border_color)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.end_fill()

def square(turta, square_color, border_color):
    """def square: applies commands to draw and color the square."""
    turta.pencolor(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.end_fill()
    
def circle(turta, circle_color, border_color):
    """def circle: applies commands to draw and color the circle."""

    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()

def setPos(turta, x, y):
    """def SetPos:sets turtle to default position and then allows to go to any specific coordination by typing in coordinates"""
    turta.penup()
    turta.setheading(0)
    turta.goto(x, y)
    turta.pendown()

def arrange(turta, distance):

    """the pattern function contains all the functions and it helps to create 
    different shapes"""
    turta.penup()
    turta.setheading(0)
    turta.forward(distance)
    turta.down()

    
def pattern(turta, hexa_color, square_color, circle_color, border_color):
    """def pattern: starts applying all previous functions all at once and draws the wanted pattern."""

     # setPos(turta, -200, 100)
    hexagon(turta,  hexa_color, border_color)
    arrange(turta, 150 )
    circle(turta, circle_color, border_color)
    arrange(turta, 75)
    square( turta,square_color, border_color)

def main(): 
    from turtle import Screen,Turtle
    hexa_color = input("Enter the color of hexagon:hexa_color=") # asks the user to give the color of hexagon
    circle_color = input("Enter the color of circle:cir_color=") # asks the user to give the color of circle
    square_color = input("Enter the color of square:square_color=") # asks the user to give the color of square
    border_color = input("Enter the color of border:border_color=") # asks the user to give the color of the border
    sc= Screen()
    turta= Turtle()
    turta.speed(10)
    sc.title("Group 9: Acitivity 1") # changes the title of the screen
    sc.bgcolor("black")
    
    setPos(turta, -200, 100)
    pattern(turta, hexa_color, square_color, circle_color, border_color)
    setPos(turta, -85, -30)
    pattern(turta, hexa_color, square_color, circle_color, border_color)
    setPos(turta, 30, -160)
    pattern(turta, hexa_color, square_color, circle_color, border_color)

    turta.hideturtle()
    sc.exitonclick()

main()