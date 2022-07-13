package util

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Run(solution func([]int) int) {
	reader := bufio.NewReader(os.Stdin)
	var data []int

	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		num, err := strconv.Atoi(strings.Trim(line, "\n"))
		if err != nil {
			log.Fatal(err)
		}
		data = append(data, num)
	}
	fmt.Println(solution(data))
}
