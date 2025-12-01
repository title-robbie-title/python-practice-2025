#produce graph fro gloves sales
from turtle import*

#set up the gloves variable
gloves1= 10
gloves2= 8
gloves3= 3
gloves4= 5
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
goto(20, gloves1 * 10)
goto(40, gloves2 * 10)
goto(60, gloves3 * 10)
goto(80, gloves4 * 10)
