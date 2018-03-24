n = int(input())

first = []
min_first_end = float('Inf')
max_first_start = float('-inf')
for i in range(n):
    s = input().split()
    start = int(s[0])
    end = int(s[1])

    first.append((start, end))

    min_first_end = min(min_first_end, end)
    max_first_start = max(max_first_start, start)

m = int(input())

second = []
min_second_end = float('Inf')
max_second_start = float('-inf')
for i in range(m):
    s = input().split()
    start = int(s[0])
    end = int(s[1])

    second.append((start, end))

    min_second_end = min(min_first_end, end)
    max_second_start = max(max_first_start, start)

dist = max_second_start - min_first_end
dist1 = max_first_start - min_second_end

ans = max(dist, dist1)
if ans <= 0:
    ans = 0

print(ans)