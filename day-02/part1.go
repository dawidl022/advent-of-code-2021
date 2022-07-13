package main

import (
	"github.com/dawidl022/advent-of-code-2021/day-02/util"
	"github.com/dawidl022/advent-of-code-2021/day-02/util/direction"
)

func solution1(moves []direction.Move) int {
	depth := 0
	horizontal := 0

	for _, move := range moves {
		switch move.Dir {
		case direction.FORWARD:
			horizontal += move.Scalar
		case direction.DOWN:
			depth += move.Scalar
		case direction.UP:
			depth -= move.Scalar
		}
	}
	return horizontal * depth
}

func main() {
	util.Run(solution1)
}
