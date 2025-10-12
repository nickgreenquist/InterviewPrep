'''
Given an array of meeting time interval objects consisting of start and end times:
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),

find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.
'''

'''
GOAL: max number of overlapping intervals at any given time
'''

def minMeetingRooms(intervals) -> int:
    num_meetings_ongoing_at_i = {}

    for interval in intervals:
        start = interval[0]
        end = interval[1]
        if start not in num_meetings_ongoing_at_i:
            num_meetings_ongoing_at_i[start] = 0
        if end not in num_meetings_ongoing_at_i:
            num_meetings_ongoing_at_i[end] = 0

        # if meeting ends at this time, decrement num ongoing meetings
        num_meetings_ongoing_at_i[start] += 1
        num_meetings_ongoing_at_i[end] -= 1

    # go over all times a meeting started/stopped   
    sorted_keys = sorted(num_meetings_ongoing_at_i.keys())

    prev_ongoing_meetings = 0
    max_ongoing_meetings = 0
    for time in sorted_keys:
        prev_ongoing_meetings += num_meetings_ongoing_at_i[time]
        max_ongoing_meetings = max(max_ongoing_meetings, prev_ongoing_meetings)
    return max_ongoing_meetings

def minMeetingRooms2(intervals) -> int:
    starts = []
    ends = []

    for interval in intervals:
        starts.append(interval[0])
        ends.append(interval[1])

    starts = sorted(starts)
    ends = sorted(ends)

    current = 0
    most = 0
    i, j = 0, 0
    while i < len(starts): # only need to find all starts
        start = starts[i]
        end = ends[j]
        if end <= start:
            current -= 1
            j += 1
        else:
            current += 1
            i += 1
        most = max(most, current)
    return most
        


'''
Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)
'''
print(minMeetingRooms(intervals = [(0,40),(5,10),(15,20)]))
print(minMeetingRooms2(intervals = [(0,40),(5,10),(15,20)]))

