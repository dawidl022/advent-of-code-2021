package main

import (
	"github.com/dawidl022/advent-of-code-2021/day-04/logic"
	"github.com/dawidl022/advent-of-code-2021/day-04/util"
)

func solution2(numbers []int, boards []*logic.Board) int {
	countOfWonBoards := 0

	for _, number := range numbers {
		for _, board := range boards {
			if board.Won {
				continue
			}

			board.MarkNumberIfPresent(number)

			if board.HasWinningLine() {
				board.Won = true
				countOfWonBoards++
			}

			if countOfWonBoards == len(boards) {
				return number * board.SumOfUnmarkedNumbers()
			}
		}
	}
	util.Terminate(notAllBoardsWonError{})
	return -1
}

type notAllBoardsWonError struct{}

func (e notAllBoardsWonError) Error() string {
	return "not all boards won from given input"
}

func main() {
	util.Run(solution2)
}
