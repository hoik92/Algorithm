"""
세상의 모든 팰린드롬

어떤 단어가 뒤에서 앞으로 거꾸로 썼을 때 원래의 단어와 같으면 이를 팰린드롬이라고 한다.

예를 들어 “madam”은 뒤에서 앞으로 읽어도 “madam”이기 때문에 팰린드롬이다.

그러나 “dog”는 뒤에서 앞으로 읽으면 “god”이기 때문에 팰린드롬이 아니다.

“doggod”은 뒤에서 앞으로 읽으면 “doggod”이므로 팰린드롬이다.

25XX년 경근이는 알파벳 소문자로 만든 단어들 중에서 팰린드롬인 것들을 모두 모아(그 단어에 뜻이 있건 없건) 데이터베이스에 넣었다.

요즘은 저장 장치가 발달해서 매우 많은 팰린드롬을 저장할 수 있기 때문에 모든 팰린드롬을 저장하지는 못할 것이라는 걱정은 하지 않아도 좋다.

경근이는 이 데이터베이스에서 특정한 패턴에 매치되는 팰린드롬을 찾으려고 한다.

경근이는 알파벳 소문자와 ‘?’를 사용한 패턴과 매치되는 단어를 찾는 명령을 내릴 수 있는데, ‘?’는 임의의 문자로 대체될 수 있는 와일드 카드이다.

예를 들어 경근이가 “a??a”에 매치되는 단어를 찾으라는 명령을 내리면, “assa”, “appa”등의 팰린드롬을 찾아 줄 것이다.

“asia”는 이런 패턴에 매치되기는 하지만 팰린드롬이 아니기 때문에 찾아주지 않을 것이고, “aa”, “aab”, “ana”, “aaaaa”는 패턴에 매치되지 않기 때문에 찾아주지 않을 것이다.

주어진 패턴과 매치되는 단어가 하나라도 있는지 아닌지 출력하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 길이가 1이상 20이하인 문자열이 주어진다.

이 문자열은 알파벳 소문자와 ‘?’만으로 이루어져 있다.

[출력]

각 테스트 케이스마다 주어진 패턴과 매칭되는 팰린드롬이 하나라도 존재하면 “Exist”를 아니라면 “Not exist”를 출력한다.

입력
2
hi
a??a

출력
#1 Not exist
#2 Exist
"""

import sys
sys.stdin = open('input.txt', 'r')

def is_pall(s_list):
    s = ''.join(s_list)
    if s == s[::-1]:
        return 'Exist'
    else:
        return 'Not exist'

for tc in range(1, int(input())+1):
    s = list(input())

    if not '?' in s:
        result = is_pall(s)
    else:
        q = []
        for i in range(len(s)):
            if s[i] == '?':
                q.append(i)

        for i in q:
            s[i] = s[-i-1]

        result = is_pall(s)

    print(f"#{tc} {result}")