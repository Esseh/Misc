package main
import(
	"net/http"
	"fmt"
)

// An API call that checks if a username exists. Meant to be used by AJAX.
func userNameExists(res http.ResponseWriter, req *http.Request){
	if(req.FormValue("username") == ""){
		fmt.Fprint(res,"wut")
		return
	}
	// Make sure only plain text is sent.
	res.Header().Set("Content-Type","text/plain")
	var err,err2 error
	// Check if the user exists in memcache.
	_, err = retrieveFromMemcache(req.FormValue("username"), req)
	if err != nil {
		// If user isn't in memcache check if user exists in datastore.
		_ ,err2 = retrieveFromDatastore(req.FormValue("username"), req)
	}
	// If the user exists in either return "exists"
	if(err != nil && err2 != nil){
		fmt.Fprint(res ,"doesn't exist")
	} else{ 
		// Otherwise return that it doesn't exist.
		fmt.Fprint(res ,"exists")
	}
}