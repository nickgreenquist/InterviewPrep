from random import randint

def shuffle(cards, i):
    if i == 0:
        return cards
    
    shuffle(cards, i - 1)

    k = randint(0, i)
    tmp = cards[k]
    cards[k] = cards[i]
    cards[i] = tmp

    return cards


cards = [1,2,3,4,5,6,7,8,9,10]
shuffle(cards, len(cards) - 1)
print(cards)