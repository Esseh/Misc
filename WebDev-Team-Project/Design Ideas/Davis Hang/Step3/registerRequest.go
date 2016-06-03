package main
import(
	"net/http"
	"github.com/nu7hatch/gouuid"
	"fmt"
)

func registerRequest(res http.ResponseWriter, req *http.Request){
	//If the username is empty don't even bother.
	if(req.FormValue("username") == "" || req.FormValue("password") == ""){
		return
	}
	// First check if user exists in Memcache
	data, err := retrieveFromMemcache(req.FormValue("username"), req)
	if err != nil {
		// Next check if user exists in Datastore.
		data, err = retrieveFromDatastore(req.FormValue("username"), req)
		if err != nil {
			//Because we didn't find a user we can construct the user.
			// Make a Unique User ID
			id,_ := uuid.NewV4()
			var newUser User
			// Place the UUID
			newUser.Uuid = id.String()
			// PASSWORD
			newUser.Password = req.FormValue("password")			
			// Store the user in the datastore.
			err := storeInDatastore(newUser, req.FormValue("username"), req)
			if err != nil{
				fmt.Fprint(res,"Problem Making User Datastore",err)
			}
			// Also update memcache
			err2 := storeInMemcache(newUser, req.FormValue("username"), req)
			if err2 != nil{
				fmt.Fprint(res,"Problem Making User Memcache",err2)
			}
			http.Redirect(res, req, "/", http.StatusFound)		
		} else {
			// Someone is trying to spoof a request, don't let them do anything.
			// Though we DID access datastore, put it in Memcache since it was found.
			storeInMemcache(data, req.FormValue("username"), req)
			fmt.Fprint(res,"Bad Idea Sir")
			return
		}
	}
	// If it got here it was found in memcache, so someone was spoofing a request.
	return
}

