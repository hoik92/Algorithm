import sys
sys.stdin = open('input.txt', 'r')

def find_idx():
    global n, M
    for i in range(n):
        idx = M * 4 - 1
        while idx >= 0:
            if new[i][idx] == '1':
                multi = 1
                while True:
                    tmp = ''
                    if idx - 56 * multi >= 0:
                        for j in range(7):
                            tmp += new[i][idx - 6 * multi + j * multi]
                    if tmp in pattern:
                        dlTsi = new[i][idx - 55 * multi:idx + 1:multi]
                        if dlTsi not in pt:
                            if confirm(dlTsi):
                                ans = multi
                                pt.append(dlTsi)
                    multi += 1
                    if multi == 6:
                        break
                idx -= 56 * ans
            else:
                idx -= 1


def confirm(s):
    global N, M, result, tc
    clghks = [0] * 8
    con = 0
    for i in range(8):
        for j in range(10):
            if s[7 * i:7 * (i + 1)] not in pattern:
                return
            if pattern[j] == s[7 * i:7 * (i + 1)]:
                clghks[i] = j
                break
    for i in range(8):
        if i % 2:
            con += clghks[i]
        else:
            con += clghks[i] * 3
    if con % 10 == 0:
        result += sum(clghks)
        # if tc == 20:
            # print(result)
    return 1


number = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = []
    for i in range(N):
        what = input()
        if what != '0' * M and what not in m:
            m.append(what)

    n = len(m)
    new = [''] * n
    for i in range(n):
        for j in range(M):
            new[i] += number[m[i][j]]

    pt = []
    result = 0
    find_idx()

    print(f"#{tc} {result}")
