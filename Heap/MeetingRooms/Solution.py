
import heapq


# How many meeting rooms needed?

def meetingRoom(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x : x[0])
    pq = []
    heapq.heappush(pq, intervals[0][1])

    for i in range(1, len(intervals)):
        if intervals[i][0] >= pq[0]:
            heapq.heappop(pq)
        heapq.heappush(pq, intervals[i][1])
    
    return len(pq)


assert meetingRoom(intervals = [[10,20],[0,15],[15,30]]) == 2
assert meetingRoom(intervals = []) == 0
