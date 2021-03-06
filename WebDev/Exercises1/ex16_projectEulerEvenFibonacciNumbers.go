/*
	Kenneth Willeford
	1-25-16
	From ProjectEuler Problem 2...
	
	"Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
	By starting with 1 and 2, the first 10 terms will be:
					1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
	find the sum of the even-valued terms."
	
	This is my solution.
*/

package main
import "fmt"

//Returns a closure with the environment of the parent function.
//This allows it to generate new even fibonacci numbers when it is called.
func evenFibGenerator() func()int{
		i := 1; j := 1				//First two values of sequence.
		return func()int{
			result := i+j;			//Get result(next step in sequence)
			i = j; j = result		//Advance i and j 1 step in sequence for next call.
			if result%2 == 0{		//If even return the result.
				return result
			}else{					//Otherwise return 0.
				return 0
			}
		}
	}

func main(){
	//Build the generator.
	evenFibs := evenFibGenerator()
	//Initialize the accumulator.
	accumulator:=0
	//Until our break condition (> 4000000)....
	for true{
		temp := evenFibs()
		if temp > 4000000{
			break
		} else {
			//Continue adding even fibonacci numbers to our accumulator.
			accumulator+=temp
		}
	}
	//Print our sum.
	fmt.Println(accumulator)
}