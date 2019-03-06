class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

head = Node(None)

def addtoFirst(data):
    global head
    head = Node(data, head)

def add(pre, data): # pre 다음 노드에 data 추가
    if pre == None:
        return
    else:
        new = Node(data, pre.next)
        pre.next = new

def addtoLast(data):
    global head
    if head == None:
        head = Node(data)
    else:
        p = head
        while p.next != None:
            p = p.next
        p.next = Node(data)

def delete(pre):
    if pre == None or pre.next == None:
        return
    else:
        pre.next = pre.next.next

addtoFirst(1)
# print(head.item)

a = head
add(a, 2)
# print(a.next.item, a.next.next)

addtoLast(3)
p = head
while p.next != None:
    print(p.item)
    p = p.next
print(p.item)