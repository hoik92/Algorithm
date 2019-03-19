number = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
          '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
for tc in range(1, int(input())+1):
    N, s = input().split()
    N = int(N)

    result = ''
    for i in s:
        if ord(i) >= ord('A'):
            result += number[ord(i) - ord('A') + 10]
        else:
            result += number[ord(i) - ord('0')]

    print(f"#{tc} {result}")
