def decompress(S):
    if not S[0].isdigit():
        return S
    i = 0
    ans = ''
    while i < len(S):
        # 0 if not a number, read append the rest of the sting and return
        if not S[i].isdigit():
            ans += S[i:len(S)]
            return ans

        # 1. Read whole digit
        num = ''
        while S[i].isdigit():
            num += S[i]
            i += 1
        num = int(num)

        # 2. Get full text in between first open and matching close bracket
        i += 1
        open_brackets = 1
        closed_brackets = 0
        sub_S = ''
        while open_brackets > closed_brackets:
            sub_S += S[i]
            if S[i] == ']':
                closed_brackets += 1
            if S[i] == '[':
                open_brackets += 1
            i += 1

        # 3. Recursive call string inside brackts
        dec_S = decompress(sub_S[0:len(sub_S) - 1]) # remove last closing bracket

        # 4. Append text from inside bracket num times
        for j in range(num):
            ans += dec_S
    return ans


print(decompress('3[abc]4[ab]c')) # abcabcabcababababc
print(decompress('10[a]')) # aaaaaaaaaa
print(decompress('2[3[a]b]')) # aaabaaab
print(decompress('2[2[2[2[2[2[2[a]]]]]]]')) # a printed 2^7 times


