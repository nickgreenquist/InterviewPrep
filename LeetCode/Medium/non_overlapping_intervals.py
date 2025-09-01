
def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    
    current = intervals[0][1]
    skip = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < current:
            skip += 1
        else: # keep
            current = intervals[i][1]
    return skip


'''
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
'''
intervals = [[1,2],[2,3],[3,4],[1,3]]

print(eraseOverlapIntervals(intervals))