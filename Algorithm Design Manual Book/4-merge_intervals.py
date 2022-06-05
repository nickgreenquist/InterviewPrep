'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''
def mergeIntervals(intervals):
    n = len(intervals)
    intervals.sort()
    
    final = []
    i = 0
    while i < n:
        interval = intervals[i]
        start = interval[0]
        end = interval[1]
        
        # search for ones to merge into this one
        j = i + 1
        to_append = interval
        max_end = interval[1]
        while j < n:
            if intervals[j][0] <= to_append[1]:
                max_end = max(max_end, intervals[j][1])
                to_append = [interval[0], max_end]
                i += 1
                j = i + 1
            else:
                break 
        final.append(to_append)
        i += 1
        
    return final

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))