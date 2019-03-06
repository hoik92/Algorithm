P = [1, 1, 1, 2, 2]
for n in range(95):
    P.append(P[-1] + P[-5])


for tc in range(1, int(input())+1):
    N = int(input())
    print(f"#{tc} {P[N-1]}")