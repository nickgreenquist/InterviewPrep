def PairsWithSum(array, sum):
    counts = {}
    for a in array:
        if a in counts:
            counts[a] += 1
        else:
            counts[a] = 1
    
    pairs = 0
    for a in array:
        target = sum - a
        if target in counts:
            pairs += counts[target]

            # can't add number with itself
            if a == target:
                pairs -= 1
    return pairs

array = [1,2,3,4,5]
sum = 3
print( PairsWithSum(array, sum))