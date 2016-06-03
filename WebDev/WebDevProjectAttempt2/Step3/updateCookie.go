package main
import(
	"encoding/json"				 //JSON
	"encoding/base64"			 //base64
	"net/http"					 //http
)

func updateCookie(cookie *http.Cookie,req *http.Request) string {
	obj := outputUser(cookie.Value)						// Grab current object data
	obj.Name= req.FormValue("name")						// Update Name
	obj.Age = req.FormValue("age")						// Update Age
	r, _ := json.Marshal(obj)							// Result to store
	return base64.StdEncoding.EncodeToString(r)			// Return the string encoded in base64. 
}