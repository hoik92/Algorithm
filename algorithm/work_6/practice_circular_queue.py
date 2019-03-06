def isEmpty():
    global front
    global rear
    return front == rear

def isFull():
    global front
    global rear
    return front == (rear + 1) % (N+1)

def enQueue(n):
    global rear
    if isFull():
        print("에러!")
    else:
        rear = (rear + 1) % (N + 1)
        queue[rear] = n

def deQueue():
    global front
    if isEmpty():
        return "에러!!"
    else:
        front = (front + 1) % (N + 1)
        n = queue[front]
        queue[front] = 0
        return n

N = 5
queue = [0] * (N+1)
front, rear = 0, 0

for i in range(1, 6):
    enQueue(i)
    print(queue)

for i in range(1, 3):
    print(deQueue())
    print(queue)

for i in range(6, 8):
    enQueue(i)
    print(queue)