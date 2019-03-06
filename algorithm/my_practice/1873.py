import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    H, W = map(int, input().split())
    m = []
    tmp = []
    h_idx, w_idx = 0, 0
    for h in range(H):
        s = input()
        for i in s:
            tmp.append(i)
        m.append(tmp)
        tmp = []
    
    N = int(input())
    C = input()
    for i in range(H):
        if '^' in m[i]:
            h_idx, w_idx = i, m[i].index('^')
        elif 'v' in m[i]:
            h_idx, w_idx = i, m[i].index('v')
        elif '<' in m[i]:
            h_idx, w_idx = i, m[i].index('<')
        elif '>' in m[i]:
            h_idx, w_idx = i, m[i].index('>')

    for i in range(N):
        if C[i] == 'U':
            if h_idx == 0:
                m[h_idx][w_idx] = '^'
            elif m[h_idx-1][w_idx] == '.':
                m[h_idx][w_idx] = '.'
                m[h_idx-1][w_idx] = '^'
                h_idx -= 1
            else:
                m[h_idx][w_idx] = '^'
        elif C[i] == 'D':
            if h_idx == H-1:
                m[h_idx][w_idx] = 'v'
            elif m[h_idx+1][w_idx] == '.':
                m[h_idx][w_idx] = '.'
                m[h_idx+1][w_idx] = 'v'
                h_idx += 1
            else:
                m[h_idx][w_idx] = 'v'
        elif C[i] == 'L':
            if w_idx == 0:
                m[h_idx][w_idx] = '<'
            elif m[h_idx][w_idx-1] == '.':
                m[h_idx][w_idx] = '.'
                m[h_idx][w_idx-1] = '<'
                w_idx -= 1
            else:
                m[h_idx][w_idx] = '<'
        elif C[i] == 'R':
            if w_idx == W-1:
                m[h_idx][w_idx] = '>'
            elif m[h_idx][w_idx+1] == '.':
                m[h_idx][w_idx] = '.'
                m[h_idx][w_idx+1] = '>'
                w_idx += 1
            else:
                m[h_idx][w_idx] = '>'
        else:
            if m[h_idx][w_idx] == '^':
                for j in range(h_idx, -1, -1):
                    if m[j][w_idx] == '*':
                        m[j][w_idx] = '.'
                        break
                    elif m[j][w_idx] == '#':
                        break
            elif m[h_idx][w_idx] == 'v':
                for j in range(h_idx, H):
                    if m[j][w_idx] == '*':
                        m[j][w_idx] = '.'
                        break
                    elif m[j][w_idx] == '#':
                        break
            elif m[h_idx][w_idx] == '<':
                for j in range(w_idx, -1, -1):
                    if m[h_idx][j] == '*':
                        m[h_idx][j] = '.'
                        break
                    elif m[h_idx][j] == '#':
                        break
            elif m[h_idx][w_idx] == '>':
                for j in range(w_idx, W):
                    if m[h_idx][j] == '*':
                        m[h_idx][j] = '.'
                        break
                    elif m[h_idx][j] == '#':
                        break

    print(f"#{tc+1}", end=' ')
    for i in range(H):
        for j in range(W):
            print(m[i][j], end='')
        print()