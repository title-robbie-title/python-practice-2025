from turtle import*
#produce times table
size = 12
for row in range(1, size + 1):
    for column in range(1, size + 1):
        print (row * column, end = ' ')
    #move to new line
    print ()
