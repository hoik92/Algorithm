import sys
sys.stdin = open('input.txt', 'r')

def mx_mn(T):
    mxidx, mnidx = 0, 0
    for i in range(len(T)):
        if T[mxidx] < T[i]:
            mxidx = i
        if T[mnidx] > T[i]:
            mnidx = i
    return mxidx, mnidx

for tc in range(1, 11):
    D = int(input())
    T = list(map(int, input().split()))
    
    for x in range(D):
        mxidx, mnidx = mx_mn(T)
        T[mxidx] -= 1
        T[mnidx] += 1
        
    mxidx, mnidx = mx_mn(T)
            
    print(f"#{tc} {T[mxidx] - T[mnidx]}")

    # for x in range(D):
    #     T[T.index(max(T))] -= 1
    #     T[T.index(min(T))] += 1
    
    # print(f"#{tc} {max(T) - min(T)}")