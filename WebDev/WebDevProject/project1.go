/*==============================================================
	Kenneth Willeford
	Project Part 1 
	Create a web page that serves an executed template.

==============================================================*/
package main
import (
		"net/http"		// web server
		"html/template" // templates
		"io/ioutil"		// file reading
		//"fmt"			// debugging
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
	obj := User{"Test User"}
	t,_ := template.New("name").Parse(file1)
	t.Execute(res, obj)
	//fmt.Fprint(res,"WORKING")
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}