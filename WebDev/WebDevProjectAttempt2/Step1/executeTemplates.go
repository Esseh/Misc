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
	t,_ := template.New("name").Parse(file1)
	t.Execute(res, obj)
}
