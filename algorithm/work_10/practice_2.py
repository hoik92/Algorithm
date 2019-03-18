"""
16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자.
"""
# ex = '0F97A3'
ex = '01D06079861D79F99F'

hex_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

ex_bin = ''
for i in ex:
    ex_bin += hex_bin[i]

n = len(ex_bin) // 7
l = len(ex_bin) % 7
t = n + 1 if l else n

for i in range(t):
    tmp = ex_bin[7 * i:7 * (i + 1)]
    result = 0
    for j in range(len(tmp)):
        result += int(tmp[len(tmp) - 1 - j]) * (1 << j)
    print(result, end=' ')
