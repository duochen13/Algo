// ref: https://gobyexample.com/
package main

import "fmt"
import "time"
import "sync"


func worker(wid int, jobDone chan int, isMap bool) {
    if isMap {
        fmt.Printf("Map ")
    } else {
        fmt.Printf("Reduce ")
    }
    fmt.Printf("worker %d start!\n", wid)
    //time.Sleep(time.Second)
    fmt.Printf("worker %d end!\n", wid)
    jobDone <- wid
}

func testChannel() {
    jobDone := make(chan int)

    // distirbute jobDone to workers 
    fmt.Println("mapp")
    for i:=0; i<3; i++ {
        i := i
        fmt.Println("jobDone i=", i)
        go worker(i, jobDone, true)
    }
    for i:=0; i<3; i++ {
        <-jobDone
    }

    // distirbute jobDone to workers
    fmt.Println("reduce")
    for i:=0; i<3; i++ {
        i := i
        fmt.Println("jobDone i=", i)
        go worker(i, jobDone, true)
    }
    for i:=0; i<3; i++ {
        <-jobDone
    }
}

func doJob(wid int) {
    fmt.Printf("start do job=%d\n", wid)
    time.Sleep(time.Second)
    fmt.Printf("end do job=%d\n", wid)
}

func testCloseChannel() {
    jobs := make(chan int, 5)
    done := make(chan bool)

    go func() {
        for {
            j, more := <-jobs
            if more {
                fmt.Println("received job=", j)
                doJob(j)
            } else {
                fmt.Println("received all jobs")
                done <- true
                return
            }
        }
    }()

    // map
    for j:=1; j<3; j++ {
        jobs <- j
        fmt.Println("sent map job=", j)
    }
    // reduce
    for j:=3; j<5; j++ {
        jobs <- j
        fmt.Println("sent reduce job=", j)
    }
    
    close(jobs)
    fmt.Println("sent all jobs")
    <-done
}

func testRangeChannel() {
    queue := make(chan int)
    //queue <- 0
    //queue <- 1
    //close(queue)


    for i:=0; i<2; i++ {
        go worker(i, queue, true)
    }
    for i:=0; i<2; i++ {
        <-queue
    }

    for i:=0; i<2; i++ {
        go worker(i, queue, false)
    }
    for i:=0; i<2; i++ {
        <-queue
    } 
}

func testWaitGroup() {
    var wg sync.WaitGroup // Add, Wait, Done

    for i:=1; i<=5; i++ {
        wg.Add(1)
        i:=i
        go func() {
            defer wg.Done()
            doJob(i)
        }()
    }

    wg.Wait()
}

func main() {
    //testRangeChannel()
    testWaitGroup()
    fmt.Println("Writing golang program is fun!");
}
