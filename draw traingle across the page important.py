from turtle import*
#DRAW triangles ACROSS THE PAGE
number_of_shapes = 4
for shapes in range(1, number_of_shapes + 1):
    #draw triangle
    for sides in range(1, 4):
        forward(40)
        right(120)
    

    #move forward to start new postion of new triangle
    penup()
    forward(50)
    pendown()
