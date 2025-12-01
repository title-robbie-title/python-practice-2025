from turtle import*
#draw first triangle
for sides in range (1,4):
    forward(100)
    left(120)
#now move the pen to the next place
penup()
right(120)
forward(200)
left(120)
pendown()
#draw second triangle
for sides in range(1,4):
    forward(100)
    left(120)
#now move the pen to the next place
penup()
forward(300)
right(120)
right(120)
pendown()
#draw second triangle
for sides in range(1,4):
    forward(100)
    left(120)
#giant triangle of triangles
penup()
forward(100)
pendown()
forward(200)
left(120)
forward(300)
left(120)
forward(300)

    
