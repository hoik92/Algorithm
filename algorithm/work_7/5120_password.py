class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addtoLast(self, item):
        if self.tail == None:
            new = Node(item)
            self.tail = new
            self.head = new
        else:
            new = Node(item, self.tail)
            self.tail.next = new
            self.tail = new
            self.head.prev = self.tail
            self.tail.next = self.head

    def add(self, cur, item):
        if cur == self.tail:
            self.addtoLast(item)
        else:
            new = Node(item, cur, cur.next)
            cur.next.prev = new
            cur.next = new

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    m = list(map(int, input().split()))

    linked = LinkedList()
    for i in m:
        linked.addtoLast(i)

    p = linked.head
    for i in range(K):
        for j in range(M - 1):
            p = p.next
        linked.add(p, p.item + p.next.item)
        p = p.next

    if N + K >= 10:
        cnt = 10
    else:
        cnt = N + K
    print("#{}".format(tc), end=' ')
    p = linked.tail
    for i in range(cnt):
        print(p.item, end=' ')
        p = p.prev
    print()