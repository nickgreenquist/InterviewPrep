def get_six_digits(N):
    N = N % 1000000
    string_N = str(N)
    if len(string_N) > 6:
        return int(string_N[-6:])
    return N

def init_matrix():
    return [
        [1,1],
        [1,0]
    ]

def deepcopy(A):
    return [row[:] for row in A]

def mat_mult(A, B):
    C = deepcopy(A)
    D = deepcopy(B)
    A[0][0] = (C[0][0]*D[0][0] + C[0][1]*D[1][0])% 1000000
    A[0][1] = (C[0][0]*D[0][1] + C[0][1]*D[1][1])% 1000000
    A[1][0] = (C[1][0]*D[0][0] + C[1][1]*D[1][0])% 1000000
    A[1][1] = (C[1][0]*D[0][1] + C[1][1]*D[1][1])% 1000000

def power(matrix, N):
    if N == 0 or N == 1:
        return

    power(matrix, int(N/2))
    mat_mult(matrix, matrix)

    if N % 2 != 0:
        mat_mult(matrix, init_matrix())


def fib(N):
    if N == 0:
        return 0
    matrix = init_matrix()
    power(matrix, N-1)
    return get_six_digits(matrix[0][0])

print(fib(10000000))
    