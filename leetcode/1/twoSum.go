package main

import "fmt"

func twoSum(nums []int, target int) []int {
    // nums 切片
    // target 整型数字
    data := make(map[int]int)
    for i, j := range nums{
        sub := target - j
        if value, ok := data[sub]; ok {
            return []int{value, i}
        }
        data[j] = i
    }
    return []int{}
}

func main() {
	num := []int{2, 7, 11, 15}
	target := 9
	res := twoSum(num, target)
	fmt.Println(res)
}
