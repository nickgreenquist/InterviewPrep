'''
The computer has four slots, and each slot will contain a ball that is red (R), yellow (Y), green (G) or blue (B). 
For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a "hit:' 
If you guess a color that exists but is in the wrong slot, you get a "pseudo-hit:' 
Note that a slot that is a hit can never count as a pseudo-hit. 
For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudo­ hit
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits
'''

def master_mind(guess, actual):
    hits = 0
    p_hits = 0
    counts = {}

    # 1. Calculate hits and reduce counts for hit slots
    for i in range(len(actual)):
        if guess[i] == actual[i]:
            hits += 1
        else:
            if actual[i] in counts:
                counts[actual[i]] += 1
            else:
                counts[actual[i]] = 1
    
    # 2. Calculate p_hits if counts > 0
    for i in range(len(actual)):
        if guess[i] != actual[i] and guess[i] in counts and counts[guess[i]] > 0:
            p_hits += 1
            counts[guess[i]] -= 1
    
    return hits, p_hits

actual = 'RGBY'
guess = 'GGRR'
hits, p_hits = master_mind(guess, actual)
print('Hits: {}\nPseudo Hits: {}'.format(hits, p_hits))
