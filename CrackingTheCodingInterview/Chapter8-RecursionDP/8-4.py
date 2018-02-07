def printPowerSet(s, s_size):
    pow_set_size = pow(2, s_size)
    counter = 0
    j = 0
 
    for counter in range(0, pow_set_size):
        new_set = ""
        for j in range(0, s_size):
            #Check if jth bit in the counter is set
            #If set then pront jth element from set */
            if counter & (1<<j):
                new_set += str(s[j])
        print(new_set)
        

s = [1,2,3]
printPowerSet(s, len(s))