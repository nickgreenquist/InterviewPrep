
def count_twos_at_digit(num, digit):
    powerOf10 = int(pow(10, digit))
    nextPowerOf10 = powerOf10 * 10
    right = int(num  % powerOf10)

    roundDown = num - num % nextPowerOf10
    roundUp = roundDown + nextPowerOf10

    digit = int((num / powerOf10) % 10)

    print(powerOf10)
    print(roundDown)
    print(roundUp)
    print(right)
    print()
    if digit == 2:
        return (roundDown / 10) + right + 1
    elif digit < 2:
        return roundDown / 10
    else:
        return roundUp / 10

def count_twos_in_range(num):
    count  = 0
    for i in range(len(str(num))):
        count += count_twos_at_digit(num, i)
        print("count: {}".format(count))
    return count

print(count_twos_in_range(29))