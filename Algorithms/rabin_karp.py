d = 256 # number of chars in input alphabet

def search(pattern, text, prime):
    global d
    M = len(pattern)
    N = len(text)

    if M > N:
        return None

    hits = []

    hash_p = 0
    hash_t = 0
    h = 1 # the current hash value

    for i in range(M-1):
        h = (h*d)%prime

    # initial hash values for pattern and text[:M]
    for i in range(M):
        hash_p = (d*hash_p + ord(pattern[i]))%prime
        hash_t = (d*hash_t + ord(text[i]))%prime

    for i in range(N-M+1):
        if hash_p == hash_t:
            # potential match, check chars one by one
            for j in range(M):
                if pattern[j] != text[i+j]:
                    break

            if j == M-1:
                hits.append(i)
        
        # update the rolling hash value
        if i < N-M:
            hash_t = (d*(hash_t - ord(text[i]) * h) + ord(text[i+M]))%prime

            # edge case for negative hash_t
            if hash_t < 0:
                hash_t += prime
    
    return hits

text = "BANANAS ARE BONANZA"
pattern = "AN"
prime = 101
hits = search(pattern, text, prime)

# display the hits
matches = ['-']*len(text)
for hit in hits:
    matches[hit] = '*'

print("Hits for pattern {} in text:\n".format(pattern))
print(text)
print("".join(matches))

