
"""
input: A = [2,1,3], S = 2, output = 3
input: A = [2,1,4], S = 3, output = 0
"""

import collections

def brutalMeanTargetSum(A, S):
    cnt = 0
    print("A:{}, S:{}".format(A, S))

    for i in range(len(A)):
        tmp = 0
        for j in range(i, len(A)):
            tmp += A[j]
            if tmp == S * (j - i + 1):
                print("A[{}:{}] = {}".format(i, j + 1, A[i:j+1]))
                cnt += 1
            elif tmp > S * (j - i + 1):
                break

    print("cnt: {}".format(cnt))
    return cnt

# preSum[j] - preSum[i] = S * (j - i)
def meanTargetSum(A, S):
    print("A:{}, S:{}".format(A, S))
    
    preSum = [0 for _ in range(len(A) + 1)]
    for i, num in enumerate(A, start=1):
        preSum[i] = preSum[i - 1] + num
    print("preSum:{}".format(preSum))
    
    cnt = 0
    memo = collections.defaultdict(int)
    for i, num in enumerate(preSum[1:]):
        tmp = preSum[i] - i * S
        print("tmp:{}, memo:{}".format(tmp, memo))
        if not tmp in memo:
            memo[tmp] = i
        elif tmp in memo and memo[tmp] != i:
            cnt += 1
    print("cnt: {}".format(cnt))
    return cnt

assert meanTargetSum(A=[2,1,3], S=2) == 3
# assert meanTargetSum(A=[2,1,4], S=3) == 0

