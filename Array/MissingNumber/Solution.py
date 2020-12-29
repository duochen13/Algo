


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
              l   r
              l  
              r    
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
avg =  9, 10


testcase 4:
        0 1 2 3 4
nums = [1,2,3,4,6]
        l       r
              l r
              
mid = 2, 3
nums[mid] = 3, 4
avg = 3.5

"""

# Assumption: nums is sorted
def findMissingNumberBS(nums):
    l, r = 0, len(nums) - 1

    avg, diff = 0, (nums[-1] - nums[0]) / (len(nums))
    medium = (nums[0] + nums[-1]) / 2

    while l < r:
        mid = l + (r - l) // 2
        # avg = (nums[l] + nums[r]) / 2
        avg = medium
        print("beforem l:{}, r:{}, nums[{}]={}, avg={}".format(l, r, mid, nums[mid], avg))
        if nums[mid] == avg:
            return avg - diff
        elif nums[mid] < avg:
            l = mid + 1
        else:
            r = mid
        print("after l:{}, r:{}, nums[{}]={}, avg={}".format(l, r, mid, nums[mid], avg))

    return nums[l] + diff if nums[l] > medium else nums[l] - diff


nums = [3,6,9,15,18]
# nums = [1,2,3,4,6]
# nums = [1,3,4,5]
# res1 = findMissingNumber(nums)

# nums = [1,3,4,5]
res2 = findMissingNumberBS(nums)
print(res2)
