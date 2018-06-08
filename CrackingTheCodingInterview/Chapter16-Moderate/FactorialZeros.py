def factors_of_5(n):
    count = 0
    while n % 5 == 0 and n != 0:
        count += 1
        n //= 5
    return count

def count_zeros_in_factorial(n):
    count = 0
    for i in range(n + 1):
        count += factors_of_5(i)
    return count

print(count_zeros_in_factorial(25))