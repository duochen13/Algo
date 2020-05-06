import collections

def subarraySum(nums, k):
    res = tmp = 0
    memo = collections.defaultdict(int)
    memo['0'] = 1 
    for i, num in enumerate(nums):
        tmp += num
        res += memo[str(tmp - k)]
        memo[str(tmp)] += 1
    return res


nums = [2,4,3,1,5,2]
k = 6


res = subarraySum(nums, k)

print(res)
