n = input()

times = input()
times = times.split()
goals = input()
goals = goals.split()
a = int(goals[0])
b = int(goals[1])

t = 0
for i in range(a, b):
    t += int(times[i - 1])

print(str(t))



