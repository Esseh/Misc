/*
	Kenneth Willeford
	1-25-16
	Program receives no input and prints the sum of every multiple of 3 or 5 below 1000.
*/
package main
import "fmt"

func main(){
	accumulator := 0				//Initialize Accumulator at 0
	for i:=0; i<1000; i++{			//Iterate to below 1000
		if i%3 == 0 || i%5 == 0{	//If it's a multiple of 3 or 5...
			accumulator+=i		//... add it to the accumulator.
		}
	}
	fmt.Printf("%d\n",accumulator)	//Print our sum.
}