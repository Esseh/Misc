/*
	This file is responsible for getting the updated cookie value for session-info
*/
package main
import(
	"encoding/json"				 //JSON
	"net/http"					 //http
	"strings"					 //String Parsing
)

func updateCookie(cookie *http.Cookie,req *http.Request) string {
	tempString := cookie.Value							// Ready string for parsing
	tempString = strings.Split(tempString,",")[0]		// Get left side of data pair.
	obj := outputUser(tempString)						// Grab current object data
	obj.Name= req.FormValue("name")						// Update Name
	obj.Age = req.FormValue("age")						// Update Age
	r, _ := json.Marshal(obj)							// Result to store
	// Return the string encoded in base64. Also add onto it delimited by a ';' the HMAC encoding.
	return sanitizedOutput(r)
}