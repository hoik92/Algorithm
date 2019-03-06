class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class PQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, item):
        new = Node(item)
        if self.isEmpty():
            self.rear = new
            self.front = new
        else:
            p = self.front
            while p != None:
                if new.item > p.item:
                    new.next = p.next
                    p.next = new
                    break
                p = p.next
            if self.rear.next != None:
                self.rear = new

    def deQueue(self):
        if not self.isEmpty():
            item = self.front.item
            self.front = self.front.next
            return item
        else:
            return '에러다 이녀석아'

q = PQueue()
q.enQueue(1)
q.enQueue(5)
q.enQueue(2)
q.enQueue(4)
q.enQueue(3)
for i in range(5):
    print(q.deQueue())

