"""
사랑은 타이밍

빼빼로 데이에 빼빼로를 들고 소개팅에서 바람을 맞은 태혁이를 지켜본 친구들은 그 비참함을 극대화하기 위해 태혁이가 바람을 맞으며 기다린 시간을 계산하기로 하였다.

소개팅 약속 시간은 정확히 2011년 11월 11일 오전 11시 11분이었으며 태혁이가 깨달음을 얻은 시간은 D일 H시 M분이었다.

깨달음을 주기 위해 바람이 얼마나 오랫동안 노력하였는지 계산하는 프로그램을 작성하시오.

[입력]
첫째 줄에는 테스트 케이스의 수 T (T ≤ 10)가 주어진다.

테스트 케이스의 각 줄에는 3개의 정수 D (11 ≤ D ≤ 14), H (0 ≤ H ≤ 23), M (0 ≤ M ≤ 59) 이 주어진다.

[출력]
각각의 케이스마다 각 줄에 태혁이가 얼마나 오랫동안 바람을 맞았는지 분 단위로 출력한다.

만약 태혁이가 소개팅 약속 시간 전에 차였다면 놀리기엔 너무 불쌍하므로 -1을 출력한다.

입력
3
14 23 59
11 11 11
11 3 7

출력
#1 5088
#2 0
#3 -1
"""

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    stdD, stdH, stdM = 11, 11, 11
    D, H, M = map(int, input().split())

    reD, reH, reM = D-stdD, H-stdH, M-stdM
    if reD < 0:
        result = -1
    elif reD == 0 and reH < 0:
        result = -1
    elif reD == 0 and reH == 0 and reM < 0:
        result = -1
    else:
        result = reD * 24 * 60 + reH * 60 + reM

    print(f"#{tc} {result}")