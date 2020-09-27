
"""
Given a non-empty array of integers, return the k most frequent elements.
Assumption: K is always valid

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

1. construct heap with tuples in the format of (freq, num)
[(3,1), (2,2), (1,3)]
2. pop until N = K
"""

import heapq
import collections

def topKFrequent(nums, k):
    if not nums:
        return []
    # construct heap with tuples in the format of (freq, num)
    pq = []
    memo = collections.Counter(nums)
    for num, freq in memo.items():
        heapq.heappush(pq, (-freq, num))
    # pop until N = K
    res = []
    i = 0
    while i < k:
        _, curNum = heapq.heappop(pq)
        res.append(curNum)
        i += 1
    return res


assert topKFrequent(nums=[1,1,1,2,2,3], k=2) == [1,2]
assert topKFrequent(nums=[1,1,2,2,2,2,4,4,4], k=2) == [2,4]

