from turtle import*
#draw triangles across the page of increasing size
#draw triangle
number_of_shapes = 6
for shape in range (1, number_of_shapes +1):
    for sides in range(1,4):
        forward(30 + shape * 10)
        right(120)
    
penup()
forward(40 + shape * 10)
pendown()
