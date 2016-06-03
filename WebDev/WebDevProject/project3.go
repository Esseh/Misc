/*==============================================================
	Kenneth Willeford
	Project Part 3

==============================================================*/
package main
import (
		"net/http"						// web server
		"html/template" 				// templates
		"io/ioutil"						// file reading
		"github.com/nu7hatch/gouuid"	//UUID
//		"fmt"							// debugging
		"strings"						//split
)

//Type for User
type User struct{
	Name string
	Age string
}

//Holds a loaded file.
var file1 string

//Actually loads the file's contents.
func init(){
	temp, _ := ioutil.ReadFile("templates/file2.htemplate")
	file1 = string(temp)
}

//Serves the executed template.
func lonelyPage(res http.ResponseWriter,req *http.Request){
	//Prepare the cookie if it doesn't exist.
	cookie, err := req.Cookie("session-fino")
	if err != nil {
		id,_ := uuid.NewV4()
		cookie = &http.Cookie{
			Name:  "session-fino",
			Value: id.String() + "- - ",		//Empty values with - as delimiter
			// Secure: true,
			HttpOnly: true,
		}
		http.SetCookie(res,cookie)
	}
	
	//Update the cookie if data was submitted.
	if req.Method == "POST"{
		//New Entry
		newValue := req.FormValue("name") + "-" + req.FormValue("age")
		
		//Separate the old values.
		temp := strings.Split(cookie.Value,"-")
		
		//Place the new values inside the cookie.
		cookie.Value = temp[0] + "-" + newValue
	}
	
	//Grab new values to display on page.
	temp := strings.Split(cookie.Value,"-")
	obj := User{temp[1],temp[2]}
	
	//Execute the Template
	t,_ := template.New("name").Parse(file1)
	t.Execute(res, obj)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}