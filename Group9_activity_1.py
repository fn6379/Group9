'''Group 3 activity 1
members: 
Elsayed, Mahmoud, mee5011: hexagon and square
Mersha, Yeshiwas, yym2283: patttern and main
Nathershah, Faizahnadir, fn6379: circle and setPos
Our gitHub link: https://github.com/fn6379/Group9
'''

""""this function is used to draw the hexagon shape
while receiving colors from the user"""

def hexagon(turta,hexa_color, border_color):
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

""""this function is used to draw the square shape"""
def square(turta, square_color, border_color):
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
    turta.end_fill()
    
"""this function is used to draw the circle shape while receiving the colors 
   from the user"""
def circle(turta, circle_color, border_color):
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()

""""this function moves the turtle to the desired location without
drawing anything"""    
def setPos(turta, x, y):
    turta.penup()
    turta.setheading(0)
    turta.goto(x, y)
    turta.pendown()
""""the pattern function contains all the functions and it helps to create 
different shapes"""
def arrange(turta, distance):
    turta.penup()
    turta.setheading(0)
    turta.forward(distance)
    turta.down()
    
    
def pattern(turta,hexa_color, square_color,circle_color, border_color):
    
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
    sc.bgcolor("purple")
    
    setPos(turta, -200, 100)
    pattern(turta, hexa_color, square_color, circle_color, border_color)
    setPos(turta, -85, -30)
    pattern(turta, hexa_color, square_color, circle_color, border_color)
    setPos(turta, 30, -160)
    pattern(turta, hexa_color, square_color, circle_color, border_color)
    
    turta.hideturtle()
    sc.exitonclick()
main()



