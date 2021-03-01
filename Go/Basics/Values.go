package main

import (
    "fmt"
    "math"
    "time"
)


func arrayTests() {
    var a [5]int64
    fmt.Println("emp: ", a)
    b := [5]int{2,3,4,6, 7}
    for i := 0; i < 5; i++ {
        fmt.Println(b[i])
    }
}

func switchTests() {
    t := time.Now()
    fmt.Println("t = ", t)
    switch {
        case t.Hour() < 12:
            fmt.Println("Its before noon")
        default:
            fmt.Println("Its after noon")
    }
}

func Loops() {
    i := 1
    for i <= 3 { fmt.Println(i); i += 1 }
    for j := 3; j <= 10; j++ { fmt.Println(j) }
}

func variables() {
    var a = "initial"
    fmt.Println(a)
    // so wierd
    var b, c int = 1, 2
    fmt.Println("b=",b,", c=",c)

    var e int
    fmt.Println("e=",e)

    var h string
    fmt.Println("h =", h)

    f := "apple"
    fmt.Println("f=",f)

    const n = 50000000
    const d = 3e20 / n
    fmt.Println(d)
    fmt.Println(int64(n))
    fmt.Println(math.Sin(n))
}

func values() {
    fmt.Println("go" + "lang")
    fmt.Println("5.0/3.0 = ", 5.0/3.0)
    fmt.Println("5/3 = ", 5/3)
    fmt.Println(true)
    fmt.Println(true && false)
    fmt.Println(!true)
}

func main() {
    arrayTests()
}
