from turtle import *

def freeze():
	screen.exitonclick()

screen = Screen()
#터틀 생성
turtle = Turtle()


turtle.hideturtle()
turtle.speed(0)
turtle.up()
#수성테두리 그리기
turtle.right(90)
turtle.forward(100)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("darkblue")
turtle.circle(100)
turtle.up()
turtle.home()

#금성테두리
turtle.right(90)
turtle.forward(130)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("gold")
turtle.circle(130)
turtle.up()
turtle.home()
#지구테두리 그리기
turtle.right(90)
turtle.forward(160)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("green")
turtle.circle(160)
turtle.up()
turtle.home()
#화성테두리 그리기
turtle.right(90)
turtle.forward(210)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("darkred")
turtle.circle(210)
turtle.up()
turtle.home()
#목성테두리 그리기
turtle.right(90)
turtle.forward(260)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("yellow")
turtle.circle(260)
turtle.up()
turtle.home()
#토성테두리 그리기
turtle.right(90)
turtle.forward(310)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("brown")
turtle.circle(310)
turtle.up()
turtle.home()
#천왕성테두리 그리기
turtle.right(90)
turtle.forward(360)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("skyblue")
turtle.circle(360)
turtle.up()
turtle.home()
#해왕성테두리 그리기
turtle.right(90)
turtle.forward(410)
turtle.right(270)
turtle.pensize(1)
turtle.down()
turtle.color("blue")
turtle.circle(410)
turtle.up()
turtle.home()

#태양그리기
turtle.up()
turtle.goto(0, 0)
turtle.right(90)
turtle.forward(50)
turtle.right(270)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(50)
turtle.end_fill()


turtle.speed(2)
#수성그리기
turtle.up()
turtle.home()
turtle.right(90)
turtle.forward(100)
turtle.right(270)
turtle.turtlesize(1)
turtle.showturtle()
turtle.color("darkblue")
turtle.shape("circle")
turtle.circle(100)

#금성그리기
turtle2 = Turtle()
turtle2.hideturtle()

turtle2.up()
turtle2.home()
turtle2.right(90)
turtle2.forward(130)
turtle2.right(270)
turtle2.turtlesize(1.5)
turtle2.showturtle()
turtle2.color("gold")
turtle2.shape("circle")
turtle2.circle(130)

#지구그리기
turtle3 = Turtle()
turtle3.hideturtle()

turtle3.up()
turtle3.home()
turtle3.right(90)
turtle3.forward(160)
turtle3.right(270)
turtle3.turtlesize(1.5)
turtle3.showturtle()
turtle3.color("green")
turtle3.shape("circle")
turtle3.circle(160)

#화성그리기
turtle4 = Turtle()
turtle4.hideturtle()

turtle4.up()
turtle4.home()
turtle4.right(90)
turtle4.forward(210)
turtle4.right(270)
turtle4.turtlesize(1.5)
turtle4.showturtle()
turtle4.color("darkred")
turtle4.shape("circle")
turtle4.circle(210)

#목성그리기
turtle5 = Turtle()
turtle5.hideturtle()

turtle5.up()
turtle5.home()
turtle5.right(90)
turtle5.forward(260)
turtle5.right(270)
turtle5.turtlesize(2.5)
turtle5.showturtle()
turtle5.color("yellow")
turtle5.shape("circle")
turtle5.circle(260)

#토성그리기
turtle6 = Turtle()
turtle6.hideturtle()

turtle6.up()
turtle6.home()
turtle6.right(90)
turtle6.forward(310)
turtle6.right(270)
turtle6.turtlesize(2.5)
turtle6.showturtle()
turtle6.color("brown")
turtle6.shape("circle")
turtle6.circle(310)

#천왕성그리기
turtle7 = Turtle()
turtle7.hideturtle()

turtle7.up()
turtle7.home()
turtle7.right(90)
turtle7.forward(360)
turtle7.right(270)
turtle7.turtlesize(1)
turtle7.showturtle()
turtle7.color("skyblue")
turtle7.shape("circle")
turtle7.circle(360)

#해왕성그리기
turtle8 = Turtle()
turtle8.hideturtle()

turtle8.up()
turtle8.home()
turtle8.right(90)
turtle8.forward(410)
turtle8.right(270)
turtle8.turtlesize(1)
turtle8.showturtle()
turtle8.color("blue")
turtle8.shape("circle")
turtle8.circle(410)

freeze()