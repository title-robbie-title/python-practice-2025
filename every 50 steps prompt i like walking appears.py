from turtle import*
#walking 500 steps 'and enjoying it...
for steps in range(1,501):
    forward(1)#move 1 unit per loop
    if steps % 50 ==0: #this checks if the number divides even with 50
        print('this is fun')
