import math

while True:
    n = int(input())
    if n == 0:
        break

    x_sum = 0
    y_sum = 0
    for i in range(n):
        inp = input().split()
        x = int(inp[0])
        y = int(inp[1])

        x_sum += x
        y_sum += y
    x_sum = round(x_sum / n)
    y_sum = round(y_sum / n)

    print("%s %s" % (x_sum, y_sum))





