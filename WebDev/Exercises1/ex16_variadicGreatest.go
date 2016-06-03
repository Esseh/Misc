/*
	Kenneth Willeford
	1-25-16
	This program takes in no input. 
	It tests a variadic function to compute the greatest number in a group of numbers.
*/
package main
import "fmt"

//Takes in any number of arguments and computes the greatest integer among them.
func greatest (arg ...int) int{
	biggest := arg[0]			//Assuming that it will always have 1 or more elements. Initialize as first position.
	for _,i := range arg{		//Iterate through slice of size n
		if i > biggest{			//If i is bigger then biggest...
			biggest = i		//..then the new biggest is i!
		}
	}
	return biggest				//Return the biggest number we could find.
}

func main(){
	fmt.Printf("%d\n", greatest(1,7,42,18))	//Test case 1	Return Life
	fmt.Printf("%d\n", greatest(42,7,1,18))	//Test case 2	Return The Universe
	fmt.Printf("%d\n", greatest(1,7,18,42))	//Test case 3	Return Everything
}