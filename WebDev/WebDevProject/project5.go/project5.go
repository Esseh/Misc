/*==============================================================
	Kenneth Willeford
	Project Part 4

==============================================================*/
package main
import (
		"net/http"						// web server
		"html/template" 				// templates
		"io/ioutil"						// file reading
)

//Type for User
type User struct{
	Uuid,Name,Age,Hmac string
}

// File Globals
var file1 string

// Load Files
func init(){
	temp, _ := ioutil.ReadFile("templates/file2.htemplate")
	file1 = string(temp)
}

// Serve Page
func lonelyPage(res http.ResponseWriter,req *http.Request){
	cookie, err := req.Cookie("session-fino")	// Cookie exists?
	if err != nil {								// If not make default one.
		cookie = defaultCookie()
		http.SetCookie(res,cookie)
	}	
	if req.Method == "POST"{					// Form submitted?
		cookie.Value = updateCookie(cookie,req)	// Update the cookie.
	}		
	obj, valid := unpackJSON(cookie)			// Unpack the cookie...
	if valid {									// ... and if valid...
		t,_ := template.New("name").Parse(file1)	// ...and Execute the page.
		t.Execute(res, obj)	
	} //else{	//If not...
	
	//}
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}