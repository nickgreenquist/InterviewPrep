from random import randint
def rand5():
    return randint(0,5)

def rand7():
    val = 5 * rand5() + rand5()
    if val < 21:
        return val % 7
    else:
        return rand7()

vals = [0,0,0,0,0,0,0]
for i in range(1000000):
    val = rand7()
    vals[val] += 1
print(vals)