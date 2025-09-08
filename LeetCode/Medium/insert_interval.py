def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]: # insert into result
            res.append(newInterval)
            return res + intervals[i:] # early return with all other intervals
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else: # newInterval overlapping, need to update newInterval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])

    # if the first if statement above never runs, we need to add newInterval here
    res.append(newInterval)

    return res

'''
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))