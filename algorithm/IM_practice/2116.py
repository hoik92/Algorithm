def find_top(dice, bot):
    for i in range(6):
        if dice[i] == bot:
            if i == 0:
                return dice[5]
            elif i == 1:
                return dice[3]
            elif i == 2:
                return dice[4]
            elif i == 3:
                return dice[1]
            elif i == 4:
                return dice[2]
            else:
                return dice[0]

N = int(input())
dice = [0] * N
ans = []
for i in range(N):
    dice[i] = list(map(int, input().split()))

for i in range(1, 7):
    top = i
    result = 0
    for j in range(N):
        bot = top
        top = find_top(dice[j], bot)
        tmp = []
        for k in range(6):
            if dice[j][k] != top and dice[j][k] != bot:
                tmp.append(dice[j][k])
        result += max(tmp)
    ans.append(result)
print(max(ans))