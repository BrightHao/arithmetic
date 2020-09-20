package main

import (
	"fmt"
)

func main() {
	str := "abc"
	length := len(str)
	result := []string{}
	permute("", str, length, &result)
	fmt.Println(result)
}

func permute(combin string, rest string, max int, result *[]string) {
	if len(combin) == max {
		*result = append(*result, combin)
		return
	}
	for i, _ := range(rest) {
		permute(combin+string(rest[i]), rest[:i]+rest[i+1:], max, result)
	}
}
