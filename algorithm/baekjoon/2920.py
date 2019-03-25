n = list(map(int, input().split()))
for i in range(8):
    if n[i] == i + 1:
        result = 0
    else:
        result = -1
        break

if result != 0:
    for i in range(8):
        if n[i] == 8 - i:
            result = 1
        else:
            result = -1
            break

if result == 0:
    print('ascending')
elif result == 1:
    print('descending')
else:
    print('mixed')
