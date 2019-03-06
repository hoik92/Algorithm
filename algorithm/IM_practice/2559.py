N, K = map(int, input().split())
temp = list(map(int, input().split()))
result = []
tmp = 0
for j in range(K):
    tmp += temp[j]
result.append(tmp)
for i in range(K, N):
    tmp -= temp[i - K]
    tmp += temp[i]
    result.append(tmp)
print(max(result))