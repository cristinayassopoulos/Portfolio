import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
star = turtle.Turtle()
star.shape("turtle")
star.color("blue")
star.speed(3)

# Function to draw a five-point star
def draw_star(size):
    for i in range(5):
        star.forward(size)
        star.right(144)  # Angle to turn after each line

# Draw the star
draw_star(100)

# Hide the turtle
star.hideturtle()

# Keep the window open
turtle.done()
