def volume(lake):
    i = 1
    total_water = 0

    # find the start barrier
    while i < len(lake) and lake[i] > lake[i-1]:
        i += 1
    i -= 1

    while i < len(lake):
        left = i
        height = lake[i]
        max_i = i
        max_height = 0

        i += 1
        while i < len(lake) and lake[i] < lake[left]:
            if lake[i] >= max_height:
                max_height = lake[i]
                max_i = i
            i += 1
        if i < len(lake): # if we didn't run out of lake, height is height of left
            max_i = i
            max_height = height

        dirt = 0
        for j in range(left + 1, max_i):
            dirt += lake[j]

        water = ((max_i - left - 1) * max_height) - dirt
        # print("left:%s, right:%s, height:%s, water:%s" % (left, max_i, height, water))

        total_water += water
        
    return total_water

lake = [1,3,2,4,1,3,1,4,5,2,2 ,1 ,4 ,2 ,2 ]
print(volume(lake)) # 15

lake = [2, 0, 2]
print(volume(lake)) # 2

lake = [3, 0, 0, 2, 0, 4]
print(volume(lake)) # 10

lake = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11] 
print(volume(lake)) # 6