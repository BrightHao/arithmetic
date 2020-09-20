package main

import "fmt"

func minimumTotal(triangle [][]int) int {
    if len(triangle) == 0 {
        return 0
    }
    n := len(triangle)
    res := triangle[n-1]
    for i:=n-2; i>=0; i-- {
        for j, val := range(triangle[i]) {
            var min int
            if res[j] >= res[j+1] {
                min = res[j+1]
            } else {
                min = res[j]
            }
            res[j] = val + min
        }
    }
    return res[0]
}

func main() {
	tri := [][]int{{2},{3,4}, {6,5,7},{4,1,8,3}}
	res := minimumTotal(tri)
	fmt.Println(res)
}
