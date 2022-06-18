import random

# range: [1,7] inclusive
def rand7():
    return random.randint(0, 7) + 1

# range [0-48] inclusive 
def rand49():
    return (rand7() - 1) * 7 + (rand7() - 1)

def rand10():
    r = 40
    while r >= 40:
        r = rand49()
    return r % 10 + 1

results = {}
for i in range(1, 10 + 1):
    results[i] = 0

for i in range(100000):
    r = rand10()
    results[r] += 1

print(results)