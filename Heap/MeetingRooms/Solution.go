// ref: https://gobyexample.com/
package main

import (
    "fmt"
    "sort"
    "container/heap"
)

type PriorityQueue []int

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue)Less(i, j int) bool { return pq[i] < pq[j] }

func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(int)) }

func (pq *PriorityQueue) Pop() (interface{}) {
    l := len(*pq)
    v := *pq
    rem := v[l-1]
    v = v[:l-1]
    *pq = v
    return rem
}

func max(a int, b int) int {
    if a > b { return a }
    return b
}

func meetingRooms(activities [][]int) int {
    fmt.Println(activities)
    sort.SliceStable(activities, func(i, j int) bool {
        return activities[i][1] < activities[j][1]
    })
    fmt.Println(activities)
    var res, preEnd int = 1, 0
    for _, activity := range activities {
        curStart, curEnd := activity[0], activity[1]
        if curStart >= preEnd {
            preEnd = max(curEnd, preEnd)
        } else {
            res ++
        }
    }//for
    return res
}

func meetingRoomsHeap(activities [][]int) int {
    sort.Slice(activities, func(i, j int) bool {
        return activities[i][0] < activities[j][0]
    })
    var pq PriorityQueue
    for _, activity := range activities {
        curStart, curEnd := activity[0], activity[1]
        if len(pq) == 0 {
            heap.Push(&pq, curEnd)
            continue
        }
        heap.Push(&pq, curEnd)
        if curStart >= pq[0] {
            heap.Pop(&pq)
        }
    }
    return len(pq)
}

func main() {
    activities := [][]int{{0,30}, {5, 10}, {10,20}};
    var res int = meetingRoomsHeap(activities)
    fmt.Println(res)
}
