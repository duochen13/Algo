

# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 
import heapq

def canAttendMeetings(intervals):
    if not intervals:
        return True
    intervals.sort()
    preStart, preEnd = intervals.pop(0)
    while intervals:
        curStart, curEnd = intervals.pop(0)
        if (preEnd > curStart):
            return False
        preStart, preEnd = curStart, curEnd
    return True

def meetings(intervals):
    intervals.sort()
    pq = []
    cnt = 0
    for curStart, curEnd in intervals:
        if not pq:
            heapq.heappush(pq, curEnd)
            cnt += 1
        else:
            # unfinished, need extra room
            if (curStart >= pq[0]):
                heapq.heappop(pq)
            else:
                cnt += 1
            heapq.heappush(pq, curEnd)
    return cnt


if __name__ == '__main__':
    intervals = [[0,20],[5,15],[15,30],[30,40]]
    res = meetings(intervals)
    print(res)
