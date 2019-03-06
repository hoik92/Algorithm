N = int(input())
m = [0] * 1001
for i in range(N):
    idx, height = list(map(int, input().split()))
    m[idx] = height

max_height = m[0]
for i in range(1001):
    if m[i] > max_height:
        max_height = m[i]
        max_idx = i

height = m[0]
for i in range(max_idx):
    if m[i] > height:
        height = m[i]
    m[i] = height

height = m[1000]
for i in range(1000, max_idx, -1):
    if m[i] > height:
        height = m[i]
    m[i] = height

result = 0
for i in range(1001):
    result += m[i]
print(result)