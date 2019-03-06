s = input()
N = len(s)
st = [0] * N
top = -1
result = True
i = 0

while i < N and result:
    if s[i] == '(' or s[i] == '{' or s[i] == '[':
        top +=1
        st[top] = s[i]

    if s[i] == ')' or s[i] == '}' or s[i] == ']':
        if top != -1:
            t = st[top]
            top -= 1
            if (s[i] == ')' and t != '(') or (s[i] == '}' and t != '{') or (s[i] == ']' and t != '['):
                result = False
        else:
            result = False
    i += 1

if top != -1:
    result = False
print(result)