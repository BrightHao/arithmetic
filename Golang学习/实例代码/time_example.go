package main

import ( 
	"time"
	"fmt"
)

func main() {
	t1 := time.Now()
	time.Sleep(100000000)  // 100ms
	t2 := time.Now()
	fmt.Println(t2.Sub(t1))
}
