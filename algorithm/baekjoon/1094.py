stick = [64, 32, 16, 8, 4, 2, 1]
m, cnt = 0, 0
X = int(input())
while m != X:
    for i in range(7):
        if m + stick[i] <= X:
            m += stick[i]
            cnt += 1
print(cnt)
