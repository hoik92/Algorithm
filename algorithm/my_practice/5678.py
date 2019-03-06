"""
팰린드롬

어떤 단어가 뒤에서 앞으로 거꾸로 썼을 때 원래의 단어와 같으면 이를 팰린드롬이라고 한다.

예를 들어 “MADAM”은 뒤에서 앞으로 읽어도 “MADAM”이기 때문에 팰린드롬이다.

그러나 “DOG”는 뒤에서 앞으로 읽으면 “GOD”이기 때문에 팰린드롬이 아니다.

“DOGGOD”은 뒤에서 앞으로 읽으면 “DOGGOD”이므로 팰린드롬이다.

알파벳 대문자들로만 이루어진 문자열이 하나 주어질 때, 가장 긴 팰린드롬 부분문자열의 길이를 구하는 프로그램을 작성하라.

예를 들면 “AQDOGGODZ”의 가장 긴 팰린드롬 부분문자열은 “DOGGOD”으로 길이는 6이다.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 15)

각 테스트 케이스의 첫 줄에는 문자열이 주어진다.

이 문자열은 알파벳 대문자들로만 이루어져 있으며, 길이는 1이상 1000이하이다.

[출력]
각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 가장 긴 Palindrome Subsequence 의 길이를 출력한다.

입력
1
BBABCBCAB

출력
#1 7
"""

# for tc in range(1, int(input())+1):
#     s = list(input())
#     n = len(s)
#     idx = 0
#     mx_len = 1
#     # while idx < len(s)-1:
#     #     for i in range(idx+3, len(s)):
#     #         if len(s[idx:i]) > mx_len:
#     #             if s[idx:i] == s[idx:i][::-1] and mx_len < len(s[idx:i]):
#     #                 mx_len = len(s[idx:i])
#     #     idx += 1
#     result = []
#     for i in range(1<<n):
#         tmp = []
#         for j in range(n):
#             if i & (1<<j):
#                 tmp.append(s[j])
#         # print(tmp)
#         result.append(tmp)
#     for i in result:
#         if i == i[::-1] and mx_len < len(i):
#             mx_len = len(i)
#     print(f"#{tc} {mx_len}")

# ???????????????????????

for tc in range(1, int(input())+1):
    s = input()
    n = len(s)

    cnt = 0
    for i in range(n):
        if n - i > cnt:
            for j in range(n, i + cnt, -1):
                tmp = s[i:j]
                if tmp == tmp[::-1] and len(tmp) > cnt:
                    cnt = len(tmp)
                    break
    print(f"#{tc} {cnt}")