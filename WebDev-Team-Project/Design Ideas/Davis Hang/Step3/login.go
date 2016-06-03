package main
import(
	"net/http"
)

// The main page. The front of our Lorem Ipsum website.
func login(res http.ResponseWriter, req *http.Request){
	// Check if they're already logged in.
	_ ,err := req.Cookie("session-info")
	// If they aren't then let them through.
	if err!=nil{
		if(req.Method == "POST"){
			// From AJAX if everything is fine push the login request forward.(second authentication handled within.)
			loginRequest(res,req)
		} else { 
			// Set the content type to html , this was to fix a bug where the content header defaulted to text/plain
			res.Header().Set("Content-Type","text/html")
			// Execute our template
			loginT.Execute(res, nil)
		}	
	} else{
		//If they're already logged in redirect them to the main page.
		http.Redirect(res, req, "/", http.StatusFound)
	}
}