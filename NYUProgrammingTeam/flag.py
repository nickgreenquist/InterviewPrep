import math

inp = input()
inp = inp.split(' ')
n = int(inp[0])
m = int(inp[1])
a = int(inp[2])

num = math.ceil(float(n)/float(a))
num += math.ceil(float(m)/float(a))

print(num)