
def find_longest_subarray_with_equal_letters_and_numbers(lis):
    n = len(lis)
    num_letters = [0]*n
    num_numbers = [0]*n

    diff = [0]*n

    if lis[0] == 'a':
        num_letters[0] = 1
        num_numbers[0] = 0
    else:
        num_letters[0] = 0
        num_numbers[0] = 1
    for i in range(1, n):
        if lis[i] == 'a':
            num_letters[i] = num_letters[i-1] + 1
            num_numbers[i] = num_numbers[i-1]
        else:
            num_letters[i] = num_letters[i-1]
            num_numbers[i] = num_numbers[i-1] + 1
    
    for i in range(n):
        diff[i] = num_letters[i] - num_numbers[i]
    
    seen = {}
    max_dis = -1
    for i in range(n):
        num = diff[i]
        if num in seen:
            max_dis = max(max_dis, i - seen[num])
        else:
            seen[num] = i
    return max_dis


lis = ['a','a','a','a',1,1,'a',1,1,'a','a',1,'a','a',1,'a','a','a','a']
max_dis = find_longest_subarray_with_equal_letters_and_numbers(lis)
print(max_dis)
