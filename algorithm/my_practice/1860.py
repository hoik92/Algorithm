import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))

    bbang = 0
    time = 0
    result = 'Possible'
    while time <= max(N_list):
        time += 1
        if result == 'Impossible':
            break
        if 0 in N_list:
            result = 'Impossible'
            break
        if time % M == 0:
            bbang += K
        if time in N_list:
            bbang -= N_list.count(time)
            if bbang < 0:
                result = 'Impossible'
                break
            
    print(f"#{tc+1} {result}")