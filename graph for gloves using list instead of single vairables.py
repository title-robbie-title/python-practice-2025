#produce graph for gloves sales
from turtle import*

#set up the gloves variable(list form)
gloves = (10,8,3,5)

#produce x axis
penup()
goto(0,0)
pendown()
goto(80,0)

#produce y axis
penup()
goto(0,0)
pendown()
goto(0,100)

#plot data
penup()
goto(0,0)
pendown()
goto(20, gloves[0] * 10)
goto(40, gloves[1] * 10)
goto(60, gloves[2] * 10)
goto(80, gloves[3] * 10)

#sets the variable "total" to all gloves in list added together
total = gloves[0]+ gloves[1]+ gloves[2] + gloves[3]
print (total)
