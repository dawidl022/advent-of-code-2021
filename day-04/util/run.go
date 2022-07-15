package util

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Run(solution func([]int, []*Board) int) {
	reader := bufio.NewReader(os.Stdin)
	var boards []*Board

	line, err := reader.ReadString('\n')
	if err != nil {
		Terminate(fmt.Errorf("no lines read from Stdin"))
	}
	numbers := splitAsInts(strings.Trim(line, "\n"), ",")
	reader.ReadSlice('\n') // skip initial blank line

	currBoard := &Board{}
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		rawData := strings.Trim(line, "\n")
		if len(rawData) == 0 {
			boards = append(boards, currBoard)
			currBoard = &Board{}
			continue
		}

		row := splitAsInts(rawData, " ")
		currBoard.Rows = append(currBoard.Rows, row)
	}
	boards = append(boards, currBoard)

	fmt.Println(solution(numbers, boards))
}

// terminate with error
func Terminate(err error) {
	fmt.Fprintf(os.Stderr, "error: %v\n", err)
	os.Exit(1)
}

func splitAsInts(input string, delimiter string) []int {
	strs := strings.Split(input, delimiter)
	var res []int

	for _, str := range strs {
		if len(str) == 0 {
			continue
		}
		number, err := strconv.Atoi(str)
		if err != nil {
			// TODO try panics instead
			Terminate(err)
		}
		res = append(res, number)
	}
	return res
}
