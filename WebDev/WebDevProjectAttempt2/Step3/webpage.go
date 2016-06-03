/*
	This file is responsible for handling the request and responses to the server.
*/
package main
import "net/http"					 //web server

//Serves the executed template.
func webpage(res http.ResponseWriter,req *http.Request){
	//Grab the obj from the cookie data.
	obj := handleCookie(res,req)
	//Execute the template.
	executeTemplate(res,obj)
}