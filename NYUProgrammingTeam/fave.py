n = int(input())
ords = input()
ords = ords.split()
faves = input()
faves = faves.split()

for i in range(n):
    ords[i] = int(ords[i])
    faves[i] = int(faves[i])

for k in range(n):
    for i in range(n):
        for j in range(i + 1, n):
            f = abs( i - j )
            if f == faves[i]:
                if ords[j] < ords[i]:
                    #swap
                    tempOrd = ords[i]
                    tempFave = faves[i]
                    ords[i] = ords[j]
                    faves[i] = faves[j]
                    ords[j] = tempOrd
                    faves[j] = tempFave
            if f == faves[j]:
                if ords[j] < ords[i]:
                    #swap
                    tempOrd = ords[i]
                    tempFave = faves[i]
                    ords[i] = ords[j]
                    faves[i] = faves[j]
                    ords[j] = tempOrd
                    faves[j] = tempFave
print(ords)
sorted = True
for i in range(1, n - 1):
    if ords[i] < ords[i - 1]:
        sorted = False
if sorted:
    print('YES')
else:
    print('NO')
