package util

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/go-errors/errors"
)

func Run(solution func([]int, int) int) {
	reader := bufio.NewReader(os.Stdin)
	var data []int
	var binDigitCount int

	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		rawData := strings.Trim(line, "\n")
		binDigitCount = len(rawData)

		scalar, err := strconv.ParseInt(rawData, 2, 0)
		if err != nil {
			log.Fatal(err)
		}

		data = append(data, int(scalar))
	}

	fmt.Println(solution(data, binDigitCount))
}

// terminate with error
func Terminate(err error) {
	fmt.Fprintln(os.Stderr, errors.New(err).ErrorStack())
	fmt.Fprintf(os.Stderr, "error: %v\n", err)
	os.Exit(1)
}
