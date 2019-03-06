origin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ip = 10
a = [0] * (ip+1)
k = 0

def backtrack(a, k, ip):
    c = [0] * (ip+1)
    n = 0

    if k == ip:
        solution(a, ip)
    else:
        k += 1
        n = make(c, n)
        for i in range(n):
            a[k] = c[i]
            backtrack(a, k, ip)

def make(c, n):
    c[0] = 1
    c[1] = 0
    n = 2
    return n

def solution(a, ip):
    result = 0
    ans = []
    for i in range(1, ip+1):
        if a[i]:
            result += origin[i]
            ans.append(origin[i])
    if result == 20:
        print(ans)

backtrack(a, k, ip)