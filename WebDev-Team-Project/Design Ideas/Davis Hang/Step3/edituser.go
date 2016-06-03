package main
import (
	"net/http"
	"strings"
)

func changePassword(res http.ResponseWriter, req *http.Request, input string){
	// Get the user session
	cookie, err := req.Cookie("session-info")
	if err != nil{
		// This should never happen, but never too careful.
		return
	}
	// Parse the cookie value
	values := strings.Split(cookie.Value,",")
	var data User
	// Find original info in memcache
	data, err = retrieveFromMemcache(values[1],req)
	if err != nil {
		// Failing that look in datastore
		data, err = retrieveFromDatastore(values[1],req) 
		if err != nil{
			// This also shouldn't happen
			return
		}
	}
	data.Password = input
	err = storeInDatastore(data, values[1], req)
	if err != nil {
		// If something goes wrong. Best not to proceed.
		return
	}
	err = storeInMemcache(data, values[1], req)
	if err != nil {
		// If something goes wrong. Best not to proceed.
		return
	}
}

func edituser(res http.ResponseWriter, req *http.Request){
	if(authenticatedUser(req,res)){
		if(req.Method == "POST"){
			changePassword(res,req,req.FormValue("userPasswordInput"))
			http.Redirect(res, req, "/", http.StatusFound)
		} else {
			res.Header().Set("Content-Type","text/html")
			edituserT.Execute(res, nil)
		}
	}
}