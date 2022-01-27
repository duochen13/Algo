package main

import "fmt"
import "time"


func squares(nums []int, val chan int) int {
    res := 0
    for _, num := range nums {
        res += num * num
    }
    val <- res
    return res
}


func cubes(nums []int, val chan int) int {
    res := 0
    for _, num := range nums {
        res += num * num * num
    }
    val <- res
    return res
}


func main() {
    fmt.Println("this is main function!")
    nums := []int{1,2,3}
    squareVal := make(chan int)
    cubesVal := make(chan int)
    go squares(nums, squareVal)
    go cubes(nums, cubesVal)

    tmp := make(chan int)
    tmp <- 3
    time.Sleep(time.Second)
}
