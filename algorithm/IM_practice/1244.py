N = int(input())
switch = list(map(int, input().split()))
stN = int(input())
for i in range(stN):
    gender, idx = map(int, input().split())
    if gender == 1:
        n = 1
        while idx * n <= N:
            if switch[idx * n - 1]:
                switch[idx * n - 1] = 0
            else:
                switch[idx * n - 1] = 1
            n += 1
    elif gender == 2:
        if switch[idx - 1]:
            switch[idx - 1] = 0
        else:
            switch[idx - 1] = 1
        n = 1
        while idx - n - 1 >= 0 and idx + n - 1 < N and switch[idx - n - 1] == switch[idx + n - 1]:
            if switch[idx - n - 1]:
                switch[idx - n - 1], switch[idx + n - 1] = 0, 0
            else:
                switch[idx - n - 1], switch[idx + n - 1] = 1, 1
            n += 1

for i in range(N):
    if i == 20 or i == 40 or i == 60 or i == 80:
        print()
    print(switch[i], end=' ')