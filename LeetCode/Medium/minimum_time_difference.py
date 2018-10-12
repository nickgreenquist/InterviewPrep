'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
'''

def toMinutes(time):
    time = time.split(":")
    return int(time[0])*60 + int(time[1])

def findMinDifference(timePoints):
    minutes = []
    for time in timePoints:
        minutes.append(toMinutes(time))
    
    minutes = sorted(minutes)
    
    min_time = float('inf')
    midnight = 24*60
    for i in range(len(minutes) - 1):
        d = minutes[i] - minutes[i+1]
        min_m = min(minutes[i], minutes[i+1])
        max_m = max(minutes[i], minutes[i+1])
        min_time = min(min_time, midnight-max_m + min_m, abs(d))
        
    # handle the min and max times - might be close to each other
    d = minutes[0] - minutes[-1]
    min_m = min(minutes[0], minutes[-1])
    max_m = max(minutes[0], minutes[-1])
    min_time = min(min_time, midnight-max_m + min_m, abs(d))
    return min_time

'''
Example 1:
Input: ["23:59","00:00"]
Output: 1
'''
print(findMinDifference(["23:59","00:00"]))