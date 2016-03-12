import math
k = 0
m = 0
q = 0
k = input()
m = input()
for i in range(k,m):
    if int(math.sqrt(i))**2==i:
        q+=1
print (q)
