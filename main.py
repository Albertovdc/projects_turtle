import random
import turtle

colors = ['red', 'blue', 'yellow', 'purple', 'green', 'orange']
all_turtles = []
race_is_on = False


screen = turtle.Screen()
screen.setup(500, 400)

user_belt = screen.textinput("Turtle race", "Make you bet, which color will win?")
x_coord = -230
y_coord = -100
for color in colors:
  new_user = turtle.Turtle(shape="turtle")
  new_user.penup()
  new_user.color(color)
  new_user.goto(x_coord, y_coord)
  y_coord += 40
  all_turtles.append(new_user)

if user_belt in colors:
  race_is_on = True

while race_is_on:
  for turtle in all_turtles:
    if turtle.xcor() == 230:
      race_is_on = False
      if user_belt == turtle.pencolor():
        print(f"You've win. The {turtle.pencolor()} turtle is the winner.")
      else:
        print(f"You've lost. The {turtle.pencolor()} turtle is the winner.")

    turtle.forward(random.randint(0,10))


screen.exitonclick()
