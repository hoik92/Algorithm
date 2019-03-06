s = '(6+5*(2-8)/2)'

stack = [None] * 100
top = -1
result = []

def push(n):
    global top
    top += 1
    stack[top] = n

def pop():
    global top
    result = stack[top]
    stack[top] = None
    top -= 1
    return result

def prior(n):
    if n == '*' or n == '/':
        return 5
    elif n == '+' or n == '-':
        return 4
    elif n == '(':
        return 3
    elif n == ')':
        return 2
    else:
        return 1

for i in s:
    if top == -1 and prior(i) >= 3:
        push(i)
    elif prior(i) == 1:
        result.append(i)
    elif prior(i) == 3:
        push(i)
    elif prior(i) == 2:
        while prior(stack[top]) != 3:
            result.append(pop())
        pop()
    elif prior(i) > prior(stack[top]):
        push(i)
    elif prior(i) <= prior(stack[top]):
        while prior(i) <= prior(stack[top]):
            result.append(pop())
        push(i)
while top != -1:
    result.append(pop())

print(result)