/*
	Kenneth Willeford
	1-25-16
	Conditional template structure..
	I utilized text/template so as to produce easy to see output on the command line.
	This is my first time using them so I was tearing my hair out a lot, but after about 8 tutorials I found one whose ideas
	stuck. 
	In order to use this program you must pass in command line arguments. 
	A maximum of 3 will take effect. Each one extending the pipeline. If one is missing it will tell you. 
	
	I think I'll get used to the template style thinking as we go along and I learn to manipulate them more finely. :)
*/
package main

import (
    "os"
    "text/template"
)

//Three strings to test a three level nested structure.
type User struct{
	CodeA string	
	CodeB string
	CodeC string
}

func main(){
	//Grab Command Line Args
	args := os.Args[1:]
	//Make User Object
	object := User{}
	//If valid number of args assign to string.
	if len(args) > 0{
		object.CodeA = args[0]
	}
	//If valid number of args assign to string.
	if len(args) > 1{
		object.CodeB = args[1]
	}
	//If valid number of args assign to string.
	if len(args) > 2{
		object.CodeC = args[2]
	}
	
	//Creation of the Template
	condTemp := template.New("Triple Nesting")
	//The template structure. Nothing too complex. Just enough to play around with.
	condTemp.Parse(`
		{{if  .CodeA}}
					{{.CodeA}}
			{{if .CodeB}}
					{{.CodeB}}
			    {{if.CodeC}}
					{{.CodeC}}
				{{else}}
					CodeC:Missing
				{{end}}
			{{else}}
				CodeB:Missing
			{{end}}
		{{else}}
			CodeA:Missing
		{{end}}
		Pipeline: {{.}}
		`) 
	//Merge template and object and print to screen.
    condTemp.Execute(os.Stdout, object)
}