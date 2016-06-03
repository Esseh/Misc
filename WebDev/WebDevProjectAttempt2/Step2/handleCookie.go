/*
	This file is responsible for determining what to do with a cookie.
*/
package main
import "net/http"					 //web server

func handleCookie(res http.ResponseWriter,req *http.Request) User {
	//Ensure that the cookie exists...
	cookie, err := req.Cookie("session-info")
	if err != nil {
		//If the cookie doesn't exist make a default cookie.
		cookie = makeDefaultCookie()
		//And set it so it can be seen in the future.
		http.SetCookie(res,cookie)
	}
	//Return the constructed User.
	return User{cookie.Value}
}
