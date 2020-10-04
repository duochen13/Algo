


"""
nums = [3,6,12]
res = 9

nums = [1,2,3,5]
res = 4

Assumption:
len(nums) >= 3
missing number does not exist in the boundaries
"""

def findMissingNumber(nums):
    assert len(nums) >= 3
    return (nums[0] + nums[-1]) * (len(nums) + 1) / 2 - sum(nums)

"""
testcase 1: 
        0 1 2 3  4
nums = [3,6,9,15,18]
        l         r
            l     r
            l  r    
mid: 2, 3
nums[mid] = 9, 15
(nums[l] + nums[r]) / 2 = 10, 13


testcase 2:
        0 1 2 3 
nums = [1,3,4,5]
        l     r
        l r
        lr  


mid = 1, 0
nums[mid] = 3, 1
avg = 3, 2


testcase 3:
        0 1 2 3 
nums = [3,6,9,15]
        l      r
          l    r
            l  r
mid: 1, 2, 2
nums[mid]: 6, 9, 9
(nums[l] + nums[r]) / 2 =  9, 10
"""

# Assumption: nums is sorted
def findMissingNumberBS(nums):
    l, r = 0, len(nums) - 1

    avg = 0
    while l < r:
        mid = l + (r - l) // 2
        avg = (nums[l] + nums[r]) / 2
        print("beforem l:{}, r:{}, nums[{}]={}, avg={}".format(l, r, mid, nums[mid], avg))
        if nums[mid] >= avg:
            r = mid - 1
        else:
            l = mid + 1
        print("after l:{}, r:{}, nums[{}]={}, avg={}".format(l, r, mid, nums[mid], avg))

    return nums[l] 
    

nums = [3,6,9,15,18]
# nums = [1,2,3,4,6]
nums = [1,3,4,5]
# res1 = findMissingNumber(nums)
res2 = findMissingNumberBS(nums)
print(res2)
