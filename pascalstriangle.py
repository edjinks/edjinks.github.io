import math

def nCr(n,r):
    NchooseR = (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
    return NchooseR

rows = 10
x = 0
z = 0
line = []

for x in range(rows):
    for z in range(x+1):
        line.append(nCr(x, z))
        z += 1
    stars = rows - x
    s = []
    for x in range(stars):
        s.append(" ")
    s.append(line)
    print(s)
    line = []
    x += 1
