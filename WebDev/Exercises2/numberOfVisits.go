/*==============================================================
 "Create a webpage that displays how many times you have visited 
 it.
 Kenneth Willeford
	prints to stdout with res as the writer. 
==============================================================*/
package main
import (
		"net/http"
		"fmt"
		"strconv"
)


func lonelyPage(res http.ResponseWriter,req *http.Request){
	cookie, err := req.Cookie("num-visits")
	if err == http.ErrNoCookie{
		cookie = &http.Cookie{
			Name:"num-visits",
			Value:"0",
		}
	}
	numVisits, _ := strconv.Atoi(cookie.Value)
	numVisits++
	cookie.Value = strconv.Itoa(numVisits)
	http.SetCookie(res, cookie)
	fmt.Fprint(res,cookie.Value)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.HandleFunc("/favicon.ico",func(res http.ResponseWriter,req *http.Request){})
	http.ListenAndServe(":8080",nil)
}