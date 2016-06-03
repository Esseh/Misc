/*
	This file is responsible for executing loaded templates.
*/
package main
import (
		"net/http"		// web server
		"html/template" // templates
)

//Runs the template.
func executeTemplate(res http.ResponseWriter,obj User){
	//Prepare template to execute.
	t,_ := template.New("name").Parse(file1)
	//Execute the template.
	t.Execute(res, obj)
}
