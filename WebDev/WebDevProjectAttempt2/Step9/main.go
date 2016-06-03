/*==============================================================
	Kenneth Willeford
	Web Dev Project
==============================================================*/
package main
import "net/http"					 //web server

func main(){
	//Handle the Web Page
	http.HandleFunc("/",webpage)
	http.HandleFunc("/login",loggingin)
	http.HandleFunc("/logout",loggingout)
	//Listen and Serve
	http.ListenAndServe(":8080",nil)
}