# 2005. 파스칼의 삼각형 D2
import sys
sys.stdin=open('2005_input.txt', 'r')

"""
1
11
121
1331
"""

T=int(input())

for t in range(1,T+1):
    N=int(input())
    board=[]

    for i in range(N):
        #print(i)
        temp=[]
        for j in range(i+1):
            #print(i,j)
            if j==0:
                temp.append(1)
            elif j==i:
                temp.append(1)
            else:
                temp.append('*')

        board.append(temp)

    for x in range(len(board)):
        for y in range(x):
            if board[x][y]=='*':
                board[x][y]=board[x-1][y-1]+board[x-1][y]

    print(f'#{t}')
    for b in board:
        print(' '.join(list(map(str,b))))

