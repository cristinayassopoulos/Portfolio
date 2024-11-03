# Binary tree project I did awhile ago. 
num_triangles_to_draw = 5

for _ in range(num_triangles_to_draw):
    checkTriangle()

import random
import math
import turtle

window = turtle.Screen()
writer = turtle.Turtle()
writer.pensize(3)
writer.pencolor("pink")

def generateRandomSideLength(min_value, max_value):
    return random.randint(min_value, max_value)

def angle(side1, side2, side3):
    return math.degrees(math.acos((side3**2 - side2**2 - side1**2) / (-2.0 * side1 * side2))

def drawTriangle(side1, side2, side3, angle1, angle2, angle3):
    writer.penup()
    writer.forward(side1)
    writer.left(angle3)
    writer.pendown()
    writer.forward(side2)
    writer.left(angle1)
    writer.forward(side3)
    writer.left(angle2)

def checkTriangle():
    side1 = generateRandomSideLength(5, 100)
    side2 = generateRandomSideLength(5, side1)  # Generate side2 <= side1
    side3 = generateRandomSideLength(5, side2)  # Generate side3 <= side2

    if side1 > 0 and side2 > 0 and side3 > 0:
        sum1and2 = side1 + side2
        sum1and3 = side1 + side3
        sum2and3 = side2 + side3

        angle1 = angle(side1, side2, side3)
        angle2 = angle(side2, side3, side1)
        angle3 = angle(side3, side1, side2)

        if side3 <= sum1and2 and side2 <= sum1and3 and side1 <= sum2and3:
            print("true")
            print(side1, side2, side3)
            print(angle1, angle2, angle3)
            drawTriangle(side1, side2, side3, angle1, angle2, angle3)
        else:
            print("false")
    else:
        print("Invalid side lengths - cannot form a triangle")

num_triangles_to_draw = 5

for _ in range(num_triangles_to_draw):
    checkTriangle()

turtle.done()
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()
    
if __name__ == '__main__':
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
