from turtle import*
#draws first sqaure
for sides in range(1,5):
    forward(100)
    left(90)
#moves to the start of the next sqaure
penup()
right(90)
forward(50)
left(90)
pendown()
#draw second square
for sides in range(1,5):
    forward(100)
    right(90)
    
    
