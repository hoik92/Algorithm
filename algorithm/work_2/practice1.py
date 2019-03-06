"""
5x5 2차 배열에 무작위로 25개의 숫자로 초기화한 후
25개의 각 요소에 대해서 그 요소와 이숫한 요소와의 차의 절대값을 구하시오.

25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
"""

arr = []
for i in range(7):
    arr.append([0]*7)

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5:
            arr[i][j] = 1
        if j == 1 or j == 5:
            arr[i][j] = 1

for j in range(7):
    arr[0][j] = arr[1][j]
    arr[6][j] = arr[5][j]
for i in range(7):
    arr[i][0] = arr[i][1]
    arr[i][6] = arr[i][5]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(4):
            result += abs(arr[i + dx[k]][j + dy[k]] - arr[i][j])

print(result)


# arr = []
# for i in range(5):
#     arr.append([0]*5)

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4:
#             arr[i][j] = 1
#         if j == 0 or j == 4:
#             arr[i][j] = 1

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# result = 0
# for i in range(5):
#     for j in range(5):
#         for k in range(4):
#             if i + dx[k] >= 0 and j + dy[k] >= 0 and i + dx[k] <= 4 and j + dy[k] <= 4:
#                 result += abs(arr[i + dx[k]][j + dy[k]] - arr[i][j])

# print(result)