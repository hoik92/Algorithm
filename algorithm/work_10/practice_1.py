"""
0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
"""
ex = "0000000111100000011001100001100110000110000111100111100111111001100111"
n = len(ex) // 7
m = [0] * n

for i in range(n):
    m[i] = ex[7*i:7*(i+1)]
# print(m)

for i in m:
    result = 0
    for j in range(7):
        result += int(i[6 - j]) * (1 << j)
    print(result, end=' ')
