def move(n, a, b, c):
    if n == 1:
        print('move %s --> %s' % (a, c))
        return
    move(n-1, a, c, b) #move (n-1) plates from A to B tower
    print('move %s --> %s'% (a, c)) # move 1 plate from A to B tower
    move(n-1, b, a, c) # move the remaining (n-1) plates from B tower to C tower
print(move(5, 'A', 'B', 'C'))
