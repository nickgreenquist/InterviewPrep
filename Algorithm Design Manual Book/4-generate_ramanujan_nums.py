import math

def generate_ramanujan_nums(n):
    cube_of_n = int(math.pow(n, 1/3) + 1)

    # map of sum of pair of cubes to the pairs
    sum_of_cubes_to_pair = {}
    
    r_nums = {}
    for i in range(1, cube_of_n):
        for j in range(1, cube_of_n):
            s = i**3 + j**3
            pair = ','.join(sorted([str(i), str(j)]))

            if s in sum_of_cubes_to_pair:
                sum_of_cubes_to_pair[s].add(pair)
            else:
                sum_of_cubes_to_pair[s] = {pair}

    for sum_of_cubes, pairs in sum_of_cubes_to_pair.items():
        if len(pairs) > 1:
            print(sum_of_cubes, pairs)

generate_ramanujan_nums(25_000)
