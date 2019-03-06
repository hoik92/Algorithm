class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, idx, item):
        new = Node(item)
        if self.isEmpty():
            self.head = new
            self.top = new
        elif idx == -1:
            self.top.next = new
            self.top = new
        elif idx == 0:
            new.next = self.head
            self.head = new
        else:
            p = self.head
            for i in range(idx - 1):
                p = p.next
            new.next = p.next
            p.next = new

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    m = list(map(int, input().split()))

    link = LinkedList()
    for i in m:
        link.push(-1, i)

    for i in range(M):
        idx, item = map(int, input().split())
        link.push(idx, item)

    p = link.head
    for i in range(L):
        p = p.next

    print("#{} {}".format(tc, p.item))