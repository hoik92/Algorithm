class Node:
    def __init__(self, item, candy=1, next=None):
        self.item = item
        self.candy = candy
        self.next = next

def enQueue(item, candy):
    global front, rear
    newNode = Node(item, candy)

    if front == None:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def deQueue():
    global front, rear, candy
    if front == None:
        return
    else:
        item = front.item
        candy -= front.candy
        front = front.next
        if front == None:
            rear = None
        return item


front, rear = None, None
i = 0
candy = 20
while True:
    if i:
        c = front.candy + 1
        j = deQueue()
        enQueue(j, c)
    enQueue(i+1, 1)

    print(front.item, front.candy, candy)

    if candy <= 0:
        result = j
        break
    i += 1
print(j)