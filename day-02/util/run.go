package util

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/dawidl022/advent-of-code-2021/day-02/util/direction"
)

func Run(solution func([]direction.Move) int) {
	reader := bufio.NewReader(os.Stdin)
	var data []direction.Move

	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		rawData := strings.Split(strings.Trim(line, "\n"), " ")
		scalar, err := strconv.Atoi(rawData[1])
		if err != nil {
			log.Fatal(err)
		}

		data = append(data, direction.Move{
			Dir:    direction.Direction(rawData[0]),
			Scalar: scalar,
		})
	}

	fmt.Println(solution(data))
}
