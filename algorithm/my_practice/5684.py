"""
운동

N개의 건물과 M개의 도로로 구성되어 있는 마을이 있다.

도로는 건물과 건물 사이에 놓여 있으며, 일방 통행 도로이다.

건물의 번호는 1번부터 N번까지 각각 주어져있다.

원철이는 마을의 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다.

운동을 한 후에는 다시 시작점으로 돌아오는 것이 편하기 때문에, 원철이는 사이클을 찾기를 원한다.

단, 운동을 하는 도중 무슨 일이 생길지 모르므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오.

두 마을을 왕복하는 경우도 사이클에 포함됨에 주의하시오.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)

각 테스트 케이스의 첫 번째 줄에 건물의 수 N과 도로의 수 M이 주어진다. (2 ≤ N ≤ 400, 2 ≤ M ≤ N*(N-1))

각 테스트 케이스의 두 번째 줄부터 M개의 줄에 걸쳐 도로의 정보 s, e, c가 주어진다.

이는 s번 건물으로부터 e번 건물으로 이동하는 길이 c의 일방 통행 도로가 있다는 의미이다.

거리는 10,000 이하의 자연수이고, 같은 시작점과 도착점을 가진 간선은 최대 한 개 등장한다.

[출력]
각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 도로의 길이의 합이 가장 작은 사이클의 길이를 출력한다. 만약, 그러한 사이클을 찾을 수 없다면 -1을 출력한다.

입력
1
3 4
1 2 1
3 2 1
1 3 5
2 3 2

출력
#1 3
"""
# 샘플은 동작하지만 런타임 에러
def backtrack(m, s, k, N):
    global cnt, min_cnt
    # visited[s] = 1
    if cnt > min_cnt:
        return
    if k == N:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    else:
        k += 1
        for i in m:
            if i[0] == s and not visited[i[1]]:
                cnt += i[2]
                visited[i[1]] = 1
                backtrack(m, i[1], k, N)
                cnt -= i[2]
                visited[i[1]] = 0

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [0] * M
    visited = [0] * (N+1)
    for i in range(M):
        m[i] = list(map(int, input().split()))

    max_cnt = m[0][2]
    for i in range(1, M):
        if max_cnt < m[i][2]:
            max_cnt = m[i][2]

    min_cnt = max_cnt * M
    for i in range(1, N):
        cnt = 0
        visited[i] = 1
        backtrack(m, i, 1, N)
        visited[i] = 0

    if min_cnt == max_cnt * M:
        min_cnt = -1

    print(f"#{tc} {min_cnt}")