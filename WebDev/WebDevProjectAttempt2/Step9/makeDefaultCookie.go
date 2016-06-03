/*
	This file is responsible for constructing a default cookie.
*/
package main
import "net/http"					 //web server


func makeDefaultCookie() (*http.Cookie){
	result := getDefaultValue()
	return &http.Cookie{				//Send out the constructed cookie.
		Name:  "session-info",
		Value: result,
		// Secure: true,
		HttpOnly: true,
	}
}