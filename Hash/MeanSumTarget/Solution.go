// ref: https://gobyexample.com/

/*
Given A = [2, 1, 3] and S = 2, output = 3,
since the arithmetic means of fragments [2], [1, 3] and [2, 1, 3] are equal to 2.
Given A = [0, 4, 3, −1] and S = 2, your function should return 2, since fragments [0, 4] and [4, 3, −1] have an arithmetic mean equal to 2.
Given A = [2, 1, 4] and S = 3, your function should return 0, since there exist no contiguous fragments whose arithmetic mean is equal to 3.
*/

package main

import "fmt"

func meanTargetSum(nums []int, S int) int {
    fmt.Println("nums: ", nums)
    preSum := make([]int, len(nums) + 1)
    for i, num := range nums {
        preSum[i + 1] = preSum[i] + num
    }
    fmt.Println("preSum: ", preSum)
    var res int = 0
    for i := 0; i < len(preSum); i++ {
        for j := i + 1; j < len(preSum); j++ {
            diff := preSum[j] - preSum[i];
            if diff == S * (j - i) {
                res++
            }
        }
    }
    return res
}

func main() {
    fmt.Println("Writing golang program is fun!");
    var nums []int = []int{0,4,3,-1}
    var S int = 2
    res := meanTargetSum(nums, S)
    if res != 3 {
        panic("ERROR: res != 3")
    }
}
