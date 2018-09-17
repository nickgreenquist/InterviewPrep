import random

def shuffle(arr):
    shuffled = arr[:]      

    # move from the back to the front, swapping a random integer
    # from the first section with the current index you are at              
    for i in range(len(shuffled)-1, 0, -1):     
        random_index = random.randrange(0, i+1)
        shuffled[i], shuffled[random_index] = shuffled[random_index], shuffled[i]
    return shuffled

arr = [1,2,3,4,5,6,7,8,9]
print(shuffle(arr))