package main

import "fmt"

func judgeCircle(moves string) bool {
	x, y := 0, 0
	for _, i := range(moves) {
		switch i {
		case 'U':
			y++
		case 'D':
			y--
		case 'L':
			x--
		case 'R':
			x++
		}
	}
	return x == 0 && y == 0
}

func main() {
	str := "UDRL"
	res := judgeCircle(str)
	fmt.Println(res)
}
