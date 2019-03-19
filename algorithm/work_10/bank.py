def bin_dec(num):
    result = 0
    for i in range(len(num)):
        result += int(num[len(num) - 1 - i]) * (1 << i)
    return result


def tri_dec(num):
    result = 0
    for i in range(len(num)):
        result += int(num[len(num) - 1 - i]) * (3 ** i)
    return result


def find_result(num2, num3):
    for i in range(len(num2)):
        tmp2 = list(num2)
        if num2[i] == '0':
            tmp2[i] = '1'
        else:
            tmp2[i] = '0'
        tmp2 = ''.join(tmp2)
        for j in range(len(num3)):
            for k in range(3):
                tmp3 = list(num3)
                if int(num3[j]) != k:
                    tmp3[j] = str(k)
                    tmp3 = ''.join(tmp3)
                    if bin_dec(tmp2) == tri_dec(tmp3):
                        return bin_dec(tmp2)


for tc in range(1, int(input())+1):
    num2 = input()
    num3 = input()

    result = find_result(num2, num3)
    print(f"#{tc} {result}")
