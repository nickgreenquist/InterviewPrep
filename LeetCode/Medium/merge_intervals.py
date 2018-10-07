# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals = sorted(intervals, key=lambda interval: interval.start)
    deprecated = set()
    i = 0
    while i < len(intervals) - 1:
        if intervals[i].end >= intervals[i+1].start:
            new_interval = Interval(intervals[i].start, max(intervals[i+1].end, intervals[i].end))
            intervals[i+1] = new_interval
            deprecated.add(i)
        i += 1
    
    merged = []
    i = 0
    while i < len(intervals):
        if i not in deprecated:
            merged.append(intervals[i])
        i += 1
            
    return merged

'''
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''
intervals = []
for tup in [[1,3],[2,6],[8,10],[15,18]]:
    intervals.append(Interval(tup[0], tup[1]))
merged = merge(intervals)
print("Example 1:")
for i in merged:
    print("[{},{}]".format(i.start, i.end))
print()

'''
Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''
intervals = []
for tup in [[1,4],[4,5]]:
    intervals.append(Interval(tup[0], tup[1]))
merged = merge(intervals)
print("Example 2:")
for i in merged:
    print("[{},{}]".format(i.start, i.end))
print()