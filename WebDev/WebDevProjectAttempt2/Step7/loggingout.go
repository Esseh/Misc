/*
	This file is responsible for handling the request and responses to the server.
*/
package main
import (
	"net/http"
	"strings"
	"fmt"
	"encoding/base64"
	"encoding/json"
)					 

//Serves the executed template.
func loggingout(res http.ResponseWriter,req *http.Request){
	cookie, err := req.Cookie("session-info")			//Ensure that the cookie exists...
	if err == nil {
		if cookieIsBad(cookie){
			//Someone was naughty.
			fmt.Println(req.RemoteAddr,": Tried to edit their information at log out.")
		} else{
			//Get data and set to loggedOff
			var user User
			tempString := strings.Split(cookie.Value,",")[0]
			decoded, _ := base64.StdEncoding.DecodeString(tempString)
			json.Unmarshal(decoded,&user)
			user.LoggedIn = "loggedOff"
			r, _ := json.Marshal(user)
			cookie.Value = sanitizedOutput(r)
			http.SetCookie(res,cookie)
			
			if !cookieIsBad(cookie){								//If the cookie is good.
				http.Redirect(res, req, "/", http.StatusFound)
			} else {
				//Someone was naughty.
				fmt.Println(req.RemoteAddr,": Tried to edit their information at log out.")
			}
		}
	}
}