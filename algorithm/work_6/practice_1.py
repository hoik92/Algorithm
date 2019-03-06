def enQueue(n):
    global rear
    if isFull():
        print("에러!")
    else:
        rear += 1
        queue[rear] = n

def deQueue():
    global front
    if isEmpty():
        return "에러!"
    else:
        front += 1
        return queue[front]

def isEmpty():
    global rear
    global front
    if rear == front:
        return True
    return False

def isFull():
    global rear
    if rear == N - 1:
        return True
    return False

N = 3
queue = [0] * N
front, rear = -1, -1

for i in range(1, 4):
    enQueue(i)

for i in range(1, 4):
    print(deQueue(), end=' ')