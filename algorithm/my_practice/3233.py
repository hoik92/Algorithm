for tc in range(1, int(input())+1):
    A, B = map(int, input().split())
    ans = (A // B) ** 2
    print(f"#{tc} {ans}")