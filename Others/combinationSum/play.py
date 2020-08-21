def combinationSum(candidates, target):

    res = []
    def dfs(cur_sum, nums):
        if cur_sum > target:
            return
        if cur_sum == target:
            res.append(list(nums))
            return
        for i in range(len(candidates)):
            num = candidates[i]
            dfs(cur_sum + num, nums + [num])

    dfs(cur_sum=0, nums=[])

    return res


candidates = [2,3,6,7]
target = 7

res = combinationSum(candidates, target)

print(res)
