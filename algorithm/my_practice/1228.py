# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    Password = list(map(int, input().split()))
    Command_num = int(input())
    Command = input().split('I')
    Command.remove('')
    Command_list = []
    for i in Command:
        Command_list.append(list(map(int, i.split())))
    
    for i in range(Command_num):
        for j in range(Command_list[i][1]):
            Password.insert(Command_list[i][0]+j, Command_list[i][2+j])
            length = len(Password)
            if length >= 10:
                for k in range(length-10):
                    Password.pop()
    
    print(f"#{tc}", end=' ')
    for i in Password:
        print(i, end=' ')
    print()