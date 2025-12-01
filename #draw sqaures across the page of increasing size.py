from turtle import*
#draw sqaures across the page of increasing size
#draw sqaure
number_of_shapes = 6
for shape in range (1, number_of_shapes +1):
    for sides in range(1,5):
        forward(30 + shape * 10)
        right(90)
    
penup()
forward(40 + shape * 10)
pendown()
