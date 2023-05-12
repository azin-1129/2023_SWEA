# 1946. 간단한 압축 풀기 D2
import sys
sys.stdin=open('1946_input.txt','r')
T=int(input())

for t in range(1,T+1):
    N=int(input())

    doc=[]

    for _ in range(N): # 알파벳, 숫자 쌍 수
        C,K=input().split()

        doc+=[C*int(K)]

    print(f'#{t}')

    doc=''.join(doc)
    #print(doc)

    for i in range(0,len(doc),10):
        print(doc[i:i+10])

