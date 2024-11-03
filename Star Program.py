import turtle

def draw_triangle(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

def draw_star():
    turtle.speed(2)

    # Draw the bottom triangle
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.setheading(0)  # Face right
    turtle.pendown()
    draw_triangle("blue")

    # Draw the top left triangle
    turtle.penup()
    turtle.goto(52, -48)  # Move to the top point
    turtle.setheading(144)  # Rotate to the correct angle
    turtle.pendown()
    draw_triangle("blue")

   # Draw the top right triangle
    turtle.penup()
    turtle.goto(0, 10)  # Move back to the top point
    turtle.setheading(-120)  # Rotate to the correct angle
    turtle.pendown()
    draw_triangle("blue")

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
  #  turtle.setup(400, 400)
    draw_star()



