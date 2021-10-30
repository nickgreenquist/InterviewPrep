import random

def selectKItems(stream, n, k):
    
    # make sample first k elements of stream
    sample = [0] * k
    for i in range(k):
        sample[i] = stream[i]

    # now that we have the first k elements from the 'stream',
    # we simulate getting one new item from the stream.
    # We give each new item a k/n chance of being part of the sample.
    i = k + 1
    while i < n:
        j = random.randint(0, i)

        if j < k:
            sample[j] = stream[i]   

        i += 1
    
    return sample

if __name__ == "__main__":
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(stream)
    k = 5
    sample = selectKItems(stream, n, k)
    print(sample)