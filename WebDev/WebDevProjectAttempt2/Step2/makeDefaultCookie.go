/*
	This file is responsible for constructing a default cookie.
*/
package main
import(
		"github.com/nu7hatch/gouuid" //UUID
		"net/http"					 //web server
)

func makeDefaultCookie() (*http.Cookie){
	//Get the cookie a unique universal id.
	id,_ := uuid.NewV4()
	//Send out the constructed cookie.
	return &http.Cookie{
		Name:  "session-info",
		Value: id.String(),
		// Secure: true,
		HttpOnly: true,
	}
}