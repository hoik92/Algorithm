def find_triplet(card):
    count = [0] * 10
    for i in card:
        count[i] += 1
        if count[i] == 3:
            return 1
    return 0


def find_run(card):
    card = sorted(card)
    for i in range(len(card) - 2):
        if card[i] + 1 in card and card[i] + 2 in card:
            return 1
    return 0


for tc in range(1, int(input())+1):
    m = list(map(int, input().split()))
    a = [0] * 6
    b = [0] * 6
    result = 0

    for i in range(6):
        a[i] = m[2 * i]
        b[i] = m[2 * i + 1]

        if i >= 2:
            A = find_triplet(a[:i + 1])
            A += find_run(a[:i + 1])
            if A:
                result = 1
                break
            B = find_triplet(b[:i + 1])
            B += find_run(b[:i + 1])
            if B:
                result = 2
                break
        if result:
            break
    print(f"#{tc} {result}")
