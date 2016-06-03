/*==============================================================
	Kenneth Willeford
	Web Dev Project
==============================================================*/
package main
import "net/http"					 //web server

func main(){
	//Handle the Web Page
	http.HandleFunc("/",webpage)
	//Listen and Serve
	http.ListenAndServe(":8080",nil)
}