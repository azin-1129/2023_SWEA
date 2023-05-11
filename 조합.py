nums = [1, 2, 3, 4, 5]

answer_list = []

def combi(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(nums[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)

combi(0, [])
print(answer_list)