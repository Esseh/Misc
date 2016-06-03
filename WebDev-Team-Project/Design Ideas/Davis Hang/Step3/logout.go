package main
import(
	"net/http"
	"time"
)

// The main page. The front of our Lorem Ipsum website.
func logout(res http.ResponseWriter, req *http.Request){
	cookie,_ := req.Cookie("session-info")
	// The cookie is already dead.
	t := time.Now()
	t.Sub(time.Now())
	cookie.Expires = t
	cookie.Path = "/"
	// Apply the dead cookie.
	http.SetCookie(res,cookie)
	// Reload Page
	http.Redirect(res, req, "/", http.StatusFound)
}