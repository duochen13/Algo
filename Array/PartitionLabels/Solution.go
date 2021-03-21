// ref: https://gobyexample.com/
/*
 *  Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 */


package main

import "fmt"

func max(a int, b int) int {
    if a > b { return a }
    return b
}

func partitionLabels(s string) []string {
    var memo = make(map[string]int)
    for i, c := range(s) {
        var key string = string(c)
        if preIndex, ok := memo[key]; ok {
            memo[key] = max(preIndex, i)
        } else {
            memo[key] = i
        }
    }
    fmt.Println("memo: ", memo)
    res := make([]string, 0)
    var i, start int = 0, 0
    var furthest int = 0
    for i < len(s) {
        var chr string = string(s[i])
        if memo[chr] > furthest {
            furthest = memo[chr]
        }
        // find a substring | add to res | reset start of next substirng
        if i == furthest {
           res = append(res, s[start: i + 1])
           start = i
        }
        i += 1
    }
    return res
}

func main() {
    var s string = "ababcbacadefegdehijhklij"
    fmt.Println("s: ", s)
    var res []string = partitionLabels(s)
    fmt.Println(res)
}
