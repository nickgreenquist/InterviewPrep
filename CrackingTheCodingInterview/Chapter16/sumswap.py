def sumswap(list1, list2):
    sum1 = 0
    for a in list1:
        sum1 += a
    sum2 = 0
    for b in list2:
        sum2 += b

    for a in list1:
        for b in list2:
            temp_sum1 = sum1
            temp_sum2 = sum2

            sum1 -= a
            sum1 += b

            sum2 -= b
            sum2 += a

            if sum1 == sum2:
                return (a, b)
            
            sum1 = temp_sum1
            sum2 = temp_sum2

    return None

def sumswap_optimal(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)

    if (sum1 - sum2) % 2 != 0:
        return None
    target = (sum1 - sum2) // 2

    contents_list2 = set()
    for b in list2:
        contents_list2.add(b)

    for a in list1:
        b = a - target
        if b in contents_list2:
            return (a, b)
    return None

list1 = [4,1,2,1,1,2]
list2 = [3,6,3,3]
print( sumswap_optimal(list1, list2))
