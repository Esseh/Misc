/*
	This file handles the loading of files into the global variables accessible elsewhere.
	The files are loaded in init into variables labeled file1..fileN
*/
package main
import "io/ioutil"		// file reading


// Holds the file to be executed later.
var file1 string

// Loads templates into the global variables.
func init(){
	//load file as byte array.
	temp, _ := ioutil.ReadFile("templates/file1.htemplate")
	// Set global file1 to the loaded file.
	file1 = string(temp)
}

