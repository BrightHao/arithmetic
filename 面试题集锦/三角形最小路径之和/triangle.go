package main

import "fmt"

func main() {
	array := [][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}
	num := solution(array)
	fmt.Println(num)
}

func solution(array [][]int) (num int) {
	le := len(array)
	res := array[le-1]
	for i:=le-2; i>=0; i-- {
		for j:=0; j<len(array[i]); j++ {
			var min int
			if (res[j] >= res[j+1]) {
				min = res[j+1]
			} else {
				min = res[j]
			}
			res[j] = min + array[i][j]
		}
	}
	return res[0]
}
