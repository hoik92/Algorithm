"""
문자열 교집합

문자열 집합은 알파멧 소문자로 이루어진 문자열들로 구성된 집합을 의미한다.

예를 들어 {"aba", "cdefasad", "wefawef"}은 문자열 3개로 구성된 한 개의 문자열 집합이다.

입력으로 2개의 문자열 집합이 주어졌을 때에, 두 집합에 모두 속하는 문자열 원소의 개수를 출력하는 프로그램을 작성하시오.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 첫 번째 줄에 두 집합의 원소의 갯수를 나타내는 두 자연수 N M(1≤N, M≤105)이 주어진다.

둘째 줄에는 첫 번째 집합의 원소 문자열들이 공백을 사이에 두고 주어진다.

셋째 줄에는 두 번째 집합의 원소 문자열들이 공백을 사이에 두고 주어진다.

각 문자열은 소문자 알파벳으로만 구성되며, 길이가 1 이상 50 이하임이 보장된다.

한 집합에 같은 문자열이 두 번 이상 등장하지 않음이 보장된다.

[출력]

각 테스트 케이스마다 첫째 줄에 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력한 다음, 공백을 하나 사이에 두고 해당 테스트 케이스의 답을 출력한다.

입력
2
2 3
ab a
a ac ba
3 3
aa bb cc
dd cc aa

출력
#1 1
#2 2
"""

# import sys
# sys.stdin = open('input.txt', 'r')

result = []
for tc in range(1, int(input())+1):
    a = input()
    N_list = input().split()
    M_list = input().split()

    cnt = 0
    for s in N_list:
        for i in range(len(M_list)):
            if s == M_list[i]:
                cnt += 1
                del M_list[i]
                break
    result.append(cnt)

for t in range(len(result)):
    print(f"#{t+1} {result[t]}")


# 시간 초과