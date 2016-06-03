/*
	This file handles the loading of files into the global variables accessible elsewhere.
	The files are loaded in init into variables labeled file1..fileN
*/
package main
import "io/ioutil"		// file reading


// Holds the file to be executed later.
var file1 string
var file2 string
var file3 string

// Loads templates into the global variables.
func init(){
	//load file as byte array.
	temp, _ := ioutil.ReadFile("templates/loggedIn.htemplate")
	// Set global file1 to the loaded file.
	file1 = string(temp)
	//load file as byte array.
	temp, _ = ioutil.ReadFile("templates/loggedOut.htemplate")
	// Set global file2 to the loaded file.
	file2 = string(temp)
	temp, _ = ioutil.ReadFile("templates/benDrowned.htemplate")
	// Set global file3 to the loaded file.
	file3 = string(temp)
}

