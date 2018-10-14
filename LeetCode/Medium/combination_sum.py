'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times
'''

def implicitSearch(candidates, target, out, current_index, current_path):
    if target < 0:
        return
    if target == 0:
        out.append(current_path)
        return
    for i in range(current_index, len(candidates)):
        c = candidates[i]
        implicitSearch(candidates, target - c, out, i, current_path + [c])
    
def combinationSum(candidates, target):
    out = []
    candidates.sort()
    implicitSearch(candidates, target, out, 0, [])
    return out

'''
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
'''
print(combinationSum(candidates = [2,3,6,7], target = 7))


'''
Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
print(combinationSum(candidates = [2,3,5], target = 8))