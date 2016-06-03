/*
	This file is responsible for handling the request and responses to the server.
*/
package main
import "net/http"				 

//Serves the executed template.
func loggingin(res http.ResponseWriter,req *http.Request){
	changeAndGoToHome(res,req,"loggedOn")		//Set Logged On and Redirect to main page.
}