/*
	This file is responsible for determining what to do with a cookie.
*/
package main
import (
	"net/http"					 //web server
	"fmt"
)

func handleCookie(res http.ResponseWriter,req *http.Request) User {
	cookie, err := req.Cookie("session-info")			//Ensure that the cookie exists...
	if err != nil {
		cookie = makeDefaultCookie()
		http.SetCookie(res,cookie)
	}
	if req.Method == "POST" {							//If in POST
		cookie.Value = updateCookie(cookie,req)						//update the cookie
		http.SetCookie(res,cookie)
	}
	//Some dastardly fiend modified the data here!
	//For simplicity it's only the terminal that gets printed to.
	cookie.Value = "ModifiedData"+cookie.Value
	if cookieIsBad(cookie){								//If the user modified the data.
		fmt.Println(req.RemoteAddr,": Tried to edit their information.")
	}
	return outputUser(cookie.Value) 					//Return the constructed User.
}
