n = int(input())

cities = input()
cities = cities.upper()

s_to_f = 0
f_to_s = 0
last = cities[0]
for i in range(1, len(cities)):
    if last == 'F' and cities[i] == 'S':
        f_to_s += 1
    if last == 'S' and cities[i] == 'F':
        s_to_f += 1
    last = cities[i]

if s_to_f > f_to_s:
    print("YES")
else:
    print("NO")