import sys
sys.stdin=open('5215_input.txt', 'r')

max_cal=0
# 실패 ㅠ_ㅠ

# def rec(arr,N):
#     global max_cal
#
#     res=[]
#
#     for i in range(N-1):
#         print('i:',i)
#         elem=arr[i]
#         rest_arr=arr[i+1:]
#
#         for c in rec(rest_arr, N-2):
#             res.append([elem]+c)
#
#     print('res:',res)
#     chk = sum(map(lambda x: x[1], res))  # 칼로리합
#     if chk > L:  # 초과
#         return
#     else:
#         print('chk:',chk)
#         max_cal = chk  # 교체
#
#     return res


T = int(input())

for t in range(1, T + 1):
    N, L = map(int, input().split())  # 재료 수, 제한 칼로리

    ingredient_info = []  # 재료 정보

    for _ in range(N):
        ingredient_info.append(list(map(int, input().split())))  # 맛 점수, 칼로리

    # print('info:', ingredient_info)
    ingredient_info.sort(key=lambda x: (x[1],-x[0]))
    # 맛점수 내림차순, 칼로리 오름차순 정렬

    #print('info:', ingredient_info)

    temp = 0
    res_cal = 0 # cal 우선

    for score, cal in ingredient_info:
        temp += cal

        if temp > L:
            break
        res_cal += score

    ingredient_info.sort(key=lambda x: (-x[0],x[1])) # 점수 우선

    res_sco=0

    for score, cal in ingredient_info:
        temp += cal

        if temp > L:
            break
        res_sco += score

    # rec(ingredient_info, N)
    # print(f'#{t} {max_cal}')

    if res_cal>res_sco:
        print(f'#{t} {res_cal}')
    else:
        print(f'#{t} {res_sco}')