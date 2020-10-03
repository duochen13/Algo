

import collections
import heapq


class datastream:
    def __init__(self, k):
        # num: frequency
        self.numFreqMemo = collections.defaultdict(int)
        self.numIndexMemo = collections.defaultdict(int)
        self.k = k
        self.data = []

    def add(self, num):
        # reset pq
        if num in self.numIndexMemo:
            index = self.numIndexMemo[num]
            self.numFreqMemo[num] += 1
            i = index - 1
            while i >= 0 and self.numFreqMemo[self.data[i]] < self.numFreqMemo[num]:
                # swap
                a, b = self.data[i], self.data[index]
                self.numIndexMemo[a], self.numIndexMemo[b] = self.numIndexMemo[b], self.numIndexMemo[a]
                self.data[i], self.data[index] = b, a
                i -= 1
        else:
            self.data.append(num)
            self.numFreqMemo[num] = 1
            self.numIndexMemo[num] = len(self.data) - 1

    def get(self):
        for num in self.data[:self.k]:
            print(num, end=" ")
        print('\n')

        
ds = datastream(k=3)
for num in [1,1,1,1,2,2,2,3,3,3,3,5,5]:
    ds.add(num)
ds.get()



"""
nums = [1,1,1,1,2,2,2,3,3,3,3,5,5]
k = 2
output: [1,3]

Q:
1. Is list nums sorted? No
2. Will k > len(set(nums))? 

assumption:
K > 0

General idea:
memo: {}
"""


# NlogK
def topKelementsOptimized(nums, k):
    memo = collections.defaultdict(int)
    for num in nums:
        memo[num] += 1

    pq = []
    # NlogK
    for num, freq in memo.items():
        heapq.heappush(pq, (freq, num))
        if len(pq) > k:
            heapq.heappop(pq)

    res = []
    while pq:
        _, num = heapq.heappop(pq)
        res.append(num)

    return res


# NlogN
def topKelementsOptimizedNlogN(nums, k):
    memo = collections.Counter(nums)
    pq = []
    # NlogN
    for num, freq in memo.items():
        heapq.heappush(pq, (-freq, num))
    # KlogN
    res = []
    for _ in range(k):
        _, num = heapq.heappop(pq)
        res.append(num)
    return res


