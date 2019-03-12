"""
괄호 짝짓기

4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.

이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성한다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 길이가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 유효성 여부를 1 또는 0으로 표시한다 (1 - 유효함, 0 - 유효하지 않음).

입력
182
(({<(({{[[[[<<[[(<[[{([{{{[<[[[{<<(<[[{}[]{}{}[]]]><><...
298
{(({[({([{(<[([(([<({[{{[[({{[({([<{(<[[((<{{[([{<<[{(<({[<(...

출력
#1 1
#2 0
"""

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    item = stack[top]
    stack[top] = 0
    top -= 1
    return item

for tc in range(1, 11):
    N = int(input())
    m = list(input())

    stack = [0] * N
    top = -1
    result = 1
    for i in range(N):
        if m[i] == '(' or m[i] == '<' or m[i] == '[' or m[i] == '{':
            push(m[i])
        else:
            tmp = pop()
            if i != N - 1 and top == -2:
                result = 0
            elif i == N - 1 and top != -1:
                result = 0
            elif (m[i] == ')' and tmp == '(') or (m[i] == '>' and tmp == '<') or \
                    (m[i] == ']' and tmp == '[') or (m[i] == '}' and tmp == '{'):
                pass
            else:
                result = 0
        if not result:
            break
    print("#{} {}".format(tc, result))