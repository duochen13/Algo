package main

import (
	"fmt"
	"time"
)

func fib(n int) int {
	if n == 0 || n == 1 {
		return 1
	}
	return fib(n - 1) + fib(n - 2)
}


func main() {
	start := time.Now()
	fib(35)
	diff := time.Since(start)
	fmt.Println(diff)
	// fmt.Println(res)
}
