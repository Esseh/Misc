/*==============================================================
	Kenneth Willeford
	Project Part 1 

==============================================================*/
package main
import (
		"net/http"						// web server
		"html/template" 				// templates
		"io/ioutil"						// file reading
		"github.com/nu7hatch/gouuid"	//UUID
		"fmt"							// debugging
)

//Basic Struct that holds the username.
type User struct{
	Username string
}

//Holds a loaded file.
var file1 string

//Actually loads the file's contents.
func init(){
	temp, _ := ioutil.ReadFile("templates/file1.htemplate")
	file1 = string(temp)
}

//Serves the executed template.
func lonelyPage(res http.ResponseWriter,req *http.Request){
	//Set the Cookie
	cookie, err := req.Cookie("session-fino")
	if err != nil {
		id,_ := uuid.NewV4()
		cookie = &http.Cookie{
			Name:  "session-fino",
			Value: id.String(),
			// Secure: true,
			HttpOnly: true,
		}
		http.SetCookie(res,cookie)
	}

	//Execute the Template
	obj := User{"Test User"}
	t,_ := template.New("name").Parse(file1)
	t.Execute(res, obj)
	
	//Debug Info
	fmt.Fprint(res,obj)
	fmt.Fprint(res,cookie)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}
