// ref: https://gobyexample.com/
package main

import (
    "fmt"
    "sort"
)

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

func main() {
    activities := [][]int{{0,30}, {5, 10}, {10,20}};
    var res int = meetingRooms(activities)
    fmt.Println(res)
}
