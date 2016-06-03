/*==============================================================
 "Creates a session with hmac, holds onto data
 Kenneth Willeford
	prints to stdout with res as the writer. 
==============================================================*/
package main
import (
		"net/http"
		"fmt"
		"crypto/hmac"
		"crypto/sha256"
)

//Copy and Pasted from Todd's example.
func getCode(data string) string {
	h := hmac.New(sha256.New, []byte("raka02asd2j01djmk"))
	return fmt.Sprintf("%x", h.Sum(nil))
}

func lonelyPage(res http.ResponseWriter,req *http.Request){
	cookie, err := req.Cookie("Session")
	if err == http.ErrNoCookie {
		cookie = &http.Cookie{
			Name:  "Session",
			Value: "",
			// Secure: true,
			HttpOnly: true,
		}
	}
	if req.FormValue("name") != "" {
		needsSalt := req.FormValue("name")
		cookie.Value = needsSalt + "|" + getCode(needsSalt) 
	}
	fmt.Fprint(res,`
		<!DOCTYPE html>
		<html>
			<body>
				<form method = "POST">
					`+cookie.Value+`
					<input type = "text" name = "name">
					<input type = "submit">
				</form>
			</body>
		</html>
	`)
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}
