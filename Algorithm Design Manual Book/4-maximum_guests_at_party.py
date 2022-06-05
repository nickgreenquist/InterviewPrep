def maxGuestsAtParty(entries, exists):
    entries = sorted(entries)
    exists = sorted(exits)

    n = len(entries)
    guests = 0
    max_guests = 0
    time = 0

    i = 0
    j = 0
    while (i < n and j < n):
        if entries[i] <= exits[j]:
            guests += 1
            if guests > max_guests:
                max_guests = guests
                time = entries[i]
            i += 1
        else:
            guests -= 1
            j += 1
    return time, max_guests


entries = [1, 2, 9, 5, 5]
exits = [4, 5, 12, 9, 12]

time, max_guests = maxGuestsAtParty(entries, exits)
print(time, max_guests)

