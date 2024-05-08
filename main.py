from turtle import Screen, Turtle, clearscreen

tim = Turtle()
screen = Screen()

def move_back():
  tim.backward(20)

def move_forward():
  tim.forward(20)

def move_left():
  tim.left(10)

def move_right():
  tim.right(10)

def clear():
  tim.clear()
  tim.up()
  tim.home()
  tim.down()

screen.listen()
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
