/*
	Kenneth Willeford
	1-25-16
	Program to print the type of a variable.
	The program accepts no input and outputs the relevant types of the test variables.
*/
package main
import "fmt"

//Format string so as to print it's type.
func printTypeOf(input interface{}){
	fmt.Printf("%T\n",input)
}

func main(){
	testArray := []float32{1,2,3}
	printTypeOf("Hello World")		//string
	printTypeOf(1)					//int
	printTypeOf(3.14)				//float64
	printTypeOf(testArray)			//[]float32
}