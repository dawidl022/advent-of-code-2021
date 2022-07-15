package logic

import "github.com/dawidl022/advent-of-code-2021/day-04/util"

const MARK = -1

func MarkNumberIfPresent(number int, board *util.Board) {
	b := board.Rows

	for i := 0; i < len(b); i++ {
		for j := 0; j < len(b[i]); j++ {
			if b[i][j] == number {
				b[i][j] = MARK
			}
		}
	}
	board.Rows = b
}

func HasWinningRow(board *util.Board) bool {
	b := board.Rows

	for _, row := range b {
		allMarked := true
		for _, cell := range row {
			if cell != MARK {
				allMarked = false
				break
			}
		}
		if allMarked {
			return true
		}
	}

	for j := 0; j < len(b[0]); j++ {
		allMarked := true
		for i := 0; i < len(b); i++ {
			if b[i][j] != MARK {
				allMarked = false
			}
		}
		if allMarked {
			return true
		}
	}
	return false
}

func SumOfUnmarkedNumbers(board *util.Board) int {
	sum := 0

	for _, row := range board.Rows {
		for _, cell := range row {
			if cell != MARK {
				sum += cell
			}
		}
	}
	return sum
}
