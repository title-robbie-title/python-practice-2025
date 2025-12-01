#produce graph fro gloves sales
from turtle import*

# set up the gloves variable in a list
gloves = [10, 8, 3, 5]

# reverse the list using temp
# len(gloves) == 4
# // 2 -> integer division, gives 2 (range needs an int, not 2.0)
for i in range(len(gloves) // 2):
    # i value goes up auto each loop so goes 0, 1 (two passes)so first pass its value is 10 second pass value is 8
    temp = gloves[i]  # save the left item (first pass: temp = 10)

    # copy the right item into the left slot
    # first pass: gloves[0] = gloves[3]so it sees whats in postion 3 and puts item at index 0
    #second pass: gloves[1] = gloves[2]so it sees whats in postion 2 and puts item at index 1
    gloves[i] = gloves[len(gloves) - 1 - i]

    # put the saved left item into the right slot
    # first pass: gloves[3] = 10
    # second pass: gloves[2] = 8
    gloves[len(gloves) - 1 - i] = temp

print(gloves)  # [5, 3, 8, 10]

#so [i] doesnt really look at the number just postion in list unless we put the value of i in a sum
