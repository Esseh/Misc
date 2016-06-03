package main
import(
	"net/http"
	"fmt"
	"time"
)

func loginRequest(res http.ResponseWriter, req *http.Request){
	// Empty username or password? Ignore that nonsense.
	if(req.FormValue("username") == "" || req.FormValue("password") == ""){
		return
	}
		// First check if user exists in Memcache
		data, err := retrieveFromMemcache(req.FormValue("username"), req)
		if err != nil {
			fmt.Fprint(res,"MEMCACHE ERR",err)
			// Next check if user exists in Datastore.
			data, err = retrieveFromDatastore(req.FormValue("username"), req)
			if err != nil {
				fmt.Fprint(res,"DATASTORE ERR",err)
				//The user should've been verified by the AJAX.
				//Someone is spoofing.
				fmt.Fprint(res,"y u do dis")
			} else {
				// It was found in datastore, place in memcache
				err = storeInMemcache(data, req.FormValue("username") , req)
				if err != nil {}
			}
		}
		//HEY YOU ALREADY HAVE A COOKIE
		_, err = req.Cookie("session-id")
		if err == nil {
			fmt.Fprint(res,"stop reaching into the cookie jar!")
		} else {
			//Otherwise begin the session.
			http.SetCookie(res,&http.Cookie{
				Name: "session-info",
				Value: data.Uuid+","+req.FormValue("username"),
				MaxAge: int((time.Hour).Seconds()),
				Path: "/",
			})
			http.Redirect(res, req, "/", http.StatusFound)
		}
}