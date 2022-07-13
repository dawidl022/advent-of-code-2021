package main

import "github.com/dawidl022/advent-of-code-2021/day-01/util"

func solution2(data []int) int {
	windows := make([]int, 0, len(data)-2)

	for i := 0; i < len(data)-2; i++ {
		sum := data[i] + data[i+1] + data[i+2]
		windows = append(windows, sum)
	}
	return util.CountIncreasing(windows)
}

func main() {
	util.Run(solution2)
}
