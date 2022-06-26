'''
Given the following words in dictionary,

[
"wrt",
"wrf",
"er",
"ett",
"rftt"
]
The correct order is: "wertf".
'''

def dfs(graph, v, state, top_sort_processed):
    state[v] = 1 # DISCOVERED

    for u in graph[v]:
        if state[u] == 1: # DISCOVERED
            print('CYCLE!')
            break
        if state[u] == 0: # UNSEEN
            dfs(graph, u, state, top_sort_processed)
    
    state[v] = 2 # PROCESSED
    top_sort_processed.append(v)


def topSort(graph):
    state = {}
    for i in range(len(graph)):
        state[i] = 0 # UNSEEN

    top_sort_processed = []
    for i in range(len(graph)):
        if state[i] == 0:
            dfs(graph, i, state, top_sort_processed)
    
    return top_sort_processed[::-1]


# Create a graph out of words
def alienD(words):
    # letter to index mappings
    letter_to_index = {}
    index_to_letter = {}

    i = 0
    for word in words:
        for letter in word:
            if letter not in letter_to_index:
                letter_to_index[letter] = i
                index_to_letter[i] = letter

                i += 1
            
    # adj list graph
    graph = [set() for i in range(len(letter_to_index.keys()))]

    # for every pair of words, go through letter by letter and for every mismatch, 
    # create an edge between those two letters.
    x = 0
    z = 0
    for x in range(len(words)):
        for y in range(x + 1, len(words)):
            word1 = words[x]
            word2 = words[y]
            i = 0
            j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    # create edge word[i] -> word[j]
                    src = letter_to_index[word1[i]]
                    dest = letter_to_index[word2[j]]
                    graph[src].add(dest)
                    
                    # move on to next word
                    i = len(word1)
                    j = len(word2)
                i += 1
                j += 1

    print(graph)
    
    # get top-sort of letter graph
    top_sort_processed = topSort(graph)

    for v in top_sort_processed:
        letter = index_to_letter[v]
        print(letter)



words = [
"wrt",
"wrf",
"er",
"ett",
"rftt"
]
# expected: The correct order is: "wertf".
alienD(words)

words = [
    'QQZ',
    'QZZ',
    'XQZ',
    'XQX',
    'XXX'
]
# Q before X, Q efore Z, Z before X
alienD(words)
