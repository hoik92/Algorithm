# for tc in range(1, int(input())+1):
#     N = int(input())
#     m = [0] * N
#     for i in range(N):
#         m[i] = list(map(int, input().split()))
#     people = [0] * 10
#     stair = [0] * 2
#     p_idx, s_idx, c_idx = 0, 0, 0
#     for i in range(N):
#         for j in range(N):
#             if m[i][j] == 1:
#                 people[p_idx] = (i, j)
#                 p_idx += 1
#             elif m[i][j] > 1:
#                 stair[s_idx] = (i, j, m[i][j])
#                 s_idx += 1
#
#     cur = [[0] * 2 for _ in range(p_idx)]
#     for i in range(p_idx):
#         for j in range(2):
#             cur[c_idx][j] = [abs(people[i][0] - stair[j][0]) + abs(people[i][1] - stair[j][1]), stair[j][2]]
#         c_idx += 1
#     print(people)
#     print(stair)
#     print(cur)
#
#     time, idx = 0, 0
#     count = [0, 0]
#     tmp = []
#     while time < 10:
#         time += 1
#         for i in range(len(cur)):
#             for j in range(2):
#                 cur[i][j][0] -= 1
#                 if cur[i][j][0] == 0:
#                     tmp.append((i, j))
#         print(cur)
#         while tmp:
#             x, y = tmp.pop(0)
#             if count[y] < 3:
#                 count[y] += 1
#             elif y:
#                 if sum(cur[x][0]) > sum(cur[x][1]):
#                     cur[x][y][0] += 1
#                 else:
