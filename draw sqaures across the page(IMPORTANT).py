from turtle import*
#DRAW SQAURES ACROSS THE PAGE
number_of_shapes = 4
for shapes in range(1, number_of_shapes + 1):
    #draw sqaure
    for sides in range(1, 5):
        forward(40)
        right(90)
    

    #move forward to start new postion of new sqaure
    penup()
    forward(50)
    pendown()
