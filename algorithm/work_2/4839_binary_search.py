# import sys
# sys.stdin = open('input.txt', 'r')

def binary_search(P, goal):
    start = 1
    end = P
    mid = (start + end) // 2
    cnt = 1

    while mid != goal:
        if goal > mid:
            start = mid
        else:
            end = mid
        mid = (start + end) // 2
        cnt += 1
    return cnt

def winner(cntA, cntB):
    if cntA < cntB:
        return 'A'
    elif cntA > cntB:
        return 'B'
    else:
        return 0

for tc in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    
    cntA = binary_search(P, A)
    cntB = binary_search(P, B)

    win = winner(cntA, cntB)

    print(f"#{tc} {win}")