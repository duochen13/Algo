package main

import (
	"fmt"
	"os"
	"time"
	"strconv"
)

func fib(n int) int {
	if n == 0 || n == 1 {
		return 1
	}
	return fib(n - 1) + fib(n - 2)
}


func main() {
	N := os.Args[1]
	arg, _ := strconv.Atoi(N)
	start := time.Now()
	fib(arg)
	diff := time.Since(start)
	fmt.Println("Go ", diff)
}
