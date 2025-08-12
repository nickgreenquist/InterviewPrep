def convert(length, rotation_offest, idx):
    new_idx = idx + rotation_offest
    if new_idx >= length:
        new_idx -= length
    return new_idx

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    # first - find rotation point
    left = 0
    right = len(nums) - 1

    iteration = 0
    rotation_offest = 0
    while left < right:
        mid = (left + right) // 2

        print(iteration, "mid: ", mid)

        if nums[mid] > nums[mid + 1]:
            print("found rotation")
            rotation_offest = mid + 1
            break
        elif nums[mid] < nums[mid - 1]:
            print("found rotation")
            rotation_offest = mid
            break

        if nums[left] < nums[mid] and nums[mid] < nums[right]:
            rotation_offest = left # TODO
            break
        
        if nums[left] > nums[mid]: # rotation to left
            right = mid
            rotation_offest = mid
        elif nums[right] < nums[mid]: # rotation to right
            left = mid
            rotation_offest = left

        iteration += 1

    print(rotation_offest)

    # binary search
    length = len(nums)
    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)

        converted_mid = convert(length, rotation_offest, mid)

        print("mid: ", mid)
        print("converted_mid: ", converted_mid)
        print("num at converted mid: ", nums[converted_mid])

        if nums[converted_mid] == target:
            print("found mid: ", converted_mid)
            return converted_mid

        elif nums[converted_mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


nums = [4,5,6,7,0,1,2]
target = 0

found = search(nums, target)
print(found)