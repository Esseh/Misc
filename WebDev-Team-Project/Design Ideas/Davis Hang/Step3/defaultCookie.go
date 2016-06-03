package main

import(
	"net/http"
	"github.com/nu7hatch/gouuid"
	"time"
)

// The default cookie definition. Primarily for step 2.
func defaultCookie()(*http.Cookie){
	// Construct a cookie with a uuid.
	id,_ := uuid.NewV4()
	return &http.Cookie{
		Name:  "session-info",
		Value: id.String(),
		// Secure: true,
		//HttpOnly: true,
		MaxAge: int((time.Hour).Seconds()),
		Path: "/",
	}
}