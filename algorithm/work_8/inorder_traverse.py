def inorder(t):
    if t:
        inorder(tree[t][0])
        print(m[t], end='')
        inorder(tree[t][1])

for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 2 for _ in range(N + 1)]
    m = [0] * (N + 1)
    for i in range(N):
        M = input().split()
        len_M = len(M)
        m[int(M[0])] = M[1]
        if len_M == 3:
            tree[int(M[0])][0] = int(M[2])
        elif len_M == 4:
            tree[int(M[0])][0] = int(M[2])
            tree[int(M[0])][1] = int(M[3])
    print(tree)
    print("#{}".format(tc), end=' ')
    inorder(1)
    print()