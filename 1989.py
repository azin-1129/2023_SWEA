# 1989. 초심자의 회문 검사 D2

import sys
sys.stdin=open('1989_input.txt','r')

T=int(input())

for t in range(1,T+1):
    word=input()
    half=len(word)//2

    if len(word)%2==0:
        #print(word[0:half], ''.join(list(reversed(word[half:]))))
        if word[0:half]==''.join(list(reversed(word[half:]))):
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    else:
        #print(word[0:half], ''.join(list(reversed(word[half+1:]))))
        if word[0:half]==''.join(list(reversed(word[half+1:]))):
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')