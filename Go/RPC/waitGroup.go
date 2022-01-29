// ref: https://gobyexample.com/
package main

import "fmt"
import "time"
import "sync"

func worker(id int) {
    fmt.Printf("worker %d starting\n", id)
    time.Sleep(time.Second)
    fmt.Printf("worker %d done\n", id)
    //    done <- id
}

func testWaitGroup() {
    var wg sync.WaitGroup
    for i:=1; i<=5; i++ {
        wg.Add(1)
        i := i
        go func() {
            defer wg.Done()
            worker(i)
        }()
    }
    // wg.Wait()
    fmt.Println("all job done!")
}

func testWGC() {
    var wg sync.WaitGroup
    jobs := make(chan int)
    fmt.Println("TestWGC")
    go func() {
        for i:=0; i<3; i++ {
            i := i
            wg.Add(1)
            jobs <- i
        }
        wg.Wait()
        close(jobs)
    }()

    for i := range jobs {
        i := i
        go func() {
            fmt.Printf("worker %d start\n", i)
            time.Sleep(time.Second)
            fmt.Printf("worker %d end\n", i)
            wg.Done()
        }()
    }//for
}

func main() {
    testWGC()
}
