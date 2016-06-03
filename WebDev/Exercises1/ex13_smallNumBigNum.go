/*
	Kenneth Willeford
	1-25-16
	Program recieves two inputs, a larger number and a smaller number.
	The program then prints the remainder of Large % Small.
*/
package main
import (
	"fmt"
	"log"
)

func getInt() int{
	var x int
	if _,err := fmt.Scan(&x); err != nil{	//Scan number in If fails exit with code -1. 
		log.Fatal("Scan failed due to",err)
	}
	return x
}

func main(){
	var largeNumber int								//Variable to store large number.
	var smallNumber int								//Variable to store small number.
	
	fmt.Printf("Enter Large Number..\n")			//Prompt user for large number.
	largeNumber = getInt()							//Get Large Number
	
	fmt.Printf("Enter Small Number..\n")			//Prompt user for small number.
	smallNumber = getInt()							//Get Small Number
	
	fmt.Printf("%d\n",largeNumber%smallNumber)		//Print the value of Large 'Mod' Small
}