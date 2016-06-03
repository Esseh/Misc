/*==============================================================
	Kenneth Willeford
	Project Part 4

==============================================================*/
package main
import (
		"net/http"						// web server
		"html/template" 				// templates
		"io/ioutil"						// file reading
		"github.com/nu7hatch/gouuid"	// UUID
//		"fmt"							// debugging
		"encoding/json"					// JSON
		"encoding/base64"				// base64
)

//Type for User
type User struct{
	Uuid string
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
		//Get UUID
		id,_ := uuid.NewV4()
		//Construct instance of User
		temp := User{Uuid:id.String()}
		//Marshal this into JSON.
		b, _ := json.Marshal(temp)
		//Encode the JSON in base64
		encode := base64.StdEncoding.EncodeToString(b)
		cookie = &http.Cookie{
			Name:  "session-fino",
			Value: encode,
			// Secure: true,
			HttpOnly: true,
		}
		http.SetCookie(res,cookie)
	}
	
	//Update the cookie if data was submitted.
	if req.Method == "POST"{
		
		//Recover the JSON
		decode, _ := base64.StdEncoding.DecodeString(cookie.Value)
		
		//Value to hold the unmarshalled JSON
		var jsonValues User

		//Unmarshal the JSON
		json.Unmarshal(decode,&jsonValues)
				
		//New Entry
		jsonValues.Name = req.FormValue("name")
		jsonValues.Age = req.FormValue("age")
		
		//Convert back to JSON
		b, _ := json.Marshal(jsonValues)
		
		//Encode the JSON in base64
		encode := base64.StdEncoding.EncodeToString(b)
		
		//Place the new values inside the cookie.
		cookie.Value = encode
	}
	
	//Grab new values to display on page.
		//Recover the JSON
		decode, _ := base64.StdEncoding.DecodeString(cookie.Value)
		
		//Value to hold the unmarshalled JSON
		var obj User

		//Unmarshal the JSON
		json.Unmarshal(decode,&obj)
	
	//Execute the Template
	t,_ := template.New("name").Parse(file1)
	t.Execute(res, obj)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}