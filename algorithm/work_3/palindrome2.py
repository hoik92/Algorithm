import sys
sys.stdin = open('input.txt', 'r')

def find_pal(M, max_cnt):
    for i in range(100):
        j = 0
        while 101 - j > max_cnt:
            for k in range(100-j, max_cnt-1, -1):
                if M[i][j:j+k] == M[i][j:j+k][::-1]:
                    max_cnt = k
                    break
            j += 1

    return max_cnt

# def find_pal2(M, max_cnt):
#     for i in range(100):
#         for j in range(100):
#             for k in range(max_cnt, 101-j):
#                 s1 = M[i][j:j+k]
#                 s2 = ''
#                 for l in range(k):
#                     s2 += M[j+l][i]
#                 if (s1 == s1[::-1] or s2 == s2[::-1]) and k > max_cnt:
#                     max_cnt = k
#     return max_cnt

result = [0] * 10
for tc in range(10):
    t = input()
    M = [0] * 100

    for i in range(100):
        M[i] = list(input())

    max_cnt = find_pal(M, 1)

    for i in range(100):
        for j in range(100):
            if i < j:
                M[i][j], M[j][i] = M[j][i], M[i][j]

    max_cnt = find_pal(M, max_cnt)
    result[tc] = max_cnt

for tc in range(10):
    print(f"#{tc+1} {result[tc]}")
