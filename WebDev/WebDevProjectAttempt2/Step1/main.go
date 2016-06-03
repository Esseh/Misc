/*==============================================================
	Kenneth Willeford
	Web Dev Project
==============================================================*/
package main
import (
		"net/http"		// web server
)

//Serves the executed template.
func lonelyPage(res http.ResponseWriter,req *http.Request){
	obj := User{"Test User"}
	executeTemplate(res,obj)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}