package main

import (
	"github.com/Esseh/go-pprocess"
)

// Simple, serial sange sum
func sum(arr []int) int {
	totalSum := 0
	for _, v := range arr {
		totalSum += v
	}
	return totalSum
}

// Parallel sum utilizing partial sums.
func sump(arr []int) int {
	// Small Optimization and Bug Fix, if the array is small the serial algorithm will perform better.
	// Additionally, deadlock occurs if there are more processors than array elements.
	// Ya know, just in case it's run on a computer with more than 100000 cores and handling almost no data at all.
	if len(arr) < 100000 || len(arr) < pprocess.NumCPU {
		return sum(arr)
	}
	// Construct Output Buffer
	outputBuffer := make(chan int, pprocess.NumCPU)

	// Helper Function, performs partial sums.
	var parallelSum func(pprocess.Context, []int)
	parallelSum = func(ctx pprocess.Context, arr []int) {
		// If there a processors remaining...
		if !ctx.End() {
			// Get array section to sum over.
			partitionSize := len(arr) / pprocess.NumCPU
			// Begin next sum.
			go parallelSum(ctx.Next(), arr[partitionSize:])
			// Compute current sum and send it to the buffer.
			outputBuffer <- sum(arr[:partitionSize])
		} else {
			// If there are no processors remaining just send the sum of the remaining elements to the output buffer.
			outputBuffer <- sum(arr)
		}
	}

	// Begin parallel sums
	go parallelSum(pprocess.CreateContext(), arr)

	// Consolidate the sums made across processors and output the result.
	totalSum := 0
	for i := 0; i < pprocess.NumCPU; i++ {
		totalSum += <-outputBuffer
	}
	return totalSum
}

func main() {}
