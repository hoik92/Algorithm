# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    print(f"#{tc+1} {2*M - N} {N - M}")