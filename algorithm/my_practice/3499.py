for tc in range(1, int(input())+1):
    N = int(input())
    list_origin = input().split()
    length = len(list_origin)
    list_result = []

    if length % 2:
        list_1 = list_origin[:length//2 + 1]
        list_2 = list_origin[length//2 + 1:]
    else:
        list_1 = list_origin[:length//2]
        list_2 = list_origin[length//2:]
    
    for i in range(len(list_1)):
        list_result.append(list_1[i])
        if i == len(list_2):
            break
        list_result.append(list_2[i])

    print(f"#{tc}", end=' ')
    for i in list_result:
        print(i, end=' ')
    print()