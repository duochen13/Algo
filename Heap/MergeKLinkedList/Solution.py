
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6


ptrs = [0,0,0]
1 4 5
1 3 4
2 6
find min(nums[ptr]), psuh to result,

(1, 0)
(1, 1)
(2, 0)
(4, 1)


Example 2:

Input: lists = []
Output: []
"""
import heapq

def BrutalMergeLists(lists):
    pq = []
    for i, l in enumerate(lists):
        for num in l:
            heapq.heappush(pq, (num, i))
    print("pq:{}".format(pq))

    res = []
    while pq:
        curNum, _ = heapq.heappop(pq)
        res.append(curNum)

    return res

def mergeLists(lists):
    pq, res = [], []

    while lists:
        for i in range(len(lists)):
            l = lists[i]
            if not lists[i]:
                continue
            heapq.heappush(pq, l[0])
            lists[i].pop(0)        
        print("pq:{}".format(pq))
        while pq:
            res.append(pq[0])
            heapq.heappop(pq)
        print("res:{}".format(res))
        print("lists:{}".format(lists))
    print("result:{}".format(res))
    return res


lists = [[1,4,5],[1,3,4],[2,6]]
res = mergeLists(lists)

print(res)


