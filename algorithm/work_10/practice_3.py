"""
16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어 있다.
"""
ex = '0DEC'
ex = '0269FAC9A0'

hex_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

ex_bin = ''
for i in ex:
    ex_bin += hex_bin[i]
print(ex_bin)

n = len(ex_bin)
for i in range(n - 5):
    if ex_bin[i:i + 6] in pattern:
        idx = i
        break
print(idx)

while True:
    tmp = ex_bin[idx:idx + 6]
    if len(tmp) != 6:
        break

    for i in range(len(pattern)):
        if tmp == pattern[i]:
            print(i, end=' ')

    idx += 6
