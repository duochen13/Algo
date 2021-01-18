

"""
Q: find median from a very large file which you cannot perform sort. f[i] does not work

input: [100,88,98,120]
output: [88,98,100,120]
"""


def combine(nums, l, mid, r):
    leftNums, rightNums = nums[l:mid], nums[mid:r]
    print("sortedLeftNums:{}, sortedRightNums:{}".format(leftNums, rightNums))
    i = j = k = 0
    while i < len(leftNums) and j < len(rightNums):
        print("i:{}, j:{}, k:{}".format(i,j,k))
        if leftNums[i] < rightNums[j]:
            nums[k] = leftNums[i]
            i += 1
        else:
            nums[k] = rightNums[j]
            j += 1
        k += 1
    while i < len(leftNums):
        nums[k] = leftNums[i]
        i += 1
        k += 1
    while j < len(rightNums):
        nums[k] = rightNums[j]
        k += 1
        j += 1
    print("mergedMums:{}".format(nums))


def mergeSort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) // 2
    leftNums, rightNums = nums[:mid], nums[mid:]
    mergeSort(leftNums)
    mergeSort(rightNums)
    # print("nums[:mid]={}, nums[mid:]={}".format(nums[:mid], nums[mid:]))
    combine(nums, 0, mid, len(nums))


nums = [2,4,5,1,9,6,8,7]
print("nums: {}".format(nums))

mergeSort(nums)

print("nums: {}".format(nums))

