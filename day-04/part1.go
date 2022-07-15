package main

import (
	"github.com/dawidl022/advent-of-code-2021/day-04/logic"
	"github.com/dawidl022/advent-of-code-2021/day-04/util"
)

func solution1(numbers []int, boards []*logic.Board) int {
	for _, number := range numbers {
		for _, board := range boards {
			board.MarkNumberIfPresent(number)

			if board.HasWinningLine() {
				return number * board.SumOfUnmarkedNumbers()
			}
		}
	}
	util.Terminate(noWinningBoardError{})
	return -1
}

type noWinningBoardError struct{}

func (e noWinningBoardError) Error() string {
	return "no boards won from given input"
}

func main() {
	util.Run(solution1)
}
