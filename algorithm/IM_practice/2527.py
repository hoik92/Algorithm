# for tc in range(4):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
#     if p1 > p2:
#         max_x = p1 + 1
#     else:
#         max_x = p2 + 1
#     if q1 > q2:
#         max_y = q1 + 1
#     else:
#         max_y = q2 + 1
#     m = [[0] * max_y for _ in range(max_x)]
#     for i in range(x1, p1 + 1):
#         for j in range(y1, q1 + 1):
#             m[i][j] = 1
#     for i in range(x2, p2 + 1):
#         for j in range(y2, q2 + 1):
#             if m[i][j] == 1:
#                 m[i][j] = 2
#
#     x_cnt, y_cnt = 0, 0
#     x_line, y_line = 0, 0
#     for i in range(x1, p1 + 1):
#         for j in range(y1, q1 + 1):
#             if m[i][j] == 2:
#                 y_cnt += 1
#             if y_cnt == 1:
#                 x_cnt += 1
#             if y_cnt >= 2:
#                 y_line = 1
#                 y_cnt = 0
#                 break
#         if x_cnt >= 2:
#             x_line = 1
#             x_cnt = 0
#             break
#
#     if x_line and y_line:
#         result = 'a'
#     elif (x_line and not y_line) or (not x_line and y_line):
#         result = 'b'
#     else:
#         if x_cnt or y_cnt:
#             result = 'c'
#         else:
#             result = 'd'
#
#     print(result)

result = []
for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if x2 < p1 and y2 < q1 and p2 > x1 and q2 > y1:
        result.append('a')
    elif x2 == p1 or x1 == p2:
        if y1 == q2 or q1 == y2:
            result.append('c')
        else:
            result.append('b')
    elif y2 == q1 or y1 == q2:
        if x1 == p2 or p1 == x2:
            result.append('c')
        else:
            result.append('b')
    else:
        result.append('d')
for i in result:
    print(i)