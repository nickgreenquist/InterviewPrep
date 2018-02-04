inp = input()
inp = inp.split(' ')
a = int(inp[0])
b = int(inp[1])

c = a * b
if c % 2 == 0:
    print("Even")
else:
    print("Odd")