#lower right-angled triangle
size = 4
for i in range(1, size + 1):
    print(' ' * (size - i) + '*' * i)

#upper right-angled triangle
size = 4
for i in range(1, size + 1):
    print('*' * (size - i) )

#upper right right-angle triangle
size = 5
for i in range(1, size + 1):
    print(' ' * i + '*' * (size - i))

#normal
size = 4
for i in range(1, size + 1):
    print('*' * i )
    
