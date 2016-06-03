/*
	This file is responsible for determining what to do with a cookie.
*/
package main
import "net/http"					 //web server


func handleCookie(res http.ResponseWriter,req *http.Request) User {
	cookie, err := req.Cookie("session-info")			//Ensure that the cookie exists...
	if err != nil {
		cookie = makeDefaultCookie()
		http.SetCookie(res,cookie)
	}
	if req.Method == "POST" {							//If in POST
		cookie.Value = updateCookie(cookie,req)						//update the cookie
	}
	return outputUser(cookie.Value) 					//Return the constructed User.
}
