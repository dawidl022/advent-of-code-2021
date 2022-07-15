package logic

const MARK = -1

type Board struct {
	Rows [][]int
	Won  bool
}

func (b *Board) MarkNumberIfPresent(number int) {
	for i := 0; i < len(b.Rows); i++ {
		for j := 0; j < len(b.Rows[i]); j++ {
			if b.Rows[i][j] == number {
				b.Rows[i][j] = MARK
			}
		}
	}
}

func (b *Board) SumOfUnmarkedNumbers() int {
	sum := 0

	for _, row := range b.Rows {
		for _, cell := range row {
			if cell != MARK {
				sum += cell
			}
		}
	}
	return sum
}

func (b *Board) HasWinningLine() bool {
	return b.hasWinningRow() || b.hasWinningColumn()
}

func (b *Board) hasWinningRow() bool {
	for _, row := range b.Rows {
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
	return false
}

func (b *Board) hasWinningColumn() bool {
	for j := 0; j < len(b.Rows[0]); j++ {
		allMarked := true
		for i := 0; i < len(b.Rows); i++ {
			if b.Rows[i][j] != MARK {
				allMarked = false
			}
		}
		if allMarked {
			return true
		}
	}
	return false
}
