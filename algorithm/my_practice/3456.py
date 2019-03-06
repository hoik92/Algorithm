for tc in range(1, int(input())+1):
    l = list(map(int, input().split()))

    for i in l:
        if l.count(i) == 1 or l.count(i) == 3:
            result = i
            break

    print(f"#{tc} {result}")