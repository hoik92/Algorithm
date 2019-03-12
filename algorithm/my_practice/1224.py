class Stack:
    def __init__(self, n):
        self.top = -1
        self.stack = [0] * n

    def push(self, item):
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        item = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return item

for tc in range(1, 11):
    N = int(input())
    S = input()
    hu = Stack(N)
    tmp = Stack(N)
    result = Stack(N)

    for i in S:
        if i == '(':
            tmp.push(i)
        elif i == ')':
            while tmp.stack[tmp.top] != '(':
                hu.push(tmp.pop())
            tmp.pop()
        elif i == '+':
            while tmp.stack[tmp.top] != '(' and tmp.top != -1:
                hu.push(tmp.pop())
            tmp.push(i)
        elif i == '*':
            while tmp.stack[tmp.top] == '*' and tmp.top != -1:
                hu.push(tmp.pop())
            tmp.push(i)
        else:
            hu.push(int(i))
    while tmp.top != -1:
        hu.push(tmp.pop())

    for i in range(hu.top + 1):
        if hu.stack[i] != '+' and hu.stack[i] != '*':
            result.push(hu.stack[i])
        else:
            b = result.pop()
            a = result.pop()
            if hu.stack[i] == '+':
                result.push(a + b)
            else:
                result.push(a * b)
    ans = result.stack[0]
    print("#{} {}".format(tc, ans))