# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    Password = list(map(int, input().split()))
    Command_num = int(input())
    Command = input()

    I_count = Command.count('I')
    D_count = Command.count('D')
    A_count = Command.count('A')
    for x in range(I_count):
        Command = Command.replace('I', '_i')
    for x in range(D_count):
        Command = Command.replace('D', '_d')
    for x in range(A_count):
        Command = Command.replace('A', '_a')

    Command = Command.split('_')
    Command.remove('')
    
    Command_list = []
    for x in Command:
        Command_list.append(x.split())

    for i in range(Command_num):
        if Command_list[i][0] == 'i':
            for j in range(int(Command_list[i][2])):
                Password.insert(int(Command_list[i][1])+j, int(Command_list[i][3+j]))
        elif Command_list[i][0] == 'd':
            for j in range(int(Command_list[i][2])):
                Password.pop(int(Command_list[i][1]))
        elif Command_list[i][0] == 'a':
            for j in range(int(Command_list[i][1])):
                Password.append(int(Command_list[i][2+j]))
    
    print(f"#{tc}", end=' ')
    for i in range(10):
        print(Password[i], end=' ')
    print()