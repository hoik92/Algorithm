# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    Password = list(map(int, input().split()))
    Command_num = int(input())
    Command = input()

    I_count = Command.count('I')
    D_count = Command.count('D')
    for x in range(I_count):
        Command = Command.replace('I', '_i')
    for x in range(D_count):
        Command = Command.replace('D', '_d')

    Command = Command.split('_')
    Command.remove('')
    
    Command_list = []
    for x in Command:
        Command_list.append(x.split())

    for i in range(Command_num):
        for j in range(int(Command_list[i][2])):
            if Command_list[i][0] == 'i':
                Password.insert(int(Command_list[i][1])+j, int(Command_list[i][3+j]))
            elif Command_list[i][0] == 'd':
                Password.pop(int(Command_list[i][1]))
    
    print(f"#{tc}", end=' ')
    for i in range(10):
        print(Password[i], end=' ')
    print()