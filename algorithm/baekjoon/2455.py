cnt, max_cnt = 0, 0
for i in range(4):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)