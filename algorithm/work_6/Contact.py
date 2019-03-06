import sys
sys.stdin = open('inputContact.txt', 'r')

class Queue:
    def __init__(self, N):
        self.N = N
        self.front, self.rear = -1, -1
        self.queue = [0] * (N + 1)

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.N

    def enQueue(self, item):
        if not self.isFull():
            self.rear += 1
            self.queue[self.rear] = item

    def deQueue(self):
        if not self.isEmpty():
            self.front += 1
            item = self.queue[self.front]
            self.queue[self.front] = 0
            return item

def BFS(s):
    global q, n
    cnt, result = 0, [0, 0]
    q.enQueue([s, cnt])
    visited[s] = 1
    while not q.isEmpty():
        item = q.deQueue()
        s, cnt = item[0], item[1]
        for i in m:
            if i[0] == s and not visited[i[1]]:
                cnt += 1
                visited[i[1]] = 1
                q.enQueue([i[1], cnt])
                cnt -= 1
        if cnt > result[1]:
            result = item
        elif cnt == result[1] and s > result[0]:
            result = item
    return result

for tc in range(1, 11):
    N, s = map(int, input().split())
    M = list(map(int, input().split()))
    n = N // 2
    m = [0] * n
    visited = [0] * 101

    for i in range(n):
        m[i] = [M[2 * i], M[2 * i + 1]]

    q = Queue(n)
    result = BFS(s)
    print(f"#{tc} {result[0]}")