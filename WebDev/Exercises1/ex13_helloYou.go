/*
	Kenneth Willeford
	1-25-16
	Program to receive a name as input and respond with "Hello <NAME>"
	The program accepts command line input to determine <NAME>
*/
package main
import (
	"fmt"
	"log"
)

func main(){
	var yourName string								//Variable to store name in.

	fmt.Printf("Enter your name..\n")				//Prompt user for name input.
	if _,err := fmt.Scan(&yourName); err != nil{	//Scan name in If fails exit with code -1. 
		log.Fatal("Scan failed due to",err)
	}
	
	fmt.Printf("Hello "+yourName+"\n")				//Print name.
}