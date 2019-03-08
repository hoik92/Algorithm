for tc in range(1, int(input())+1):
    S = input()
    n = len(S)
    m = [""] * 5
    m[0] = "..#." * n + "."
    m[1] = ".#.#" * n + "."
    m[3] = m[1]
    m[4] = m[0]
    for i in range(n):
        m[2] += "#." + S[i] + "."
    m[2] += "#"
    for i in range(5):
        print(m[i])