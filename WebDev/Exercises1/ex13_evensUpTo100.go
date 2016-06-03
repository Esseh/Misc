/*
	Kenneth Willeford
	1-25-16
	Program receives no input and prints every even number from 0 to 100.
*/
package main
import "fmt"


func main(){
	//Iterate from 0 to 100
	for i:=0;i<=100;i++{
		//If Number is even..
		if i%2 == 0{
			//... print it.
			fmt.Printf("%d\n",i)
		}
	}
}


	/* More concisely.
	for i:=0;i<=100;i+=2{
		fmt.Printf("%d\n",i)
	}
	*/