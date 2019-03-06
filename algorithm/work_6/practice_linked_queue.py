class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def isEmpty():
    return front == None

def enQueue(item):
    global front, rear
    newNode = Node(item)

    if isEmpty():
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear

    if isEmpty():
        return "에러!"
    else:
        item = front.item
        front = front.next
        if front == None:
            rear = None
        return item

front, rear = None, None
for i in range(1, 6):
    enQueue(i)
    print(rear.item)

for i in range(6):
    print(deQueue())