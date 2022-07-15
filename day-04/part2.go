package main

import (
	l "github.com/dawidl022/advent-of-code-2021/day-04/logic"
	"github.com/dawidl022/advent-of-code-2021/day-04/util"
)

func solution2(numbers []int, boards []*util.Board) int {
	countOfWonBoards := 0

	for _, number := range numbers {
		for _, board := range boards {
			if board.Won {
				continue
			}

			l.MarkNumberIfPresent(number, board)

			if l.HasWinningRow(board) {
				board.Won = true
				countOfWonBoards++
			}

			if countOfWonBoards == len(boards) {
				return number * l.SumOfUnmarkedNumbers(board)
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
