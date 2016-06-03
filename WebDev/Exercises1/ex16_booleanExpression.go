/*
	Kenneth Willeford
	1-25-16
	This program has an arbitrary function foo which can be called with the following parameters.
	foo(1,2)
	foo(1,2,3)
	aSlice := []int{1,2,3,4}
	foo(aSlice...)
	foo()
	So it can accept 0 or more parameters.
	A variadic should accommodate all of these behaviours because it processes it's arguments as a slice.
*/

package main
import "fmt"

func foo(arg ...int) int {
	return 0;
}

func main(){
	fmt.Printf("%d\n", foo(1,2))
	fmt.Printf("%d\n", foo(1,2,3))
	aSlice := []int{1,2,3,4}
	fmt.Printf("%d\n", foo(aSlice...))
	fmt.Printf("%d\n", foo())
}