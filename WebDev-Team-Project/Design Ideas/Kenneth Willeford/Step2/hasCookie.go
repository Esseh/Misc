package main

import ("net/http")

// Checks if a cookie exists with the name chk.
func hasCookie(req *http.Request, chk string) (*http.Cookie,bool) {
	cookie, err := req.Cookie(chk)
	if err != nil {
		return cookie,false
	}
	return cookie,true
}