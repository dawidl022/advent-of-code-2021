package util

func CountIncreasing(data []int) int {
	count := 0

	for i := 0; i < len(data)-1; i++ {
		if data[i+1] > data[i] {
			count++
		}
	}
	return count
}
