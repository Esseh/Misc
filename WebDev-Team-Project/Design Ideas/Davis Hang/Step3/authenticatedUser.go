package main
import (
	"net/http"
	"strings"
)

func authenticatedUser(req *http.Request, res http.ResponseWriter) bool {
	// Get the cookie.
	cookie,err := req.Cookie("session-info")
	if err != nil {
		// If no cookie you don't belong here.
		http.Redirect(res, req, "/", http.StatusFound)
		return false
	}
	values := strings.Split(cookie.Value,",")
	// Grab our data from memcache
	data, err := retrieveFromMemcache(values[1], req)
	if err != nil{
		// Failing that grab it from data store.
		data, err = retrieveFromDatastore(values[1],req)
		if err != nil{
			// If not found they can't be authenticated.
			return false
		} else {
			// If found then place in memcache before continuing.
			err = storeInMemcache(data, values[1], req)
			if err != nil {}
		}
	}
	// Make sure they're legit.
	return data.Uuid == values[0]
}