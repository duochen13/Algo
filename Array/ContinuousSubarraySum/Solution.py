
"""
input:
nums: a list of unsorted numbers, can be zero and negative
k: int
nums = [4,7,-2,1,8]
"""

def CSSPreSum(nums, k):
    N = len(nums)
    preSum = [0 for _ in range(N + 1)]
    for i in range(N):
        preSum[i + 1] = preSum[i] + nums[i]
    res = 0
    for i in range(N + 1):
        for j in range(i):
            if preSum[i] - preSum[j] == k:
                print(nums[j:i])
                res += 1
    return res

ref https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/

assert CSSPreSum(nums=[4,7,-2,1,5,8], k=5) == 2

"""
def findSubarraySum(arr, n, Sum):  
    prevSum = defaultdict(lambda : 0)  
    res = 0 
    currsum = 0 
    
    for i in range(0, n):   
    
        # Add current element to sum so far.  
        currsum += arr[i]  
    
        # If currsum is equal to desired sum,  
        # then a new subarray is found. So  
        # increase count of subarrays.  
        if currsum == Sum:   
            res += 1         
    
        # currsum exceeds given sum by currsum  - sum. 
        # Find number of subarrays having   
        # this sum and exclude those subarrays  
        # from currsum by increasing count by   
        # same amount.  
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]  
            
    
        # Add currsum value to count of   
        # different values of sum.  
        prevSum[currsum] += 1 
       
    return res  
"""


def CSSOptimized(nums, k):

