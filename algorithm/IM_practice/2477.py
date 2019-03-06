K = int(input())
sjfqdl = 0
m = [0] * 6
for i in range(6):
    drt, length = map(int, input().split())
    m[i] = length

max_sjfqdl = 0
for i in range(6):
    tmp = m[i % 6] * m[(i + 1) % 6]
    sjfqdl += tmp
    if max_sjfqdl < tmp:
        max_sjfqdl = tmp
sjfqdl -= max_sjfqdl * 2

print(sjfqdl * K)