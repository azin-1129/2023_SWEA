# 1209. [S/W 문제해결 기본] 2일차 - Sum
import sys
sys.stdin=open('1209_input.txt', 'r')

for _ in range(10):
    t=int(input())

    board = []

    for _ in range(100):
        board.append(list(map(int,input().split()))) # 한 행씩 들어옴

    max_row=0 # 행 합
    max_col=0 # 열 합

    for b in board: # 행 체크
        if sum(b)>max_row:
            max_row=sum(b)

    for y in range(100): # 열 체크
        col_tmp=0 # 열 합
        for x in range(100):
            #print('x:', x, 'y:', y)
            col_tmp+=board[x][y]

        if col_tmp>max_col:
            max_col=col_tmp

    diag_right=0 # 오른 대각선
    diag_left=0 # 왼 대각선

    for i in range(100):
        diag_right+=board[i][i]

    for j in range(99,-1,-1): # 99~0
        #print('j ',99-j,j)
        diag_left+=board[99-j][j]

    print(f'#{t} {max([max_row, max_col, diag_right, diag_left])}')
