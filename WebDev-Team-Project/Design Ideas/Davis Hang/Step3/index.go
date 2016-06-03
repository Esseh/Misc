package main
import(
	"net/http"
)

type LoginCheck struct{
	Url string
	UrlText string
	Edit string
}

// The main page. The front of our Lorem Ipsum website.
func index(res http.ResponseWriter, req *http.Request){
	
	/* Check if the user is logged in. */
	_, err := req.Cookie("session-info")
	var Status LoginCheck
	if(err != nil){ 
		Status = LoginCheck{Url:`login` , UrlText:`Log In`}
	} else {
		Status = LoginCheck{Url:`/logout` , UrlText:`Log Out`}
		Status.Edit = "true"
	}

	// Set the content type to html , this was to fix a bug where the content header defaulted to text/plain
	res.Header().Set("Content-Type","text/html")
	// Execute our template
	indexT.Execute(res, Status)
}