
def _power_set(power, arr, path):
    power.append(path)
    for i in range(len(arr)):
        _power_set(power, arr[i + 1:], path + [arr[i]])
    
def power_set(nums):
    power = []
    nums.sort()
    _power_set(power, nums, [])
    return power

'''
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
print(power_set([1,2,3]))