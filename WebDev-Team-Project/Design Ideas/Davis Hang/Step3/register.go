package main
import(
	"net/http"
)

// The main page. The front of our Lorem Ipsum website.
func register(res http.ResponseWriter, req *http.Request){
	// Check if they're already logged in.
	_,err := req.Cookie("session-info")
	// If they aren't then let them through.
	if err!=nil{
		if(req.Method == "POST"){
			// From AJAX if everything is fine push the register request forward. (Second authentication handled within)
			registerRequest(res,req)
			// Redirect them once the registerRequest completes
			//http.Redirect(res, req, "/", http.StatusFound)
		} else { 
			// Set the content type to html , this was to fix a bug where the content header defaulted to text/plain
			res.Header().Set("Content-Type","text/html")
			// Execute our template
			registerT.Execute(res, nil)
		}
	} else {
		//If they're already logged in redirect them to the main page.
		http.Redirect(res, req, "/", http.StatusFound)
	}
}