uniq = set()
seen = set()
def build(depth, k, length, short, longer):
    global uniq, seen
    if depth == k:
        uniq.add(length)
    else:
        seen_key = str(depth) + ' ' + str(length)
        if seen_key in seen:
            return
        build(depth + 1, k, length + short, short, longer)
        build(depth + 1, k, length + longer, short, longer)
        seen.add(seen_key)
    
def build_all_lengths(k, short, longer):
    global uniq
    build(0, k, 0, short, longer)
    return len(uniq)


short = 5
longer = 7
lengths = build_all_lengths(5, short, longer)
print(lengths)