import sys
sys.stdin=open('input.txt', 'r')
T=int(input())

comp=[1,2,3,4,5,6,7,8,9]

for t in range(1,T+1):
    flag=0

    sudoku=[]
    su_group=[ [] for _ in range(9) ] # 사각형 식별
    col_group=[ [] for _ in range(9) ] # 열 식별
    for _ in range(9):
        sudoku.append(list(map(int,input().split())))

    #print('가로 체크')
    for s in sudoku:
        if comp!=sorted(s): # 가로 체크
            print(f'#{t} {0}')
            flag=1
            break
    #print('--------------------------------')
    if flag==1: # 처리할 가치 X
        continue

    idx=0

    for x in range(0,9,3):
        su_g=sudoku[x:x+3]

        for g in su_g:
            for y in range(0,9,3):
                su_group[idx]+=g[y:y+3] # 사각형 그루핑
            idx+=1

    #print('사각 체크')

    for s in su_group:
        if comp!=sorted(s): # 사각형 체크
            print(f'#{t} {0}')
            flag=1
        #print(sorted(s))
            break
    #print('--------------------------------')

    if flag==1:
        continue

    for y in range(9):
        for x in range(9):
            col_group[y]+=[sudoku[x][y]] # 열 라인 그루핑

    #print('세로 체크')

    for s in col_group:
        if comp!=sorted(s): # 세로 체크
            print(f'#{t} {0}')
            flag=1
            break

    if flag==0: #통과
        print(f'#{t} {1}')