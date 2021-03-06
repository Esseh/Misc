package main
import(
	"net/http"
	"fmt"
)

// The main page. The front of our Lorem Ipsum website.
func index(res http.ResponseWriter, req *http.Request){
	// If we don't have the cookie session-info construct our default cookie.
	cookie, exists := hasCookie(req,"session-info")
	if(!exists){ 
		cookie = defaultCookie()
		http.SetCookie(res,cookie) 
	}
	// Set the content type to html
	res.Header().Set("Content-Type","text/html")
	// Execute our template
	indexT.Execute(res, nil)
	// Print our UUID to show the maintaining of state.
	fmt.Fprintf(res ,cookie.Value)
	// Close the html tag on our page right after our UUID.
	fmt.Fprintf(res ,"</html>")

}