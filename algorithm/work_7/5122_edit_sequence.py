class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def addtoLast(self, item):
        new = Node(item)
        if self.head == None:
            self.head = new
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new

    def add(self, idx, item):
        new = Node(item)
        p = self.head
        if idx == 0:
            new.next = self.head
            self.head = new
        else:
            for i in range(idx - 1):
                p = p.next
            new.next = p.next
            p.next = new

    def delete(self, idx):
        p = self.head
        if idx == 0:
            self.head = p.next
            p.next = None
        else:
            for i in range(idx - 1):
                p = p.next
            p.next = p.next.next

    def change(self, idx, item):
        p = self.head
        for i in range(idx):
            p = p.next
        p.item = item

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    m = list(map(int, input().split()))
    linked = LinkedList()
    for i in m:
        linked.addtoLast(i)

    for i in range(M):
        o = input().split()
        if o[0] == 'I':
            linked.add(int(o[1]), int(o[2]))
        elif o[0] == 'C':
            linked.change(int(o[1]), int(o[2]))
        elif o[0] == 'D':
            linked.delete(int(o[1]))

    p = linked.head
    result = 0
    for i in range(L):
        if p.next != None:
            p = p.next
        else:
            result = -1
            break
    if result != -1:
        result = p.item

    print("#{} {}".format(tc, result))