// ref: https://gobyexample.com/
package main

import "fmt"

func onePass(nums []int, target int) []int {
    var memo = make(map[int]int)
    for i, num := range nums {
        j, ok := memo[num]
        memo[target - num] = i
        if ok {
            return []int{i, j}
        }
    }
    return []int{}
}

func main() {
    nums := []int{1,2,3,4};
    target := 6;
    var res []int = onePass(nums, target);
    fmt.Println("res: ", res);
}
