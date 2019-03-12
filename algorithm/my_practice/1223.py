class Stack:
    def __init__(self, n):
        self.n = n
        self.stack = [0] * self.n
        self.top = -1

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
    result1 = Stack(N)
    result2 = Stack(N)

    for i in S:
        if i != '+' and i != '*':
            result1.push(int(i))
        elif i == '+':
            while result2.top != -1:
                result1.push(result2.pop())
            result2.push(i)
        elif i == "*":
            if result2.top == -1:
                result2.push(i)
            else:
                while result2.stack[result2.top] == "*" and result2.top != -1:
                    result1.push(result2.pop())
                result2.push(i)
    while result2.top != -1:
        result1.push(result2.pop())

    for i in range(N):
        if result1.stack[i] != '+' and result1.stack[i] != '*':
            result2.push(result1.stack[i])
        else:
            b = result2.pop()
            a = result2.pop()
            if result1.stack[i] == '+':
                result2.push(a + b)
            else:
                result2.push(a * b)
    ans = result2.stack[0]
    print("#{} {}".format(tc, ans))