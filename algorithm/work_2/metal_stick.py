# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))

    A_ = []
    for i in range(N):
        tmp = A[2*i:2*i+2]
        A_.append(tmp)

    res = [A_.pop(0)]
    for i in range(N):
        l = len(A_)
        for j in range(l):
            if A_[j][0] == res[len(res)-1][1]:
                res.append(A_.pop(j))
                break
            if A_[j][1] == res[0][0]:
                res.insert(0, A_.pop(j))
                break
    
    print(f"#{tc}", end=' ')
    for i in range(len(res)):
        for j in range(2):
            print(res[i][j], end=' ')
    print()