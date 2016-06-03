/*
	This file is responsible for handling the request and responses to the server.
*/
package main
import "net/http"					 

//Serves the executed template.
func loggingout(res http.ResponseWriter,req *http.Request){
	changeAndGoToHome(res,req,"loggedOff")		//Set Logged Off and Redirect to main page.
}