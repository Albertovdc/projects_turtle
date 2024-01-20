import turtle

user = turtle.Turtle()
screen = turtle.Screen()

def move():
  user.forward(20)

def around_right():
  for _ in range(1):
    user.right(10)
    user.forward(20)
def around_left():
  for _ in range(1):
    user.left(10)
    user.forward(20)

def back():
  user.backward(20)


screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="d", fun=around_right)
screen.onkey(key="a", fun=around_left)
screen.onkey(key="s", fun=back)
screen.onkey(key="c", fun=screen.resetscreen)

screen.exitonclick()
