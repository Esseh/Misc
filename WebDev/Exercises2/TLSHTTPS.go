/*
	HTTPS/TLS server
	Kenneth Willeford
	Hosts a definitely, totally trustworthy website.
*/
package main
import (
	"fmt"
	"net/http"
)

func secureLonelyPage(res http.ResponseWriter,req *http.Request){
	fmt.Fprint(res,
	`<!DOCTYPE HTML>
	<html>
	<head>
	</head>
	<body>
		I'm totally trustworthy. I mean I DID sign for myself didn't I?..
	</body>
	</html>
	`)
}

func main(){
	go http.ListenAndServe(":8080", http.RedirectHandler("https://127.0.0.1:10443/",301))
	http.HandleFunc("/", secureLonelyPage)
	http.ListenAndServeTLS(":10443", "cert.pem", "key.pem", nil)
}