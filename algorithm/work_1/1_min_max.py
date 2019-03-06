# import sys
# sys.stdin = open('input.txt', 'r')

for i in range(int(input())):
    N = int(input())
    T = list(map(int, input().split()))
    tmax, tmin = T[0], T[0]
    for j in range(N):
        if tmax < T[j]:
            tmax = T[j]
        if tmin > T[j]:
            tmin = T[j]
    print(f"#{i + 1} {tmax - tmin}")