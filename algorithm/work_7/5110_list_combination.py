class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # def addtoFirst(self, item):
    #     new = Node(item)
    #     if self.head == None:
    #         self.head = new
    #         self.tail = new
    #     else:
    #         self.head.prev = new
    #         new.next = self.head
    #         self.head = new

    def addtoLast(self, item):
        new = Node(item)
        if self.tail == None:
            self.tail = new
            self.head = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    # def add(self, idx, item):
    #     if idx == 0:
    #         self.addtoFirst(item)
    #     else:
    #         p = self.head
    #         for i in range(idx - 1):
    #             p = p.next
    #         new = Node(item, p, p.next)
    #         p.next.prev = new
    #         p.next = new
    #         if new.next == None:
    #             self.tail = new

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    linked = [0] * M
    for i in range(M):
        linked[i] = LinkedList()

    for i in range(M):
        m = list(map(int, input().split()))
        for j in range(N):
            linked[i].addtoLast(m[j])

    # for i in range(M):
    #     p = linked[i].head
    #     for j in range(N):
    #         print(p.item, end=' ')
    #         p = p.next
    #     print()

    result = linked[0]
    for i in range(1, M):
        st = linked[i].head
        p = result.head
        for j in range(N * i):
            if p.item <= st.item:
                p = p.next
            elif j == 0:
                linked[i].tail.next = p
                p.prev = linked[i].tail
                result.head = st
            else:
                p.prev.next = st
                st.prev = p.prev
                p.prev = linked[i].tail
                linked[i].tail.next = p
                break
        if p == None:
            result.tail.next = st
            st.prev = result.tail
            result.tail = linked[i].tail

    print("#{}".format(tc), end=' ')
    p = result.tail
    for i in range(10):
        print(p.item, end=' ')
        p = p.prev
    print()