def intersect(nums1, nums2):
    set1 = {}
    for n in nums1:
        if n in set1:
            set1[n] += 1
        else:
            set1[n] = 1
    set2 = {}
    for n in nums2:
        if n in set2:
            set2[n] += 1
        else:
            set2[n] = 1
    
    inter_list = []
    for n in nums2:
        if n in set1:
            if set1[n] > 0:
                inter_list.append(n)
                set1[n] -= 1
    return inter_list

'''
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''
print(intersect([4,9,5], [9,4,9,8,4]))