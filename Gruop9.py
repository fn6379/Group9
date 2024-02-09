from turtle import Turtle, Screen
"""
Group 9
Group members: Mahmoud, Faizah, Yeshiwas

Faizah: Hexagon and Square
Mahmoud: Circle and SetPos
Yeshiwas: Pattern and Main"""


def setPos(turta, x, y):
    """def SetPos:sets turtle to default position and then allows to go to any specific coordination by typing in coordinates"""
    turta.penup()
    turta.setheading(0)
    turta.goto(x, y)
    turta.pendown()

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

    
def pattern(turta, hexa_color, square_color, circle_color, border_color):
    """def pattern: starts applying all previous functions all at once and draws the wanted pattern."""

    setPos(turta, x= -200, y = 100)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, x= -50, y = 100)
    circle(turta, circle_color, border_color)
    setPos(turta, x=25 , y = 100)
    square(turta, square_color, border_color)
    
    setPos(turta, x= -85, y = -30)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, x= 65, y = -30)
    circle(turta, circle_color, border_color)
    setPos(turta, x= 140, y = -30)
    square(turta,square_color, border_color)
   
    setPos(turta, x= 15, y = -160)
    hexagon(turta,hexa_color, border_color)
    setPos(turta, x= 165, y = -160)
    circle(turta,circle_color, border_color)
    setPos(turta, x= 240, y = -160)
    square(turta, square_color, border_color)


def main(): 
    """ def main: calls all functions"""
    hexa_color = input("Enter the color of hexagon: ")
    circle_color = input("Enter the color of circle: ")
    square_color = input("Enter the color of square: ")
    border_color = input("Enter the color of border: ")


    """Intializing screen and turtle"""
    sc = Screen()
    turta = Turtle()

    sc.title("Group 9: Activity 1")
    sc.bgcolor("black")
    turta.speed(10)

    pattern(turta, hexa_color, square_color, circle_color, border_color)

    turta.hideturtle()
    sc.exitonclick()

main()