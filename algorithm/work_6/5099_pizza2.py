class Queue:
    def __init__(self, N):
        self.N = N
        self.queue = [0] * (self.N + 1)
        self.front, self.rear = 0, 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % (self.N + 1)

    def enQueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % (self.N + 1)
            self.queue[self.rear] = item

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % (self.N + 1)
            item = self.queue[self.front]
            self.queue[self.front] = 0
            return item

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    for i in range(M):
        C[i] = [i, C[i]]

    q = Queue(N)
    cnt, idx = 0, 0
    while cnt != N + 1:
        if idx != M and not q.isFull():
            q.enQueue(C[idx])
            idx += 1
        else:
            item = q.deQueue()
            C[item[0]][1] = C[item[0]][1] // 2
            if C[item[0]][1] == 0:
                result = item[0]
            else:
                q.enQueue(C[item[0]])

        if idx == M:
            cnt = 0
            for i in range(N + 1):
                if q.queue[i] == 0:
                    cnt += 1
                else:
                    break

    print(f"#{tc} {result + 1}")