package main

import (
	"github.com/dawidl022/advent-of-code-2021/day-03/util"
)

func solution1(numbers []int, binDigitCount int) int {
	// use bitwise AND to get individual bit (&)
	// and use bitwise shift left (<<) to iterate through bits in number

	mask := 0b1
	gamma := 0
	epsilon := 0

	for i := 0; i < binDigitCount; i++ {
		one_count := 0

		for _, num := range numbers {
			if num&mask != 0 {
				one_count++
			}
		}

		if one_count > len(numbers)/2 {
			gamma += mask
		} else {
			epsilon += mask
		}

		mask <<= 1
	}

	return gamma * epsilon
}

func main() {
	util.Run(solution1)
}
