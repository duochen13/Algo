"""
Design a data structure that supports the following two operations:

1.void addNum(int num) - Add a integer number from the data stream to the data structure.
2.double findMedian() - Return the median of all elements so far.
 
Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

nums = [2 5 1 8 3 9 5]
       [1 2 3 5 5 8 9]
add(2), median = median(2)
add(5), median = median(2,5)
add(1), median = median(1,2,5)



General idea
(max val from relative small nums): 
[5, 3, 2, 1]
(min val from relative large nums): 
[5, 8, 9]
variant: maintain s.t. heap1.size() = heap2.size()

"""
import heapq
import statistics


class MedianFinder:

    def __init__(self):
        self.pq1 = []
        self.pq2 = []

    def addNum(self, num: int) -> None:
        # heapq.heappush(self.pq1, -num)
        # if not self.pq2 or -self.pq1[0] > self.pq2[0]:
        #     heapq.heappush(self.pq2, -1 * heapq.heappop(self.pq1))
        # if len(self.pq2) > len(self.pq1):
        #     heapq.heappush(self.pq1, -1 * heapq.heappop(self.pq2))
        heapq.heappush(self.pq1, -num)
        heapq.heappush(self.pq2, -heapq.heappop(self.pq1))
        if len(self.pq2) > len(self.pq1):
            heapq.heappush(self.pq1, -heapq.heappop(self.pq2))

    def findMedian(self) -> float:
        N = len(self.pq1) + len(self.pq2)
        if N % 2:
            return -self.pq1[0]
        return (-self.pq1[0] + self.pq2[0]) / 2


mf = MedianFinder()
tmp = []
for num in [-1,-2,-3,-4,-5]:
    mf.addNum(num)
    tmp.append(num)
    print("num:{}, out:{}, correct:{}".format(num, mf.findMedian(), statistics.median(tmp)))
    print("pq1:{}, pq2:{}".format(mf.pq1, mf.pq2))


"""
["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]

expected: [null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]

"""