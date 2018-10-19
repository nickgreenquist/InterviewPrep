from random import randint

'''
    Ugly but FAST solution. Beats 99.6% of all Leetcode submissions
'''
def numberToWords(num):
    mapper = {
        1: 'One',
        2: 'Two',
        3: "Three",
        4: 'Four',
        5: "Five",
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: "Twelve",
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: "Forty",
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety'
    }
    base = {
        1: 'Thousand',
        2: 'Million',
        3: 'Billion'
    }

    def chunker(num):
        num_list = [int(c) for c in str(num)][::-1]
        chunks = []
        for i in range(0, len(num_list), 3):
            chunks.append(num_list[i:i + 3][::-1])
        return chunks[::-1]
    
    '''
        Brute force but it works!
    '''
    def parseChunk(num, mapper):
        if num[0] == 0 and num[1] == 0 and num[2] == 0: # 000
            return ""
        if num[0] == 0 and num[1] == 0 and num[2] != 0: # 001
            return mapper[num[2]]
        if num[0] == 0 and num[1] != 0 and num[2] == 0: # 010
            return mapper[num[1]*10]
        if num[0] != 0 and num[1] == 0 and num[2] == 0: # 100
            return mapper[num[0]] + " Hundred"
        if num[0] == 0 and num[1] != 0 and num[2] != 0: # 011
            if num[1]*10 + num[2] in mapper: # 11
                return mapper[num[1]*10 + num[2]]
            else: # 21
                return mapper[num[1]*10] + ' ' + mapper[num[2]]
        if num[0] != 0 and num[1] != 0 and num[2] == 0: # 110
            return mapper[num[0]] + ' Hundred ' + mapper[num[1]*10]
        if num[0] != 0 and num[1] == 0 and num[2] != 0: # 101
            return mapper[num[0]] + ' Hundred ' + mapper[num[2]]
        if num[0] != 0 and num[1] != 0 and num[2] != 0: # 111
            if num[1]*10 + num[2] in mapper: # 111
                return mapper[num[0]] + ' Hundred ' + mapper[num[1]*10 + num[2]]
            else: # 121
                return mapper[num[0]] + ' Hundred ' + mapper[num[1]*10] + ' ' + mapper[num[2]]
        return ""     
    
    if num == 0:
        return "Zero"
    
    chunks = chunker(num)

    # fix the first chunk
    if len(chunks[0]) == 1:
        chunks[0] = [0,0,chunks[0][0]]
    elif len(chunks[0]) == 2:
        chunks[0] = [0, chunks[0][0], chunks[0][1]]
    
    sb = ""
    base_id = 1
    first_chunk = parseChunk(chunks[-1], mapper)
    i = len(chunks) - 2
    while i >= 0:
        c = parseChunk(chunks[i], mapper)
        sb = c + ' ' + base[base_id] + ' ' + sb
        i -= 1
        base_id += 1
    sb = sb + ' ' + first_chunk

    return " ".join(sb.split())

for i in range(20):
    r = randint(0, 99999999)
    print("{}: {}".format(r, numberToWords(r)))
        