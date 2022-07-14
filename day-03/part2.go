package main

import (
	"github.com/dawidl022/advent-of-code-2021/day-03/util"
)

type MaskUnderflowError struct{}

func (e *MaskUnderflowError) Error() string {
	return "Mask cannot be less than 1"
}

func solution2(numbers []int, binDigitCount int) int {
	mask := 0b1 << (binDigitCount - 1)
	oxygenRatingCandidates := numbers
	o2ScrubberCandidates := numbers

	for len(oxygenRatingCandidates) > 1 || len(o2ScrubberCandidates) > 1 {
		if mask < 0b1 {
			util.Terminate(&MaskUnderflowError{})
		}

		if len(oxygenRatingCandidates) > 1 {
			zeros, ones := partitionBasedOnBit(oxygenRatingCandidates, mask)
			oxygenRatingCandidates = longerSliceOrRight(zeros, ones)
		}

		if len(o2ScrubberCandidates) > 1 {
			zeros, ones := partitionBasedOnBit(o2ScrubberCandidates, mask)
			o2ScrubberCandidates = shorterSliceOrLeft(zeros, ones)
		}

		mask >>= 1
	}

	return oxygenRatingCandidates[0] * o2ScrubberCandidates[0]
}

func partitionBasedOnBit(numbers []int, mask int) ([]int, []int) {
	var zeros []int
	var ones []int

	for _, num := range numbers {
		if num&mask == 0 {
			zeros = append(zeros, num)
		} else {
			ones = append(ones, num)
		}
	}

	return zeros, ones
}

func longerSliceOrRight[T any](a []T, b []T) []T {
	if len(a) > len(b) {
		return a
	}
	return b
}

func shorterSliceOrLeft[T any](a []T, b []T) []T {
	if len(a) <= len(b) {
		return a
	}
	return b
}

func main() {
	util.Run(solution2)
}
