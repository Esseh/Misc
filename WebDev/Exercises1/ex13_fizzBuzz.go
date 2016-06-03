/*
	Kenneth Willeford
	1-25-16
	Program recieves no input.
	For multiples of 3 it prints Fizz, for multiples of 5 it prints Buzz, for multiples of both it prints FizzBuzz,
	and otherwise it will simply print the integer.
*/
package main
import "fmt"


func main(){
	for i:=0;i<=100;i++{						//Iterate from 0 to 100
		if i%3 == 0 && i%5 == 0{				//If Number is multiple of 3 and 5..
			fmt.Printf("FizzBuzz\n")		//... print FizzBuzz!
		}else if i%3==0{						//Otherwise if it is only a multiple of 3...
			fmt.Printf("Fizz\n")			//... print Fizz!
		}else if i%5==0{						//Otherwise if it is only a multiple of 5...
			fmt.Printf("Buzz\n")			//... print Buzz!
		}else{									//Otherwise only print the number. (How boring.)
			fmt.Printf("%d\n",i)
			
		}
	}
}