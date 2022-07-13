package main

import (
	"github.com/dawidl022/advent-of-code-2021/day-02/util"
	"github.com/dawidl022/advent-of-code-2021/day-02/util/direction"
)

func solution2(moves []direction.Move) int {
	aim := 0
	depth := 0
	horizontal := 0

	for _, move := range moves {
		switch move.Dir {
		case direction.DOWN:
			aim += move.Scalar
		case direction.UP:
			aim -= move.Scalar
		case direction.FORWARD:
			horizontal += move.Scalar
			depth += aim * move.Scalar
		}
	}
	return horizontal * depth
}

func main() {
	util.Run(solution2)
}
