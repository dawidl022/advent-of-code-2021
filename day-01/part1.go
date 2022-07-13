package main

import "github.com/dawidl022/advent-of-code-2021/day-01/util"

func solution1(data []int) int {
	return util.CountIncreasing(data)
}

func main() {
	util.Run(solution1)
}
