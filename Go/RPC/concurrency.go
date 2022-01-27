package main

import "fmt"


func worker(wid int, done chan bool) {
    fmt.Printf("worker %d is doing some serious job!\n", wid)
    done <- true
}

func main() {
    
    done := make(chan bool, 3)
    for wid:=0; wid<3; wid++ {
        go worker(wid, done)
    }

    for i:=0; i<3; i++ {
        <-done
    }

    fmt.Printf("type of channel done: %T\n", done)
    fmt.Println("all worker finished!")
}
