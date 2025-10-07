"""
Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
determine if a person could add all meetings to their schedule without any conflicts.
"""

def canAttendMeetings(intervals) -> bool:
    intervals = sorted(intervals)
    for i in range(len(intervals) - 1):
        cur = intervals[i]
        next = intervals[i + 1]
        if cur[1] > next[0]:
            return False
    return True

'''
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false

Input: intervals = [(5,8),(9,15)]
Output: true
'''

print(canAttendMeetings([(0,30),(5,10),(15,20)]))
print(canAttendMeetings([(5,8),(9,15)]))