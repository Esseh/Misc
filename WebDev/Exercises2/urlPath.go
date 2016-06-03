/*==============================================================
 "Create a webpage that displays the URL path using req.URL.path"
 Kenneth Willeford
	prints to stdout with res as the writer the path. 
==============================================================*/
package main
import (
		"net/http"
		"fmt"
)

func lonelyPage(res http.ResponseWriter,req *http.Request){
	fmt.Fprint(res,req.URL.Path)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}