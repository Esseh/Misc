/*
	Kenneth Willeford
	1-25-16
	This program takes in no input. It performs a multiple return of integer and bool.
	Details in the documentation of half. (line 10)
*/
package main
import "fmt"

//Returns half of the input and a bool related to it being even or not. (true is even)
func half(arg int) (int , bool){
	//Return half of the input and wether or not it was even.
	return arg/2 , arg%2==0		
}

func main(){
	var x int
	var y bool
	x,y = half(1)
	fmt.Printf("(%d,%t)\n", x, y)	//Test case 1, half(1) returns (0,false)
	x,y = half(2)
	fmt.Printf("(%d,%t)\n", x, y)   //Test case 2, half(2) returns (1,true)
}