package main

import (
	"math/rand"
	"testing"
)

var testarr []int

func init() {
	testarr = make([]int, 100000000)
	for i, _ := range testarr {
		testarr[i] = rand.Int() % 10
	}
}

func BenchmarkSum(b *testing.B) {
	for i := 0; i < b.N; i++ {
		sum(testarr)
	}
}
func BenchmarkSump(b *testing.B) {
	for i := 0; i < b.N; i++ {
		sump(testarr)
	}
}
