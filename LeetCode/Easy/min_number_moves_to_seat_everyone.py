def minMovesToSeat(seats, students):
    """
    :type seats: List[int]
    :type students: List[int]
    :rtype: int
    """
    seats.sort()
    students.sort()
    dist = 0
    for i in range(len(seats)):
        dist += abs(seats[i] - students[i])
    return dist

'''
Input: seats = [3,1,5], students = [2,7,4]
Output: 4
'''
seats = [3,1,5]
students = [2,7,4]
print(minMovesToSeat(seats, students) == 4)