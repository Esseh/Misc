/*==============================================================
 "Create a webpage that displays.... name in localhost:8080/name
 Kenneth Willeford
	prints to stdout with res as the writer. 
==============================================================*/
package main
import (
		"net/http"
		"fmt"
		"strings"
)

func lonelyPage(res http.ResponseWriter,req *http.Request){
	name := strings.Split(req.URL.Path,"/")
	fmt.Fprint(res,name[len(name)-1])
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}