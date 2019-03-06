w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x, y = p, q
# dx, dy = 1, 1
# for i in range(t):
#     if 0 < x < w and 0 < y < h:
#         pass
#     elif 0 < y < h:
#         dx = -dx
#     elif 0 < x < w:
#         dy = -dy
#     else:
#         dx = -dx
#         dy = -dy
#     x += dx
#     y += dy
# print(x, y)

xt = t - w + p
if (xt // w) % 2 :
    x = 0
else:
    x = w
if x == 0:
    x = x + (xt % w)
else:
    x = x - (xt % w)

yt = t - h + q
if (yt // h) % 2:
    y = 0
else:
    y = h
if y == 0:
    y = y + (yt % h)
else:
    y = y - (yt % h)
print(x, y)