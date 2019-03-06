# import sys
# sys.stdin = open('input.txt', 'r')

planet_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(int(input())):
    T, length = input().split()
    length = int(length)

    planet_case = input().split()
    earth_case = []

    for i in planet_case:
        earth_case.append(planet_num.index(i))
    
    earth_case.sort()

    print(T)
    for i in earth_case:
        print(planet_num[i], end=' ')
    print()