/*==============================================================
 "Creates a session with uuid
 Kenneth Willeford
	prints to stdout with res as the writer. 
==============================================================*/
package main
import (
		"net/http"
		"fmt"
		"github.com/nu7hatch/gouuid"
)


func lonelyPage(res http.ResponseWriter,req *http.Request){
	cookie, err := req.Cookie("session")
	if err != nil {
		fmt.Fprint(res,"Have a cookie!\n")
		id,_ := uuid.NewV4()
		cookie = &http.Cookie{
			Name:  "session",
			Value: id.String(),
			// Secure: true,
			HttpOnly: true,
		}
		http.SetCookie(res,cookie)
	}
	fmt.Fprint(res,cookie)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}