def backtrack(a, k, N):
    c = [0] * 2

    if k == N:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, N, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, N)


def construct_candidates(a, k, N, c):
    c[0] = 1
    c[1] = 0
    return 2


def process_solution(a, k):
    for i in range(len(a)):
        if a[i]:
            print(i, end=' ')
    print()


a = [0] * 100
backtrack(a, 0, 3)