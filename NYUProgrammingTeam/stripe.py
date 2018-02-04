n = int(input())
inp = input().split()

nums = []
for ip in inp:
    nums.append(int(ip))

total = 0
sum1 = 0
sum2 = 0
for i in range(0, len(nums)):
    sum2 += nums[i]

for i in range(0, len(nums) - 1):
    sum1 += nums[i]
    sum2 -= nums[i]
    if sum1 == sum2:
        total += 1
print(total)