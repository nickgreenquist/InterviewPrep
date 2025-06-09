def groupThePeople(groupSizes):
    """
    :type groupSizes: List[int]
    :rtype: List[List[int]]
    """
    group_size_to_members = {}
    for i in range(len(groupSizes)):
        group_size = groupSizes[i]
        if group_size not in group_size_to_members:
            group_size_to_members[group_size] = []
        group_size_to_members[group_size].append(i)
    
    out = []
    for group_size,members in group_size_to_members.items():
        groups = []
        for i in range(0, len(members), group_size):
            groups.append(members[i:i + group_size])
        for group in groups:
            out.append(group)
    return out

'''
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
'''
groupSizes = [2,1,3,3,3,2]
print(groupThePeople(groupSizes))