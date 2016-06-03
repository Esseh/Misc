/*==============================================================
 "Create a webpage that displays a name after taking a name as input.
 Kenneth Willeford
	prints to stdout with res as the writer. 
==============================================================*/
package main
import (
		"net/http"
		"fmt"
)

func lonelyPage(res http.ResponseWriter,req *http.Request){
		fmt.Fprint(res,`<!DOCTYPE html>
					<html>
					<head>
						<title></title>
					</head>

					<body>
						<form>
							Input your name:<br>
							<input type="text" name="name"><br>
						</form>
					</body>
					</html>`)
		fmt.Fprint(res,req.FormValue("name"))
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}