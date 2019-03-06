# def f(n):
#     result = 0
#     for i in str(n):
#         result += int(i)
#     return result
#
# for tc in range(1, int(input())+1):
#     n = int(input())
#
#     while n // 10 != 0:
#         n = f(n)
#
#     print(f"#{tc} {n}")
#

def f(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result


result = []
for tc in range(1, int(input()) + 1):
    n = int(input())

    while n // 10 != 0:
        n = f(n)
    result.append(n)

for t in range(len(result)):
    print(f"#{t + 1} {result[t]}")