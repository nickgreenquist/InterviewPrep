def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

while True:
    x = int(input())
    if x == 0:
        break
    
    s = sum_digits(x)
    for i in range(11, 10000):
        if sum_digits(x * i) == s:
            print(i)
            break